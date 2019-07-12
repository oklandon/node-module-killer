import os
import re
import shutil

#dir = './canopy'

print("clear node_modules from which directory?")
dir = input()

for subdir, dirs, filenames in os.walk(dir):
    if re.search('node_modules$', subdir):
        print("Deleting from: " + subdir)
        shutil.rmtree(subdir)

print("done")
