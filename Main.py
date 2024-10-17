import os
import re
import pickle
from config import pkl_name, pattern,detect_encoding,clean_line

#clear the file
with open(pkl_name, 'wb') as pkl_file:
    pass  # This will clear the file

def extract_file_name(file_path):
    base_name = os.path.basename(file_path)
    file_name, _ = os.path.splitext(base_name)
    return file_name




import pickle

def add_entries_to_dataset(file_path, new_entries):
    # Step 1: Check if the file is empty or does not exist
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        data = []
    else:
        # Step 2: Load the existing dataset from the .pkl file
        with open(file_path, 'rb') as file:
            data = pickle.load(file)

    # Step 3: Add new entries to the dataset
    data.extend(new_entries)

    # Step 4: Save the updated dataset back to the .pkl file
    with open(file_path, 'wb') as file:
        pickle.dump(data, file)

    print(f"New entries added and dataset saved to {file_path}")

import re

def text_collect(filename):
    global pattern
    sections = []
    current_section = None
    collected_text = []

    with open(filename, 'r',encoding=detect_encoding(filename),errors='replace') as file:
        for line in file:
            line = clean_line(line)
            match = pattern.match(line)
            if match:
                if current_section:
                    sections.append({
                        "Section": current_section,
                        "Text": ' '.join(collected_text),
                        "Zoning Location": extract_file_name(filename)
                    })
                current_section = match.group()
                collected_text = [line[len(current_section):].strip()]
            elif current_section:
                collected_text.append(line.strip())

        if current_section:
            sections.append({
                "Section": current_section,
                "Text": ' '.join(collected_text),
                "Zoning Location": extract_file_name(filename)
            })

    add_entries_to_dataset(pkl_name, sections)

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
