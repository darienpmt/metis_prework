#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 12:43:53 2020

@author: darienpmt
"""

def fix_start(s):
    try:
        return s[0] + ''.join(['*' if char == s[0] else char for char in s[1:]])
    except IndexError:
        return "Enter a nonempty string, jeeze!"

print(fix_start(''))
    