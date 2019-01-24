# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 17:49:22 2019

@author: Emi Minamitani
This script reading POSCAR and gather the required POTCAR from specific directory.
You need to set path which contains the VASP PAW potentials.
Here I assume the directory tree as
pot
|---H/
    |---POTCAR
    |---PSCTR
|---C/
    |---POTCAR
    |---PSCTR
...
"""

from ase import Atoms
import ase.io


#set the appropreate path for your environment
path='./pot'

atoms=ase.io.read('POSCAR', format='vasp')
symbols=[a.symbol for a in atoms]

#extract the element symbols
s_uniq=list(dict.fromkeys(symbols))

with open('POTCAR', 'w') as p:
    for symbol in s_uniq:
        file=path+"/"+symbol+'/POTCAR'
        with open(file,'r') as f:
            potinfo=f.readlines()
        
        for str in potinfo:
            p.write(str)
            
        

