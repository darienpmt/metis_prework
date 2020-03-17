#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 17:22:31 2020

@author: darienpmt
"""
import csv

def read_data(csv_file_name, col_num):
    """ Opens the desired file. Returns a column of data 
    as a list from the file. """
    
    with open(csv_file_name) as fn:
        return [titles[col_num] for titles in list(csv.reader(fn))[1:] ]

def emails(csv_file_name):
    """ Reads in a csv file then returns a list of emails in the file. """
    
    return read_data(csv_file_name, 3)

def unique_domains(emails):
    """ Given a list of emails, returns the unique domain names 
    for each email."""
    
    # splits each email string on the 'at sign' and gives a set of domains
    # because we only need the unique domain emails
    return set([email.split('@')[1] for email in emails])

email_list = emails('faculty.csv')
domains = unique_domains(email_list)
print(domains)