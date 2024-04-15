import json
import random

import result_utils
import dataset
import model
import position_utils
import crate_utils

import numpy as np

def convert(predictions):
    # Quick conversion b/c original dataset didn't have "warm" as a descriptor.
    predictions["warm"] = np.mean([predictions["amber"], predictions["musk"]]).item()
    return {n:predictions[n.lower()] for n in result_utils.NOTES_WHEEL}

def make_aroma(selection,position):
    predictions = convert(dataset.get_predictions(selection["SMILES"]))
    radar = result_utils.Radar(*[predictions[n] for n in result_utils.NOTES_WHEEL])
    notes = dataset.get_notes(selection["SMILES"])

    if selection["crate"]:
        aroma = crate_utils.get_aroma(selection["crate"],selection["SMILES"])
    else:
        aroma = dataset.get_aroma(selection["SMILES"])
    
    return result_utils.RecResult(aroma["names"],aroma["CAS"],aroma["SMILES"],selection["concentration"],selection["probability"],position,radar,notes)

def make_positions(selected,options):
    if options.get("global_tsne",True):
        embeds = [position_utils.transform(selection["SMILES"]) for selection in selected]
    else:
        embeds = position_utils.subspace_transform([selection["SMILES"] for selection in selected])
    return [result_utils.Position(*embed) for embed in embeds]


def get(aroma_sequence,crate_fnames,options):
    """Get the top-k recommendations for a given sequence.

    Keyword arguments:
    sequence -- list of Aromas
    crate_fnames -- list of Crate names
    options -- user specified options
        k -- number of desired recommendations
        global_tsne -- whether the 2d reduction is applied across all molecules or just the recommended set. (default: false)

    Returns:
    list -- a list of top-k recommendations as Aromas with added x,y fields.
    """
    k = options.get("k",3)
    selected, concentration = model.get_top_k(k,aroma_sequence,crate_fnames)
    positions = make_positions(selected,options)
    results = [make_aroma(selection,pos) for (selection,pos) in zip(selected,positions)]
    return {"options":[res.to_dict() for res in results],"dosage":concentration}
