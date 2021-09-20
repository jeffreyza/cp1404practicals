import shutil
import os
import pathlib

os.chdir('FilesToSort')
for filename in os.listdir('.'):
    #    print(pathlib.Path(filename).suffix)
    extension = os.path.splitext(filename)[1][1:]
    os.mkdir(extension)
