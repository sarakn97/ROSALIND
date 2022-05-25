#!/usr/bin/env python3

with open ('rosalind_dna.txt') as file:
    chars = file.read()

counta = 0
countg = 0
countc = 0
countt = 0
for i in chars:
    if i == "A":
        counta +=1
    if i == "G":
        countg += 1
    if i == "C":
        countc += 1
    if i == "T":
        countt +=1

print(counta, countc,  countg, countt)
