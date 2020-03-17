#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 13:04:50 2020

@author: darienpmt
"""

def verbing(s):
    if len(s) < 3:
        return s
    else:
        if s[-3:] == 'ing':
            return s + 'ly'
        else:
            return s +'ing'

print(verbing('ing'))