#!/usr/bin/env python3

file = 'rosalind_rna.txt'
rna = ''
with open(file) as f:
    chars = f.read()
    chars = chars.rstrip()
    for i in chars:
        if i in ['A','C','G']:
            rna += i
        else:
            i = 'U'
            rna += i
print(rna)
