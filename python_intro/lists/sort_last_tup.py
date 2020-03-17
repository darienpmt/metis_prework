#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 15:31:01 2020

@author: darienpmt
"""

def sort_last(tuples):
    return sorted(tuples, key=lambda tup: tup[-1])
    
    
    
    
    
tup_lst = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]
print(sort_last(tup_lst))