# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 14:20:58 2022

@author: bauerber
"""

import pandas as pd
from unidecode import unidecode # To convert the Greek characters into Latin
from textwrap import TextWrapper

# The number of manuscripts
number_of_manuscripts = int(input('How many manuscripts do you have? '))

# Get a list of all the ms abbreviations 
ms_list = []
for manuscript in range(number_of_manuscripts):
    ms = input('Please input the abbreviation of manuscript ' + str(manuscript) + ': ')
    ms_list.append(ms)

# Establish a dictionary containing "Abbreviation of the manuscript" and a dataframe for each manuscript
d = {}
for ms in ms_list:
    inputfile = ms + '.csv'
    d[ms] = pd.read_csv(inputfile)
    d[ms]['Gloss'] = d[ms]['Gloss'].replace({'á': 'a','é': 'e','í': 'i','ó': 'o','ú': 'u', r'[^\w\s]+': '', ' ': ''}, regex=True) #maybe include ' ': 'w'
    d[ms]['Gloss'] =  d[ms]['Gloss'].apply(unidecode)
    d[ms] = d[ms].sort_values('ID')

# Establishing and printing the output in the FASTA format
for key in d:
    ms = key
    text = d[key]['Gloss'].tolist()
    # text = 'w'.join([str(a) for a in text]) # glosses are divided by 'W' because it does not occur otherwise
    tw = TextWrapper()
    tw.width = 80
    text = ('\n'.join(tw.wrap(text)))
    print('>' + ms + '\n' + text)

print('\n', 'Please copy and paste this text into the text into the correspoding field on the website (https://www.genome.jp/tools-bin/clustalw): ')
print('\n', '********************************************************************'
      '\n', 'Use the following settings:', '\n'
      'K-tuple 1, Window size 10, Gap 3', '\n', 
      'Diagonals 5, Scoring ABSOLUTE', '\n',
      'Gap Open 1, Gap Extension 0.05', '\n',
      'Gap Open 1, Gap Extension 0.05', '\n'
      'Weight and Hydrophilic NO')