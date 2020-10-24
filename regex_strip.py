#! python3

import re

def strip_text(text, remove):
    if remove == '':
        text_regex = re.compile(r'^\s*')
        stripped_text = text_regex.sub('', text)
        text_regex = re.compile(r'\s*$')
        stripped_text = text_regex.sub('', stripped_text)
        return stripped_text
    else:
        text_regex = re.compile(remove)
        stripped_text = text_regex.sub('', text)
        return stripped_text

text = input("Please enter text to strip.\n")
#print(len(text))
char_remove = input("Enter character you want removed. (Leave blank to remove only white space from both ends.\n")

stripped_text = strip_text(text, char_remove)
print(stripped_text)
#print(len(stripped_text))