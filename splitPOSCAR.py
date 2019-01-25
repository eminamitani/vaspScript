# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 12:02:26 2019

@author: Emi Minamitani
In order to differential charge calculation,
making the POSCAR for molecule area and surface area.
parameter 'height' is the threshould to determine the adsorbate or substrate
"""

from ase import Atoms, Atom
import ase.io
import os
import shutil

height=6.5

atoms=ase.io.read('POSCAR', format='vasp')

mol=Atoms([a for a in atoms if a.z > height])
sub=Atoms([a for a in atoms if a.z <= height])

mol.set_cell(atoms.cell)
mol.set_pbc(atoms.pbc)

sub.set_cell(atoms.cell)
sub.set_pbc(atoms.pbc)


os.makedirs('adsorbate', exist_ok=True)
ase.io.write('adsorbate/POSCAR',mol,format='vasp', direct=True, vasp5=True)

os.makedirs('substrate', exist_ok=True)
ase.io.write('substrate/POSCAR',sub,format='vasp', direct=True, vasp5=True)

if os.path.isfile('INCAR'):
    shutil.copyfile('INCAR', './adsorbate/INCAR')
    shutil.copyfile('INCAR', './substrate/INCAR')
    
if os.path.isfile('KPOINTS'):
    shutil.copyfile('KPOINTS', './adsorbate/KPOINTS')
    shutil.copyfile('KPOINTS', './substrate/KPOINTS')