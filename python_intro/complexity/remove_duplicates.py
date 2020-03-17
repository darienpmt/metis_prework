#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 17:08:07 2020

@author: darienpmt
"""
from datetime import datetime, timedelta
import random
from collections import OrderedDict

def remove_duplicates(somelist):
    """Given a non-sorted list with duplicate elements, return the unique
    elements in that list in a {data structure}."""
    return set(somelist)

somelist = [random.randint(0, 10000) for i in range(1000)]
then = datetime.now()
ans = remove_duplicates(somelist)
now = datetime.now()
assert (now-then) < timedelta(0, 0, 100), 'the function can be faster'
assert not len(ans) - len(set(ans)), 'there are dupes in your answer'
assert all(i in somelist for i in ans)

print(1)