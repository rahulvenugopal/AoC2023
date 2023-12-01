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


# We have to find the first number and last number of each line

# I am thinking to run a regex to remove all non numbers from each line via loop
# Then pick the first and last and convert it from str to number

# import regex library
import re

# Throw away all non numbers
data = [re.sub("[^0-9]", "", line) for line in data]

# We take the first entry and last entry (if only one number last entry is also first entry and that's what we want)

data = sum([int(line[0]+ line[-1]) for line in data])

#%% Part Two

# Replacing one, two, three etc with numbers

# Throw away all non numbers
# Realised that we have to take care of overlaps as well

data = [re.sub("oneight", "18", line) for line in data]
data = [re.sub("twone", "21", line) for line in data]
data = [re.sub("threeight", "38", line) for line in data]
data = [re.sub("fiveight", "58", line) for line in data]
data = [re.sub("sevenine", "79", line) for line in data]
data = [re.sub("eightwo", "82", line) for line in data]
data = [re.sub("eighthree", "83", line) for line in data]
data = [re.sub("nineight", "98", line) for line in data]

data = [re.sub("one", "1", line) for line in data]
data = [re.sub("two", "2", line) for line in data]
data = [re.sub("three", "3", line) for line in data]
data = [re.sub("four", "4", line) for line in data]
data = [re.sub("five", "5", line) for line in data]
data = [re.sub("six", "6", line) for line in data]
data = [re.sub("seven", "7", line) for line in data]
data = [re.sub("eight", "8", line) for line in data]
data = [re.sub("nine", "9", line) for line in data]

# Throw away all non numbers
data = [re.sub("[^0-9]", "", line) for line in data]

# We take the first entry and last entry (if only one number last entry is also first entry and that's what we want)

data = sum([int(line[0]+ line[-1]) for line in data])

