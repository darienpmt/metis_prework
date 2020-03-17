#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 11:56:27 2020

@author: darienpmt
"""
import csv
import re
from collections import defaultdict

def read_data(csv_file_name, col_num):
    """ Opens the desired file. Returns a column of data 
    as a list from the file. """
    
    with open(csv_file_name) as fn:
        return [col for lines in list(csv.reader(fn))[1:] for col in lines[col_num].split()]

def count_degrees(csv_file_name):
    """ Reads in a file and returns a dictionary where keys are degrees
    and values are their corresponding frequencies in the file. """
    
    # the degree types which need cleaning
    phd = re.compile(r'Ph\.*D.*')
    scd = re.compile(r'Sc\.*D.*')
    ms = re.compile(r'M\.*S.*')
    
    # obtaining the data set
    data = read_data(csv_file_name, 1)

    # replace the strings matching the corresponding regex expression with
    # "cleaned" string
    
    # does having these as generators really "help?"
    clean_phd = (phd.sub('Ph.D', degree) for degree in data)
    clean_scd = (scd.sub('Sc.D', degree) for degree in clean_phd)
    clean_ms = (ms.sub('MS', degree) for degree in clean_scd)
        
    # creating a dictionary to store degrees as vals and freq as keys
    degree_dict = defaultdict(int)
        
    for degree in clean_ms:
        degree_dict[degree] += 1
            
    return dict(degree_dict)



phd_count = count_degrees('faculty.csv')
print(phd_count)


