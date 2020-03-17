#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 12:42:07 2020

@author: darienpmt
"""

def both_ends(s):
    if len(s) < 2:
        return ''
    else:
        return s[:2] + s[-2:]

print(both_ends('x'))