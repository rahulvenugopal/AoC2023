# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 18:49:38 2023
Day 1: Trebuchet

@author: Rahul Venugopal
"""
#%% Part One
# Load the data input
# Load data which is in text format
file = open('input.txt','r')
data = file.readlines()
data = [line.rstrip() for line in data]

import re

# Get the time to charge and distance to beat as two lists
time = re.findall(r'\d+', data[0])
time_for_charging = list(map(int, time))

distance = re.findall(r'\d+', data[1])
distance_to_travel = list(map(int, distance))

# Take the first entries from both lists, run a loop and see winning combos
winning_races = 1

for time,distance in zip(time_for_charging,distance_to_travel):
    winning_combos = 0
    for runs in range(time+1):
        if runs*(time-runs) > distance:
            winning_combos += 1
            
    winning_races = winning_races * winning_combos

#%% Part Two Kerning in paper

one_time = int(''.join([str(x) for x in time_for_charging]))
one_distance = int(''.join([str(x) for x in distance_to_travel]))


winning_combos = 0
for runs in range(one_time+1):
    if runs*(one_time-runs) > one_distance:
        winning_combos += 1
