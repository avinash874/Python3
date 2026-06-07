# "Write a python program to print the contents of a directory using the os module. Search online for the function which does that."

import os

# select the path whose content you want to list
path = "/Users/avinashsingh/Desktop/ALLLL"

 # Get all files and folders from current directory
contents = os.listdir(path)

# Print each item in the directory
print("Contents of the directory:")
for item in contents:
    print(item)