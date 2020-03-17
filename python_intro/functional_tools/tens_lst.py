#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 11:26:12 2020

@author: darienpmt
"""

xlist = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 75,100]

# Write your answer in one line, using "filter"

tens_list = list(filter(lambda x: x % 10 == 0, xlist))
print(tens_list)