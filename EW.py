#EW
from pymatgen.core import *
from pymatgen.io.vasp.sets import *
from pymatgen.core.structure import Lattice, Structure, Molecule
from pymatgen.io.vasp.sets import MPRelaxSet
from pymatgen.core.periodic_table import Element, DummySpecies, get_el_sp

from pymatgen.ext.matproj import MPRester, Composition, Element
from pymatgen.io.vasp import Vasprun
from pymatgen.analysis.phase_diagram import CompoundPhaseDiagram, GrandPotentialPhaseDiagram, PDPlotter, PhaseDiagram

from pymatgen.entries.computed_entries import ComputedEntry
from pymatgen.entries.compatibility import MaterialsProjectCompatibility
import json
import re
import palettable
import matplotlib as mpl

def get_most_stable_entry(formula,all_entries):
    relevant_entries = [entry for entry in all_entries if entry.composition.reduced_formula == Composition(formula).reduced_formula]
    relevant_entries = sorted(relevant_entries, key=lambda e: e.energy_per_atom)
    return relevant_entries[0]
def get_comp_entries(formula,all_entries):
    relevant_entries = [entry for entry in all_entries if entry.composition.reduced_formula == Composition(formula).reduced_formula]
    return relevant_entries
def find_entry_index(formula,all_entries):
    entry_index = [all_entries.index(entry) for entry in all_entries if entry.composition.reduced_formula == Composition(formula).reduced_formula]
    return entry_index

rester = MPRester('Your own API key') #Generate your own key from Materials Projects.
mp_entries = rester.get_entries_in_chemsys(["Ge", "Li", "Ca","O"])

pd = PhaseDiagram(mp_entries)
plotter = PDPlotter(pd)

li_entries = [e for e in mp_entries if e.composition.reduced_formula == "Li"]
uli0 = min(li_entries, key=lambda e: e.energy_per_atom).energy_per_atom

el_profile = pd.get_element_profile(Element("Li"), Composition("Li2CaGeO4"))
for i, d in enumerate(el_profile):
    voltage = -(d["chempot"] - uli0)
    print("Voltage: %s V" % voltage,file=f)
    print(d["reaction"],file=f)
    print("")