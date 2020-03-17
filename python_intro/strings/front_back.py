#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 14:31:02 2020

@author: darienpmt
"""

def front_back(s1, s2):
    
    def check_len(string):
        if len(string) % 2 == 0:
            return if_even(string)
        else:
            return if_odd(string)
    
    def if_odd(string):
        return string[: len(string)//2 + 1], string[len(string)//2 + 1:]
    
    def if_even(string):
        return string[: len(string)//2 ], string[len(string)//2:]
    
    return check_len(s1)[0] + check_len(s2)[0] + check_len(s1)[1] + check_len(s2)[1]
    
 
    
s1, s2 = 'Kitten', 'Donut'
print(front_back(s1, s2))