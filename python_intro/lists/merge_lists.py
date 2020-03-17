#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 16:14:49 2020

@author: darienpmt
"""

def linear_merge(list1, list2):
    return sorted(list1 + list2)
    
    
    
    
list1, list2 = ['aa', 'xx', 'zz'], ['bb', 'cc']
print(linear_merge(list1, list2))