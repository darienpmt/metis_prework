#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 18:48:54 2020

@author: darienpmt
"""
import csv 
from collections import defaultdict

def get_dict():
    """ Reads in 'faculty.csv' and returns a dictionary where keys are
    the professor's names, as a tuple, and values are corresponding rows. """
    
    with open('faculty.csv') as fn:
      
        faculty_dict = defaultdict(list)
        
        for row in list(csv.reader(fn))[1:]:
            faculty_dict[tuple(row[0].split())] += row[1:]
            
        return dict(faculty_dict)
    
faculty_dict =  get_dict()
print(faculty_dict)