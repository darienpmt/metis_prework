#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 17:39:24 2020

@author: darienpmt
"""

import csv

def read_data(csv_file_name, col_num):
    """ Opens the desired file. Returns a column of data 
    as a list from the file. """
    
    with open(csv_file_name) as fn:
        return [titles[col_num] for titles in list(csv.reader(fn))[1:] ]

def emails(csv_file_name):
    return read_data(csv_file_name, 3)


def write_to_csv(list_of_emails):
    """ Given a list of emails, writes the emails to a file called
    emails.csv. """
    # naming the file we will write the data into
    with open("emails.csv", 'w') as email_file:
        
        email_f = csv.writer(email_file)
        
        # obtain a list of lists to make writing to each cell easier
        email_as_lists = [[email] for email in list_of_emails]
        
        # sets title of the column of emails
        email_f.writerow(['Faculty emails:'])
        # writes each email into a cell (row)
        email_f.writerows(email_as_lists)
        
    return None
    
    
    
    
email_list = emails('faculty.csv')
print(write_to_csv(email_list))