#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 13:16:58 2020
@author: darienpmt
"""

def not_bad(s):
    last_char = ''
    
    if s[-1].isalpha():
        last_char = ''
        s = s
    else:
        last_char = s[-1]
        s = s[:-1]
    
    word_list = s.split()
    
    try:
        not_pos = word_list.index('not')
        bad_pos = word_list.index('bad')
    except ValueError:
        return s + last_char
    
    if not_pos > bad_pos:
        return s
    else:
        word_list = word_list[:not_pos] + ['good'] + word_list[bad_pos + 1:]
        print(word_list)
        return (' '.join(word_list) + last_char).rstrip()

string = "This dinner is not bad in fact it is the bomb!"

print(not_bad(string))