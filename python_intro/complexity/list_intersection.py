#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 17:00:20 2020

@author: darienpmt
"""

from datetime import datetime

def intersect_lists_1(list1, list2):
    return [i for i in list1 if i in list2]


def intersect_lists_2(list1, list2):
    return list(set(list1) & set(list2))


import random

def measure_time(f, *args):
    then = datetime.now()
    res = f(*args)
    now = datetime.now()
    return res, now-then

list1 = random.sample(range(10**6), 10000)
list2 = random.sample(range(10**6), 10000)
ans1, time1 = measure_time(intersect_lists_1, list1, list2)
ans2, time2 = measure_time(intersect_lists_2, list1, list2)
print(time1, time2)
assert time2 < time1 / 100, 'the function can be faster'
assert set(ans1) == set(ans2), 'the function does not work correctly'
print(1)

#print(intersect_lists_2(list1, list2))
