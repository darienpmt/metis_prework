#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 12:36:18 2020

@author: darienpmt
"""

def donuts(count):
    if count < 0:
        return "Invalid number of donuts."
    if count < 10:
        return "Number of donuts: " + str(count)
    else:
        return "Number of donuts: many" 


print(donuts(-1))