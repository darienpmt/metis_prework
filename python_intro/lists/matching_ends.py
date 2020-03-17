#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 15:09:17 2020

@author: darienpmt
"""

                
def match_ends(s):
    return sum([1 for string in s if len(string) > 1 and string[0] == string[-1]])
    
    

    
lst = ['aba', 'xyz', 'aa', 'bbb', 'poop']
print(match_ends(lst))
