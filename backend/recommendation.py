import json
import random
import result_utils
import dataset
import model

def convert(predictions):
    # Quick conversion b/c original dataset didn't have "warm" as a descriptor.
    predictions["warm"] = (predictions["amber"] + predictions["musk"])/2
    return {n:predictions[n.lower()] for n in result_utils.NOTES_WHEEL}

def make_aroma(selection):
    position = result_utils.Position(random.random(),random.random())

    predictions = convert(dataset.get_predictions(selection["SMILES"]))
    notes = result_utils.Notes(*[predictions[n] for n in result_utils.NOTES_WHEEL])

    aroma = dataset.get_aroma(selection["SMILES"])

    return result_utils.RecResult(aroma["names"],aroma["CAS"],aroma["SMILES"],selection["concentration"],selection["probability"],position,notes)

def get(k,aroma_sequence,**kwargs):
    """Get the top-k recommendations for a given sequence.

    Keyword arguments:
    k -- number of desired recommendations
    sequence -- list of Aromas
    **kwargs -- user specified options
        global_tsne -- whether the 2d reduction is applied across all molecules or just the recommended set. (default: false)

    Returns:
    list -- a list of top-k recommendations as Aromas with added x,y fields.
    """
    selected = model.get_top_k(k,aroma_sequence)
    results = [make_aroma(selection) for selection in selected]
    return [res.to_dict() for res in results]
