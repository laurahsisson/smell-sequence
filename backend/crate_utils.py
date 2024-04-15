import json
import os

import dataset

def get(crate_fname):
    with open(os.path.join("crates",f"{crate_fname}.json")) as f:
        crate = json.load(f)

    crate["data"] = [mol for mol in crate["data"] if dataset.has_data(mol["SMILES"])]
    for mol in crate["data"]:
        mol["notes"] = dataset.get_notes(mol["SMILES"])
        mol["concentration"] = dataset.get_concentration(mol["SMILES"])

    crate["name"] = crate_fname
    return crate

def smiles(crate_fname):
    return [mol["SMILES"] for mol in get(crate_fname)["data"]]

def get_aroma(crate_fname,smiles):
    for mol in get(crate_fname)["data"]:
        if mol["SMILES"] != smiles:
            continue
        return {"names":[mol["name"]],"CAS":mol["CAS"],"SMILES":mol["SMILES"]}

    raise KeyError(f"Failed to find SMILES={smiles} in crate={crate_fname}")

def list_all():
    files = os.listdir("crates")
    crate_names = [os.path.splitext(f)[0] for f in files if os.path.splitext(f)[1] == ".json"]
    results = []
    for crate_fname in crate_names:
        crd = get(crate_fname)
        results.append({"name":crate_fname,"description":crd["description"],"size":len(crd["data"])})
    return results