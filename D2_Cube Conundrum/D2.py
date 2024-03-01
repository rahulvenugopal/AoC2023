# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 20:48:37 2023
Cube Conundrum

@author: Rahul Venugopal
"""
#%% Part One
# Load the data input
# Load data which is in text format
file = open('input.txt','r')
data = file.readlines()
data = [line.rstrip() for line in data]

# Idea is to iterate through each line
# For each line,create a list for each draws
# calculate maximum of red, blue and greens
# Use a condition to check and add the iter number

draw_wise = []

for iter_no, lines in enumerate(data):
    line_by_line = lines.split(':')[1].split(';')
    draw_wise.append(','.join(line_by_line))

import pandas as pd
import numpy as np

list_of_lists = []
for iter_no, items in draw_wise:
    one_entry = (items.split(','))
    dfs = pd.DataFrame(entries.split(' ') for entries in one_entry)
    dfs.drop([0], axis = 1, inplace=True)

    dfs[1] = pd.to_numeric(dfs[1])

    dfs = dfs.sort_values(by = [2,1], ascending=[False,False], ignore_index=True)

    indices = np.unique(dfs[2], return_index=True)[1]
    for iter in range(len(indices)):
        if dfs[1][indices[iter]] <
    list_of_lists.append(dfs)



