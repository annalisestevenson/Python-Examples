__author__ = 'Shawn Daniel'
"""
    This simple script counts the number of files within all the directories
that are located within a given path. Then it sorts the number of files
per folder by descending order. More capabilities are planning to be added

I made this for some server software although it can be generally
useful, as well as a good example for beginner programmers.
"""

import os
import operator


path = 'C:\\test'
folders = {key: 0 for key in os.listdir(path) if os.path.isdir(os.path.join(path, key))}   # list all the directories
# from "path" variable and create a dictionary with each of the folders as the keys and 0 as their default values

def count_files():
    for folder in folders.keys():
        file_count = len(os.listdir(os.path.join(path, user)))     # for each folder count the length of each folder
        folders[folder] = file_count    # assign file_count as the (value) to the corresponding folder (key)
    sorted_count = sorted(folders.iteritems(), key=operator.itemgetter(1), reverse=True) # iterate through dictionary,
    #  assign items as tuples inside new list "sorted_count", then sorts them by their values in descending order
    for x, y in sorted_count:
        if y > 0:
            print x, y
    return sorted_count

count_files()
