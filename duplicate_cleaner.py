#!/usr/bin/env python

import os
import getopt, sys

def get_all_folder_content(dir_name):
    result = []
    for path, subdirs, files in os.walk(dir_name):
        for name in files:
            result.append(os.path.join(path, name))
    return result

def clean_duplicates_in_file(input_file_name):
    # if output_file_name == '':
    #     output_file_name = input_file_name
    with open(input_file_name, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
    if lines[-1][-1] != '\n':
        lines[-1] += '\n'
    lines.sort()
    i = 0
    while i < len(lines) - 1:
        if lines[i] == lines[i + 1]:
            del lines[i]
        else:
            i += 1
    return lines

def clean_duplicates_in_dir(input_dir_name):
    # if output_dir_name == '':
    #     output_dir_name = input_dir_name
    result = []
    for input_file_name in get_all_folder_content(input_dir_name):
        result += clean_duplicates_in_file(os.path.join(input_file_name))
    return result

def get_whitelist(whitelist_path):
    if os.path.isdir(whitelist_path):
        lines = []
        for file_name in get_all_folder_content(whitelist_path):
            with open(os.path.join(file_name), 'r', encoding='utf-8', errors='ignore') as f:
                lines += f.readlines()
    else:
        with open(whitelist_path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
    i = 0
    while i < len(lines):
        if lines[i][-1] == '\n':
            lines[i] = lines[i][:-1]    
        i += 1
    return lines

def search_in_results(search_lines, search_source, output_file_name):
    if os.path.isdir(search_source):
        lines = []
        for file_name in get_all_folder_content(search_source):
            with open(os.path.join(file_name), 'r', encoding='utf-8', errors='ignore') as f:
                lines += f.readlines()
    else:
        with open(search_source, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
    i = 0
    while i < len(lines):
        if lines[i][-1] == '\n':
            lines[i] = lines[i][:-1]    
        i += 1
    not_found_strings = []
    found_strings = []
    known_text = " ".join(lines)
    lines = search_lines
    i = 0
    while i < len(lines):
        if lines[i][-1] == '\n':
            lines[i] = lines[i][:-1]    
        i += 1
    for line in lines:
        if known_text.find(line) == -1:
            not_found_strings.append(line)
        

    not_found_strings.sort()
    #clean duplicates
    i = 0
    while i < len(not_found_strings) - 1:
        if not_found_strings[i] == not_found_strings[i + 1]:
            del not_found_strings[i]
        else:
            i += 1
    #clean whitelist
    if whitelist_flag:
        whitelist = get_whitelist(whitelist_path)
        i = 0
        while i < len(not_found_strings):
            if not_found_strings[i] in whitelist:
                del not_found_strings[i]
            else:
                i += 1
    #output
    if output_file_name == '':
        print('Not found these:')
        for not_found_string in not_found_strings:
            print(not_found_string)
    else:
        if os.path.isdir(output_file_name):
            output_file_name += '/output.txt'
        with open(output_file_name, 'w', encoding='utf-8') as f:
            for not_found_string in not_found_strings:
                f.write(not_found_string + '\n')     
        

input_path = ''
output_path = ''
search_path = ''
whitelist_path = ''

whitelist_flag = False

argumentList = sys.argv[1:]
options = "hi:o:s:w:"
long_options = ["help", "input=", "output=", "search=", 'whitelist=']

try:
    arguments, values = getopt.getopt(argumentList, options, long_options)
     
    for currentArgument, currentValue in arguments:
 
        if currentArgument in ("-h", "--help"):
            print ("""
            -i, --input: input directory or file
            -o, --output: output directory or file
            -s, --search: search file or directory
            -w, --whitelist: whitelist file or directory
            """)
             
        elif currentArgument in ("-i", "--input"):
            input_path = currentValue
             
        elif currentArgument in ("-o", "--output"):
            output_path = currentValue

        elif currentArgument in ("-s", "--search"):
            search_path = currentValue
        elif currentArgument in ("-w", "--whitelist"):
            whitelist_path = currentValue
            whitelist_flag = True
             
except getopt.error as err:
    print (str(err))
    sys.exit(2)
if input_path == '' or search_path == '':
    print("Please, enter all required parameters\nUse -h or --help for help")
    sys.exit(2)

data_to_analyze = []

if os.path.isdir(input_path):
    data_to_analyze = clean_duplicates_in_dir(input_path)
else:
    data_to_analyze = clean_duplicates_in_file(input_path)

search_in_results(data_to_analyze, search_path, output_path)