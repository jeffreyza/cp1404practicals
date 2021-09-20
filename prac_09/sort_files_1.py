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

extensions = ["doc", "docx", "gif", "jpg", "png", "txt", "xls", "xlsx"]
