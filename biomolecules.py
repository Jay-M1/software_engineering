"""from abc import ABC, abstractmethod

class Molecule(ABC):
    def __init__(self, sequence):
        self._sequence = sequence

    #@abstractmethod
    #def build(self):
        #Define a structure for building the biomolecule
        #raise NotImplementedError()



class Biomolecule(Molecule):
    def __init__(self, sequence):
        super().__init__(sequence)



class Complex(Biomolecule):

    def __init__(self, DNA, Protein):
        self.constituents = {DNA():Protein()}


class Protein(Biomolecule):

    atom_list = ['N','O','C']

    def __init__(self, sequence):
        self.backbone = Backbone()
        self.sidechain = Sidechain(sequence)

    def build(self):
        pass



class DNA(Biomolecule):

    def __init__(self, sequence):
        super().__init__(sequence)
        self.backbone = Backbone()
        self.sidechain = Sidechain(sequence)
        

    def build(self):
        pass



class AminoAcid(Biomolecule):
    pass


class BasePair(Biomolecule):
    pass

class Backbone(Molecule):
    def __init__(self):
        self.backbone = {'width': 3, 'breadth':1, 'color':'#FFC0CB'} # pink

class Sidechain(Molecule):
    def __init__(self, sequence, color1, color2=None):
        super().__init__(sequence)
        if color2 is None:
            self.sidechains = {'width': 1, 'breadth':1, 'colors':[color1]}
        else:
            self.sidechains = {'width': 1, 'breadth':1, 'colors':[color1, color2]}
"""

import json
import matplotlib.pyplot as plt # type: ignore
from matplotlib import colors as col # type: ignore

class Molecule():
        pass

class Biomolecule(Molecule):
    pass

class Complex(Biomolecule):
    def __init__(self, base_pair_seq, amino_acid_seq) -> None:
        super().__init__()

        base_pairs = []
        for color in base_pair_seq:
            base_pairs.append(BasePair(color))

        amino_acids = []
        for dublett in amino_acid_seq.split():
            amino_acids.append(AmonoAcid(dublett))

        self.structure = {DNA(base_pairs), Protein(amino_acids)}

    def build(self):
        pass 

class Protein(Biomolecule):
    def __init__(self, amino_acids) -> None:
        super().__init__()
        self.amino_acids = amino_acids

class DNA(Biomolecule):
    def __init__(self, base_pairs) -> None:
        super().__init__()
        self.base_pairs = base_pairs

class BasePair(Biomolecule):
    def __init__(self, color) -> None:
        super().__init__()
        self.backbone = Backbone('purple')
        self.sidechain = Sidechain(color[0])

class AmonoAcid(Molecule):
    
    def __init__(self, colors) -> None:
        super().__init__()
        self.backbone = Backbone('pink')
        self.sidechain1 = Sidechain(colors[0])
        self.sidechain2 = Sidechain(colors[1])

class Backbone(Molecule):
    
    def __init__(self, color) -> None:
        super().__init__()
        self.color = color

class Sidechain(Molecule):

    def __init__(self, color) -> None:
        super().__init__()
        self.color = color

def main():

    with open("data.json", "r") as file:
        data = json.load(file)

    seq1 = data['sequences'][0]['text_value']
    seq2 = data['sequences'][1]['text_value']

    complex1 = Complex(seq1,seq2)

    grid_colors = [[0.1,0.2,0.3],[0.4,0.5,0.6]]
    plt.imshow(grid_colors)
    plt.xticks([]) 
    plt.yticks([])  

if __name__ == "__main__":
    main()
