import json
import os

def get(crate_fname):
    with open(os.path.join("crates",f"{crate_fname}.json")) as f:
        return json.load(f)


def list_all():
    files = os.listdir("crates")
    crate_names = [os.path.splitext(f)[0] for f in files if os.path.splitext(f)[1] == ".json"]
    results = []
    for crate_fname in crate_names:
        crd = get(crate_fname)
        results.append({"name":crate_fname,"description":crd["description"],"size":len(crd["data"])})
    return results