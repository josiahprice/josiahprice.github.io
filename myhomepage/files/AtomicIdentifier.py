# -*- coding: utf-8 -*-
#day 5 assignment
#Paul and Josiah

def atomic_finder(n):
    atomSymbol=['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O','F','Ne', 
               'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca',
               'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn',
               'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr',
               'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn',
               'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd',
               'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb',
               'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 
               'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn']
    atomMass=[1, 4, 6, 9, 10, 12, 14,15, 18, 20, 
              22, 24, 26, 28, 30, 32, 35, 39, 39, 40,
              44, 47, 50, 51, 54, 55, 58, 58, 63, 65,
              69, 72, 74, 78, 79, 84, 84, 87, 88, 91, 
              92, 95, 98, 101, 102, 106, 107, 112, 114, 118, 
              121, 127, 126, 131, 132, 137, 138, 140, 140, 144, 
              144, 150, 151, 157, 158, 162, 164, 167, 168, 173, 
              174, 178, 180, 183, 186, 190, 192, 195, 196, 200, 
              204, 207, 208, 208, 209, 222]
    atomName=['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Flourine', 'Neon',
              'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorous', 'Sulfur', 'Chlorine', 'Argon', 'Potassium', 'Calcium',
              'Scandium', 'Titanium', 'Vanadium', 'Chromium', 'Manganese', 'Iron', 'Cobalt', 'Nickel', 'Copper', 'Zinc',
              'Gallium', 'Germanium', 'Arsenic', 'Selenium', 'Bromine', 'Krypton', 'Rubidium', 'Strontium', 'Yttrium', 'Zirconium',
              'Niobium', 'Molybdenum', 'Technetium', 'Ruthinium', 'Rhodium', 'Palladium', 'Silver', 'Cadmium', 'Indium', 'Tin',
              'Antimony', 'Tellurium', 'Iodine', 'Xenon', 'Cesium', 'Barium', 'Lanthanum', 'Cerium', 'Praseodymium', 'Neodymium',
              'Promethium', 'Samarum', 'Europium', 'Gadolinium', 'Turbium', 'Dysprosium', 'Holmium', 'Erbium', 'Thulium', 'Ytterbium',
              'Lutetium', 'Hafnium', 'Tantalum', 'Tungsten', 'Rhenium', 'Osmium', 'Iridium', 'Platinum', 'Gold', 'Mercury',
              'Thallium', 'Lead', 'Bismuth', 'Polonium', 'Astatine', 'Radon']
    print "Name:", atomName[n-1]
    print "Atomic Symbol:", atomSymbol[n-1]
    print "Atomic Mass:", atomMass[n-1]
              
answer= input('Enter the atomic number for any element from 1-86: ')
atomic_finder(answer)
    