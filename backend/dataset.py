import json
import collections
import tqdm
import numpy as np

print("Loading dataset")

# Load molecule database
with open("datasets/molecules.json") as f:
    molecules = json.load(f)
    molecules = [m for m in molecules if m["SMILES"] and m["CAS"]]

# Load dataset and metadata
with open("datasets/dataset.json") as f:
  dataset = json.load(f)

smiles_to_all_concentrations = collections.defaultdict(list)
for d in dataset:
  for aroma in d["ingredients"]:
    try:
      if not aroma["SMILES"]:
        raise RuntimeError("Invalid SMILES")
      smiles_to_all_concentrations[aroma["SMILES"]].append(aroma["concentration"])
    except Exception as e:
      continue

smiles_to_concentration = {k:np.mean(v).item() for k,v in smiles_to_all_concentrations.items()}

all_smiles = {m["SMILES"] for m in molecules}.intersection(smiles_to_all_concentrations.keys())

smiles_to_all_concentrations = {s:smiles_to_all_concentrations[s] for s in all_smiles}
smiles_to_aroma = {m["SMILES"]: m for m in molecules if m["SMILES"] in all_smiles}

# Load embedding information
with open("datasets/smiles_to_embed.json") as f:
  smiles_embed = json.load(f)
  smiles_embed = {s:smiles_embed[s] for s in all_smiles}

for k, v in smiles_embed.items():
  smiles_embed[k] = np.array(v)

def get_fpsize():
    return len(next(iter(smiles_embed.values())))

def get_embed(smiles):
    return smiles_embed[smiles]

def entire_smiles_crate():
  for smiles in smiles_embed.keys():
    yield smiles

# Load prediction information
with open("datasets/smiles_to_predictions.json") as f:
  smiles_predictions = json.load(f)
  smiles_predictions = {s:smiles_predictions[s] for s in all_smiles}

def get_predictions(smiles):
    return smiles_predictions[smiles]

def get_concentration(smiles):
    return smiles_to_concentration[smiles]

def has_data(smiles):
    return smiles in smiles_to_concentration

def get_aroma(smiles):
    return smiles_to_aroma[smiles]
