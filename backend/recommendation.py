import json
import random
import result_utils

with open("data/molecules.json") as f:
    molecules = json.load(f)

molecules = [m for m in molecules if m["SMILES"] and m["CAS"]]

def make(aroma):
    position = result_utils.Position(random.random(),random.random())
    notes = result_utils.Notes(*[random.random() for _ in result_utils.NOTES_WHEEL])
    concentration = random.random()
    return result_utils.RecResult(aroma["names"],aroma["CAS"],aroma["SMILES"],concentration,position,notes)

def get(sequence,k,**kwargs):
    """Get the top-k recommendations for a given sequence.

    Keyword arguments:
    sequence -- list of Aromas
    k -- number of desired recommendations
    **kwargs -- user specified options
        global_tsne -- whether the 2d reduction is applied across all molecules or just the recommended set. (default: false)

    Returns:
    list -- a list of top-k recommendations as Aromas with added x,y fields.
    """
    selected = random.sample(molecules,k)
    results = [make(aroma) for aroma in selected]
    return [res.to_dict() for res in results]
