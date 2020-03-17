#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 12:31:41 2020

@author: darienpmt
"""

celsius = [39.2, 36.5, 37.3, 0, 20]
# write your answer in one line. use a list comprehension. use the variable "celsius"
fahrenheit = [(c * 9 / 5) + 32 for c in celsius]

print(fahrenheit)
