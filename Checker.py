import os
import re

from config import pkl_name

def add_multiline_flag(pattern):
    return re.compile(pattern.pattern, re.MULTILINE)

modified_pattern = add_multiline_flag(pattern)


# Function to check if the pattern exists in the file
def check_pattern_in_file(file_path):
    global modified_pattern
    with open(file_path, 'r',encoding=detect_encoding(file_path),errors='replace') as file:
        contents = file.read()
        contents= clean_line(contents)
        #if modified_pattern.search(contents):
            #print(f"Pattern found in {file_path}.")
        #else:
        if not modified_pattern.search(contents):
            print(f"Pattern not found in {file_path}.")

# Function to recursively search for .txt files and check the pattern
def check_pattern_in_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                check_pattern_in_file(file_path)

# Directory path
directory = r'C:\Users\clint\Desktop\Studied_Trucks\Data\Raw\set1'

# Check pattern in all .txt files in the directory and subdirectories
check_pattern_in_directory(directory)

#look at birmingham and chicksaw
