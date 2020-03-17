#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 15:38:03 2020

@author: darienpmt
"""

def remove_adjacent(nums):
    
   
    new_nums = []
    
    if not nums:
        return new_nums
    
    for i in range(len(nums + ['.']) - 1):
        if nums[i] != nums[i+1]:
            new_nums.append(nums[i])
    
    return new_nums + [nums[-1]]

def remove_adjacent2(nums):
    
    if not nums:
        return []
    
    try: 
        return [nums[i] for i in range(len(nums + ['.']) - 1) if nums[i] != nums[i+1]]
    except IndexError:
        print('yeat')
        
    




lst = [1, 1, 77, 2, 2, 3, 3, 3, 3, 4, 5]
print(remove_adjacent(lst))
print('')
#print(remove_adjacent2(lst))