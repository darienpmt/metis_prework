#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 10:44:24 2020

@author: darienpmt
"""

import csv
import re
from collections import defaultdict

def read_data(csv_file_name, col_num):
    """ Opens the desired file. Returns a column of data 
    as a list from the file. """
    
    # reads each line of the file into single list; splits the strings in each sublist 
    # is there a better of doing this besides nested for loop?
    
    with open(csv_file_name) as fn:
        return [col for lines in list(csv.reader(fn))[1:] for col in lines[col_num].split()]

def count_degrees(csv_file_name):
    """ Reads in a file and returns a dictionary where keys are degrees
    and values are their corresponding frequencies in the file. """
    
    # obtaining the data set
    data = read_data(csv_file_name, 1)
    
    # replace the strings matching the corresponding regex expression with a
    # "standardized" string
    for i, degree in enumerate(data):
        if re.match(r'Ph\.*D.*', degree):
            data[i] = re.compile(r'Ph\.*D.*').sub('Ph.D', degree)
        elif re.match(r'Sc\.*D.*', degree):
            data[i] = re.compile(r'Sc\.*D.*').sub('Sc.D', degree)
        elif re.match(r'M\.*S.*', degree):
            data[i] = re.compile(r'M\.*S.*').sub('MS', degree)
        
    # creating a dictionary to store degrees as vals and freq as keys
    degree_dict = defaultdict(int)
        
    for degree in data:
        degree_dict[degree] += 1
            
    return dict(degree_dict)



phd_count = count_degrees('faculty.csv')
print(phd_count)