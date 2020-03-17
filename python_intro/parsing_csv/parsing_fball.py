#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 16:20:26 2020

@author: darienpmt
"""
import csv


# The football.csv file contains the results from the English Premier League.
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of
# goals scored for and against each team in that season (so Arsenal scored 79 goals
# against opponents, and had 36 goals scored against them). Write a program to read the file,
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

def read_data(filename):
    """Returns a list of lists representing the rows of the csv file data.

    Arguments: filename is the name of a csv file (as a string)
    Returns: list of lists of strings, where every line is split into a list of values. 
        ex: ['Arsenal', 38, 26, 9, 3, 79, 36, 87]
    """
    with open(filename) as fn:
        data = [lines for lines in list(csv.reader(fn))]
            
        return data
    
def get_index_with_min_abs_score_difference(goals):
    """Returns the index of the team with the smallest difference
    between 'for' and 'against' goals, in terms of absolute value.

    Arguments: parsed_data is a list of lists of cleaned strings
    Returns: integer row index
    """
    diffs = [abs(int(lst[5]) - int(lst[6])) for lst in goals[1:]]
    
    return diffs.index(min(diffs)) + 1
    
def get_team(index_value, parsed_data):
    """Returns the team name at a given index.
    
    Arguments: index_value is an integer row index
               parsed_data is the output of `read_data` above
               
    Returns: the team name
    """
    return parsed_data[index_value][0]
    

# Following functions will be called like this:
footballTable = read_data('football.csv')
minRow = get_index_with_min_abs_score_difference(footballTable) 

print("Team with minimum absolute goal differential: " + str(get_team(minRow, footballTable)+ '.'))