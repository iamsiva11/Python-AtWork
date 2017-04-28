"""
Module to get the list of code files to Index
Given the path, get the list of all the files to index
"""

import linecache

#Print Lines
def getfileLine(file,line):
    LineAt = linecache.getline(file,line)
    return LineAt
