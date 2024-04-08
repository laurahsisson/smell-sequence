import collections

import torch
import numpy as np

import dataset

start_token = np.ones(dataset.get_fpsize())
end_token = -1*np.ones(dataset.get_fpsize())

BATCH_FIRST = True

def make_embed_dict(aroma):
  structure = smiles_embed[aroma["SMILES"]]
  concentration = aroma["concentration"]/smiles_to_concentration[aroma["SMILES"]]
  return {"structure":structure,"concentration":concentration}


class Model(torch.nn.Module):
  def __init__(self,hidden_size,num_layers,dropout):
    super().__init__()
    # fp_size + concentration (of size 1)
    # Removing dropout if num_layers == 1 because LSTM doesn't like that.
    self.lstm = torch.nn.LSTM(dataset.get_fpsize()+1,hidden_size,num_layers=num_layers,dropout=dropout if num_layers > 1 else 0,batch_first=BATCH_FIRST)
    self.out_structure = torch.nn.Linear(hidden_size,dataset.get_fpsize())
    self.out_concentration = torch.nn.Linear(hidden_size,1)

  def forward(self, x, hidden=None):
    x = torch.cat([x["structure"],x["concentration"].unsqueeze(-1)],dim=-1).float()
    output, hidden = self.lstm(x, hidden)
    structure = self.out_structure(output)
    concentration = self.out_concentration(output)
    if BATCH_FIRST:
      hidden = hidden[0].transpose(0,1), hidden[1].transpose(0,1)
    return structure, concentration.squeeze(-1), hidden

def make_models(config):
  model = Model(hidden_size=2**config["hidden_dim"],num_layers=config["num_layers"],dropout=config["dropout"])
  return {
      "model": model,
      "optimizer":torch.optim.Adam(model.parameters(), lr=config["lr"]),
      }

print("Loading model")
config = torch.load("models/config.pt")
model = make_models(config)["model"]
state_dict = torch.load("models/model.pt")
model.load_state_dict(state_dict)

def get_top_k(k,aroma_sequence,smiles_crate=[]):
  prior_embed = np.array([start_token] + [dataset.get_embed(aroma["SMILES"]) for aroma in aroma_sequence])
  prior_concentration = np.array([0] + [aroma["concentration"] for aroma in aroma_sequence])

  prior_smiles = {aroma["SMILES"] for aroma in aroma_sequence}
  prior_input = {"structure":torch.tensor(prior_embed).unsqueeze(0),"concentration":torch.tensor(prior_concentration).unsqueeze(0)}
  with torch.no_grad():
    structure, concentration, _ = model(prior_input)
  structure, concentration = structure[0,-1,:], concentration[0,-1]

  probs = collections.Counter()

  smiles_crate = smiles_crate if smiles_crate else dataset.entire_smiles_crate()
  for smiles in smiles_crate:
    if smiles in prior_smiles:
      continue
    embed = dataset.get_embed(smiles)
    probs[smiles] = torch.nn.functional.cosine_similarity(torch.tensor(embed),structure,dim=-1).numpy().item()

  results = []
  for smiles, p in probs.most_common(k):
    results.append({"SMILES":smiles,"probability":p,"concentration":dataset.get_concentration(smiles)*concentration.numpy().item()})
  
  return results
