import json
import collections
import tqdm
import numpy as np

print("Loading dataset")

# Load molecule database
with open("datasets/molecules.json") as f:
    molecules = json.load(f)
    molecules = [m for m in molecules if m["SMILES"] and m["CAS"]]

# Load metadata
with open("datasets/smiles_to_metadata.json") as f:
  metadata = json.load(f)

all_smiles = {m["SMILES"] for m in molecules}.intersection(metadata.keys())

metadata = {s:metadata[s] for s in all_smiles}
aromas = {m["SMILES"]: m for m in molecules if m["SMILES"] in all_smiles}

for k, v in metadata.items():
  metadata[k]["embedding"] = np.array(metadata[k]["embedding"])

def get_fpsize():
  return len(next(iter(metadata.values()))["embedding"])

def get_embed(smiles):
    return metadata[smiles]["embedding"]

def entire_smiles_crate():
  for smiles in metadata.keys():
    yield smiles

def get_predictions(smiles):
    return metadata[smiles]["predictions"]

def get_concentration(smiles):
    return metadata[smiles]["concentration"]

def has_data(smiles):
    return smiles in metadata

def get_aroma(smiles):
    return aromas[smiles]
