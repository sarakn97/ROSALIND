#!/usr/bin/env python3

file = 'rosalind_revc.txt'

# define function to return complement DNA strand for string input
def complement(seq):
    comp = ""
    for i in seq:
        if i == "A":
            comp += "T"
        if i == "T":
            comp += "A"
        if i == "C":
            comp += "G"
        if i == "G":
            comp += "C"
    return comp 

# Retrn reverse complement for sequence input
with open(file) as f:
    str = f.read()
    str = str.rstrip()
    comp = complement(str) 
    print(comp[::-1])

