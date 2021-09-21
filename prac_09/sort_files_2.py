"""
CP1404/CP5632 Practical
Files To Sort v2
Jeffrey Timms
"""
import shutil
import os
import pathlib

extension_list = ["doc", "docx", "gif", "jpg", "png", "txt", "xls", "xlsx"]
os.chdir('FilesToSort')
for extension in extension_list:
    category = input(f"What category would you like to sort {extension} files into?")
    if not os.path.exists(category):  # if directory doesn't exist create it
        if extension != "":
            os.mkdir(category)
    for filename in os.listdir('.'):
        if extension != "":
            if filename.endswith(extension):
                shutil.move(filename, str(category))

