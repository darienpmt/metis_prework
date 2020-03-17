#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 14:22:02 2020

@author: darienpmt
"""

def not_bad(s):
    
    not_pos = s.find('not')
    bad_pos = s.find('bad')
    print(not_pos)
    print(not_bad)
    if not_pos >= bad_pos:
        return s
    else:
        return s[:not_pos] + 'good' + s[bad_pos + 3:]
    
    
    

string = "The tea is good!"

print(not_bad(string))