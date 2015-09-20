__author__ = 'Shawn Daniel'

import os
import operator


path = 'C:\\test'
folders = {key: 0 for key in os.listdir(path) if os.path.isdir(os.path.join(path, key))}

def count_files():
    for folder in folders.keys():
        folders = len(os.listdir(os.path.join(path, user)))
        folders[folder] = file_count
    sorted_count = sorted(folders.iteritems(), key=operator.itemgetter(1), reverse=True)
    for x, y in sorted_count:
        if y > 0:
            print x, y
    return sorted_count

count_files()
