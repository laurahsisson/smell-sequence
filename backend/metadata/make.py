import crate_utils
import dataset

# TODO: Actually make the metadata
crate_smiles = crate_utils.smiles("mine")
missing = 0
for s in crate_smiles:
    if dataset.has_data(s):
        continue
    print(s)
    missing += 1

print(f"Missing {missing} smiles out of {len(crate_smiles)}. Fraction = {missing/len(crate_smiles):.2f}")



