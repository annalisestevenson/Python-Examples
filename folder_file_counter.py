__author__ = 'Shawn Daniel'
"""
Initially decided to write this for some server software although, it is a good example
for python beginners and can be generally useful when more capabilities added.
"""

import os
from sys import argv
import time

# path = "C:\\test"
script, path = argv
folders = {key: 0 for key in os.listdir(path) if os.path.isdir(os.path.join(path, key))}


def count_files():
    """prints the number of files within each directory then the age of the directory itself"""
    for folder in folders.keys():
        file_count = len(os.listdir(os.path.join(path, folder)))

        current_date = time.localtime()
        folder_date = time.localtime(os.stat(os.path.join(path, folder)).st_ctime)
        month = current_date[1] - folder_date[1]
        day = current_date[2] - folder_date[2]
        year = current_date[0] - folder_date[0]

        while month < 0 or day < 0 or year < 0:
            if year < 0:
                year += 1
                month -= 12
            elif month < 0:
                year -= 1
                month += 12
            elif day < 0:
                month -= 1
                day += 30
        duration_formatted = "%d Years, %d Months, %d days" % (year, month, day)
        folders[folder] = file_count, duration_formatted
    sorted_count = sorted(folders.items(), key=(lambda x: x[1]), reverse=True)
    for x, y in sorted_count:
        if y[0] > 0:
            print "{:<35} {:^10} {:>5}".format(x, y[0], y[1])
        else:
            pass

count_files()
