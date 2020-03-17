#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 11:07:00 2020

@author: darienpmt
"""


lst = [3, 4, 7, 2, 9, 170]


f = lambda my_list: [num for num in my_list if num % 2 == 0]
    
print(f(lst))