__author__ = 'Shawn Daniel'
"""
    This simple script counts the number of files within all the directories
that are located within a given path. Then it sorts the number of files
per folder by descending order.

I made this for some server software although it can be generally
useful, as well as a good example for beginner programmers. It shows how
you can use list comprehensions, converting / sorting dictionaries as
lists, and examples on how to begin using the os, and operator modules.
"""

import os
import operator


path = 'C:\\test'
# list all the directories from "path" variable and create a dictionary with each of the folders as the keys
# and 0 as their default values
folders = {key: 0 for key in os.listdir(path) if os.path.isdir(os.path.join(path, key))}

def count_files():
    for folder in folders.keys():
        file_count = len(os.listdir(os.path.join(path, user)))     # for each folder assign the length of each folder
        folders[folder] = file_count    # assign file_count as the (value) to the corresponding folder (key)
    # iterate through the items in the dictionary and sort them by assigning a new list then sorting their values
    # (1)=file_count in reverse (descending) order
    sorted_count = sorted(folders.iteritems(), key=operator.itemgetter(1), reverse=True)
    for x, y in sorted_count:
        if y > 0:
            print x, y
    return sorted_count

count_files()
