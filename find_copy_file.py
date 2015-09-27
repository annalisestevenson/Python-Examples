__author__ = 'Shawn Daniel'
"""
This code speaks for itself and demonstrates why I love Python.
In roughly 4 lines of code it finds and downloads all files with
said extension.
 """

import fnmatch
import os.path
import shutil

path = 'C:\\Users'

for path, dirs, files in os.walk(path):
    for file in files:
        if fnmatch.fnmatch(file, '*.doc'):
            shutil.copy(os.path.join(path, file), './')



