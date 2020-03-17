#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 13:51:56 2020

@author: darienpmt
"""
import csv
import re
from collections import defaultdict

def read_data(csv_file_name, col_num):
    """ Opens the desired file. Returns a column of data 
    as a list from the file. """
    
    with open(csv_file_name) as fn:
        return [titles[col_num] for titles in list(csv.reader(fn))[1:] ]

def count_titles(csv_file_name):
    """ Reads in a csv file and returns a dictionary where keys are the title
    of a professor and the values are their frequencies in the file."""
    
    # there is one typo in 'Titles' column that needs fixing
    typo_fix = re.compile(r' is ')
    
    # obtaining the data in the form of a list (thanks to the function above)
    titles = read_data(csv_file_name, 2)
    
    # fixes the known typo
    cleaned_titles = [typo_fix.sub(' of ', title) for title in titles]
    
    # building a dictionary with the titles as keys and their frequencies as values
    titles_dict = defaultdict(int)
        
    for title in cleaned_titles:
        titles_dict[title] += 1
    
    return dict(titles_dict)



title_dict = count_titles('faculty.csv')
print(title_dict)
    
