"""
CP1404/CP5632 Practical
Files To Sort v1
Jeffrey Timms
"""

import shutil
import os
import pathlib

os.chdir('FilesToSort')
for filename in os.listdir('.'):
    #    print(pathlib.Path(filename).suffix)
    extension = os.path.splitext(filename)[1][1:]  # will extract text after . to get extension only
    if not os.path.exists(extension):  # if directory doesn't exist create it
        if extension != "":
            os.mkdir(extension)


'''Verifies that the extension is not an empty string. Move file to designated folder
based on extension'''
for filename in os.listdir('.'):
    extension = os.path.splitext(filename)[1][1:]
    if extension != "":
        if filename.endswith(extension):
            shutil.move(filename, str(extension))
