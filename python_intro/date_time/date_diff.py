#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 11:29:40 2020

@author: darienpmt
"""
import sys
import os
from datetime import datetime

def difference_in_days(date1, date2):
    return (datetime.strptime(date2, '%m-%d-%y') - datetime.strptime(date1, '%m-%d-%y')).days
    

    
date1 = '01-02-13'
date2 = '01-03-13'

print(date1)
print(date2)

diff = difference_in_days(date1, date2)

print(diff)