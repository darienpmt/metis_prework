#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 13:00:54 2020

@author: darienpmt
"""

def mix_up(a, b):
    return b[:2] + a[2:] + ' ' + a[:2] + b[2:]

print(mix_up('pezzy', 'firm'))