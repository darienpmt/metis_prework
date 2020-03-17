#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 18:08:17 2020

@author: darienpmt
"""
import csv
from collections import defaultdict


def get_dict():
    """ Reads in 'faculty.csv' and returns a dictionary where keys are
    the professor's last names and values are corresponding rows. """
    
    with open('faculty.csv') as fn:
        
        # building a dictionary where keys are prof's last name and
        # values are corresponding rows
        faculty_dict = defaultdict(list)
        
        
        for row in list(csv.reader(fn))[1:]:
            # split the first element of each row since we only want the last
            # of each professor
            faculty_dict[row[0].split()[-1]] += [row[1:]]

        
        return dict(faculty_dict)
        
        
faculty_dict =  get_dict()
print(faculty_dict)