"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            new_file_name = get_fixed_filename(filename)
            print(f"Renamed {filename} to {new_file_name}")
            name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name


main()
