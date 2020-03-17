#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 14:36:18 2020

@author: darienpmt
"""
import csv

def read_data(csv_file_name, col_num):
    """ Opens the desired file. Returns a column of data 
    as a list from the file. """
    
    with open(csv_file_name) as fn:
        return [titles[col_num] for titles in list(csv.reader(fn))[1:] ]

def emails(csv_file_name):
    """ Reads in a csv file then returns a list of emails in the file. """
    
    return read_data(csv_file_name, 3)

print(emails('faculty.csv'))