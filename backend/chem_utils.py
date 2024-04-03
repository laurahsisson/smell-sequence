import re
import collections
import tqdm

Source = collections.namedtuple("Source","source url")

class Aromachemical:
    def __init__(self,names,cas="",smiles="",sources=[],concentration=0):
        self.names = list(set([split_name_percentage(n).name for n in names if n]))
        self.cas = cas if cas else ""
        self.smiles = smiles if smiles else ""
        self.sources = sources
        self.concentration = concentration
        
    def get_smiles(self):
        return self.smiles
    
    def is_match(self,name):
        return name in self.names
    
    def __str__(self):
        return f"Aromachemical(names: {self.names}, CAS: '{self.cas}', SMILES: '{self.smiles}', sources: {self.sources}, concentration: {self.concentration})"
    
    def __repr__(self):
        return str(self)
    
    def __iter__(self):
        yield "names", self.names
        yield "CAS", self.cas
        yield "SMILES", self.smiles
        yield "sources", [{"source":s.source,"url":s.url} for s in self.sources]
        if self.concentration:
            yield "concentration", self.concentration
    
    def same_aromachemical(self,other):
        names_match = len(set(self.names).intersection(set(other.names))) > 0
        cas_match = self.cas == other.cas if self.cas and other.cas else False
        return names_match or cas_match
    
    def merge(self,other):
        names = list(set(self.names).union(set(other.names)))
        cas = self.cas if self.cas else other.cas
        smiles = self.smiles if self.smiles else other.smiles
        sources = self.sources + other.sources
        concentration = self.concentration + other.concentration
        return Aromachemical(names,cas,smiles,sources,concentration)
    
def merge_dataset(all_unique_data,disable_tqdm=False):
    has_merged = True
    while has_merged:
        has_merged = False
        found_match = set()
        next_all_unique_data = []
        for i,d1 in enumerate(tqdm.tqdm(all_unique_data,disable=disable_tqdm)):
            if i in found_match:
                continue

            for j, d2 in enumerate(all_unique_data):
                if j <= i:
                    continue

                if d1.same_aromachemical(d2):
                    has_merged = True
                    found_match.add(i)
                    found_match.add(j)
                    d1 = d1.merge(d2)

            next_all_unique_data.append(d1)

        all_unique_data = next_all_unique_data
    return all_unique_data

Ingredient = collections.namedtuple("Ingredient","name concentration")

def split_name_percentage(raw_name):
    raw_name = raw_name.replace("®","")
    match = re.match(r"(.+?)(?:\(.*\))?\s?\(?@?((?:\.?\d)+)%|(.+?)(?:\(.*\))?$", raw_name)
    
    if not match:
        print(raw_name.encode())
    name = match.group(1).strip().lower() if match.group(1) else match.group(3).strip().lower()
    concentration = float(match.group(2)) / 100 if match.group(2) else 100
    return Ingredient(name, concentration)

def is_parsed(raw_name):
    parsed = split_name_percentage(raw_name)
    return parsed.name == raw_name

def test():
    inputs = ["alpha-isomethyl ionone (50% min.)","Hedione (firmenich)","ambrofix (givaudan) @10%","allyl amyl glycolate 0.1% DPG","aldehyde c-9 1%","iso e super",'ethyl maltol 0.1%',"allyl amyl glycolate 0.1% dpg","fleuranil 10% dpg","allyl amyl glycolate 0.1% dpg"]
    for input_str in inputs:
        name, concentration = split_name_percentage(input_str)
        print(f"Raw: {input_str} - Name: {name}, Concentration: {concentration}")
    print(is_parsed("hedione"))
    