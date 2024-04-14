import json
import os

def get(crate_fname):
    with open(os.path.join("crates",f"{crate_fname}.json")) as f:
        data = json.load(f)

    data["name"] = crate_fname
    return data

def smiles(crate_fname):
    return [mol["SMILES"] for mol in get(crate_fname)["data"]]

def get_aroma(crate_fname,smiles):
    data = get(crate_fname)
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