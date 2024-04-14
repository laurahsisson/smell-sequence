import dataset

import sklearn
import sklearn.manifold
import sklearn.decomposition
import numpy as np

print("Loading embedding space")

embeddings = np.stack([dataset.get_embed(smiles) for smiles in dataset.entire_smiles_crate()])
# TSNE has no transform function after being trained, so all embeddings must be calculated
# at startup time.
positions = sklearn.manifold.TSNE(n_components=2,perplexity=50).fit_transform(embeddings)
normalized = (positions - positions.min(axis=0)) / (positions.max(axis=0) - positions.min(axis=0))
smiles_to_position = {smiles:normalized[i].tolist() for (i,smiles) in enumerate(dataset.entire_smiles_crate())}

def transform(smiles):
   return smiles_to_position[smiles]