#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 08:44:47 2019

@author: Brewbaker
"""

import string
from collections import Counter

# Prompt user for name of .txt file containing job description.  Open file if it exists.
fname = input('Enter name of text file containing job description: ')
try: 
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    exit()

# Define commonly used words.  These words will not be included in final keywords list.
common_words = ['a', 'an', 'and', 'the', 'for', 'with', 'this', 'to', 'in', 'of', 
                'through', 'has', 'it', 'its', 'are', 'not', 'but', 'with', 'or', 'is', 
                'from', 'you', 'our', 'by', 'all', 'at', 'can', 'within', 'as', 'will', 
                'us', 'that', 'be', 'on', 'work', 'help', 'helps', 'able']

# Create dictionary containing words and the number of times used.
counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

# Remove commonly used words
for key, value in list(counts.items()):
	if key in common_words:
		del counts[key]
		
# Only keep words that occur more than once
for key in list(counts.keys()):
	if counts[key] < 2:
		del counts[key]
    
print(Counter(counts).most_common())