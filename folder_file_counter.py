__author__ = 'Shawn Daniel'
"""
    This simple script counts the number of files within all the directories
that are located within a given path. Then it sorts the number of files
per folder by descending order. More capabilities are planning to be added

Initially decided to write this for some server software although, it is a good example
for python beginners and can be generally useful when more capabilities added.
"""

import os
from sys import argv


script, path = argv
# list all directories within "path" variable and create a dict with each of them as the keys and 0 as their value
folders = {key: 0 for key in os.listdir(path) if os.path.isdir(os.path.join(path, key))}   


def count_files():
    for folder in folders.keys():   # for each folder count the length of it
        file_count = len(os.listdir(os.path.join(path, folder)))
        folders[folder] = file_count
# return copy of items as tuples inside new list, then sort them by their values in descending order
    sorted_count = sorted(folders.items(), key=(lambda x: x[1]), reverse=True)
# if file count > 0, print each folder with it's count number on each line
    for x, y in sorted_count:
        if y > 0:
            print x, y
        else:
            continue

count_files()
