import collections

Position = collections.namedtuple("Position","x y")

NOTES_WHEEL = ['Citrus', 'Warm', 'Sweet', 'Green', 'Fruity', 'Floral', 'Fresh', 'Spicy', 'Woody']
Notes = collections.namedtuple("Notes"," ".join(NOTES_WHEEL))


class RecResult:
    def __init__(self,names,cas,smiles,concentration,position,notes):
        self.names = names
        self.cas = cas
        self.smiles = smiles
        self.concentration = concentration
        self.position = position
        self.notes = notes

    def to_dict(self):
        return {
            'names': self.names,
            'cas': self.cas,
            'smiles': self.smiles,
            'concentration': self.concentration,
            'position': self.position._asdict(),
            'notes': self.notes._asdict()
        }
