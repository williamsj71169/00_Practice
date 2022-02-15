# source: https://www.guru99.com/reading-and-writing-files-in-python.html

import re

has_error = "yes"
while has_error == "yes":
    print()
    filename = input("Enter a Filename: ")
    has_error = "no"

    valid_char = "[A-Za-z0-9_]"
    for letter in filename:
        if re.match(valid_char, letter):
            continue
