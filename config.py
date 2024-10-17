import re 
import chardet

pkl_name = "grouped_text.pkl"
pattern = re.compile(r"""
    (?i)                    # Case-insensitive mode
    ^\d+\.\d+\.\d+          # Matches patterns like 1.2.3
    | ^sec\. \d+-\d+[a-z]?-\d+  # Matches patterns like Sec. 1-2a-3
    | ^sec\. \d+-\d+        # Matches patterns like Sec. 1-2
    | ^sec\. \d+\.\d+       # Matches patterns like Sec. 1.2
    | ^sec\. \d+\.\d+       # Matches patterns like Sec. 91.01
    | ^naics \d+            # Matches patterns like NAICS 12345
    | ^section \d+          # Matches patterns like Section 123
    | ^§ \d+\.\d+           # Matches patterns like § 1.2
    | ^� \d+-\d+-\d+        # Matches patterns like � 1-2-3
    """, re.IGNORECASE | re.VERBOSE)


def detect_encoding(filepath):
    with open(filepath, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
        return encoding
    
def clean_line(line):
    line = re.sub(r'[",!?*\[\]]', '', line)
    line = re.sub(r';', ' ', line)
    line = re.sub(r'\\', '', line)
    return line