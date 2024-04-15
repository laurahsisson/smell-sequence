import collections

Position = collections.namedtuple("Position","x y")

NOTES_WHEEL = ['Citrus', 'Warm', 'Sweet', 'Green', 'Fruity', 'Floral', 'Fresh', 'Spicy', 'Woody']
Radar = collections.namedtuple("Radar"," ".join(NOTES_WHEEL))

class RecResult:
    def __init__(self,names,cas,smiles,concentration,probability,position,radar,notes):
        self.names = names
        self.cas = cas
        self.smiles = smiles
        self.concentration = concentration
        self.probability = probability
        self.position = position
        self.radar = radar
        self.notes = notes

    def to_dict(self):
        return {
            'names': sorted(self.names,key=lambda x: len(x)),
            'CAS': self.cas,
            'SMILES': self.smiles,
            'concentration': self.concentration,
            'probability': self.probability,
            'position': self.position._asdict(),
            'radar': self.radar._asdict(),
            'notes': self.notes,
        }
