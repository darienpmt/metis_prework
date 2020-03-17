#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 15:17:09 2020

@author: darienpmt
"""
new_alpha = 'xabcdefghijklmnopqrstuvwyz'

def front_x(words):
    return sorted(words, key=lambda word: [new_alpha.index(c) for c in word])

lst = ["mix", "xyz", "apple", "xanadu", "aardvark"]

print(front_x(lst))