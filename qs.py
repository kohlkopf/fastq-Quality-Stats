#!/usr/bin/env python3.6

import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import argparse

def get_arguments():
    parser = argparse.ArgumentParser(prog='qscore_plot', description= 'Outputs a distribution of quality scores as a function of the base position of sequencing reads.')

    parser.add_argument('-f', '--infile', help='fastq filepath', required=True, type=argparse.FileType('rt', encoding='UTF-8 '))

    return parser.parse_args()

def convert_phred(letter):
    score = ord(letter) - 33    # phred + 33
    return score

def get_lines(nthLine):
    qualityLinesList = []
    with open (file) as fh:
        NR = 0
        for line in fh:
            line = line.strip("\n")
            NR += 1
            if NR % 4 == nthLine:  #every 4th line starting at 0
                qualityLinesList.append(line)
    return qualityLinesList

def convert_phred(letter):
    return (ord(letter)-33)

args = get_arguments()
file = args.infile.name

lines = get_lines(0)
c = 0
i = 0

scores = np.zeros((101, len(lines)), dtype = float)

for c in range(101):
    i = 0
    for line in lines:
        scores[c][i] = convert_phred(line[c])  #convert cth char on quality line and add to qualityList
        i+=1
    c+=1

for pos in range(101):
    means = scores[pos].mean()

print("BP Position", "\t", "Mean Score", "\t", "Variance", "\t", "StDev", "\t", "Median")
for pos in range(101):
    print(pos, "\t", scores[pos].mean(), "\t", scores[pos].var(), "\t", scores[pos].std(), "\t", np.median(scores[pos]))
