import os
import re
import pickle
from config import pkl_name, pattern,detect_encoding,clean_line

def text_collect(filename):
    global pattern
    sections = []
    current_section = None
    collected_text = []
    pattern_found = False
    with open(filename, 'r',encoding=detect_encoding(filename),errors='replace') as file:
        for line in file:
            line = clean_line(line)
            match = pattern.match(line)
            if match:
                print(f"Pattern found in {filename}.")
                pattern_found = True
                break
        if not pattern_found:
            print(f"Pattern not found in {filename}.")

    #add_entries_to_dataset(pkl_name, sections)

import os
import glob

def process_files(directory):
    # Use glob to find all .txt files in the directory and subdirectories
    txt_files = glob.glob(os.path.join(directory, '**', '*.txt'), recursive=True)
    for file_path in txt_files:
        #print(f"Processing {file_path}")
        text_collect(file_path)

# Directory containing the text files
directory = r'C:\Users\clint\Desktop\Studied_Trucks\Data\Raw\set0'

# Process all text files in the directory
process_files(directory)
