
"""
Usage: python header_adder.py <root_directory> <header_file>

Search recursively in <root_directory> for  *.java files, and prepend contents of
<header_file> at the top of each java file if the header is not already present.
"""
import os
import sys
import re


def is_java_file(filename):
    return re.search("\.java$", filename) is not None


def is_whitespace(s):
    return len(s.strip()) == 0


def has_header(filepath, header_lines):
    """ Test whether filepath contains header_lines at the top of the file.
    Ignore any initial lines of whitespace when checking for header content.
    """
    f = open(filepath, 'r')

    found_content = False
    header_line_counter = 0
    for line in f:
        # Skip empty lines at the top of the file
        if not found_content and is_whitespace(line):
            continue
        found_content = True

        if header_line_counter >= len(header_lines):
            # We have run out of lines to check
            break

        if line != header_lines[header_line_counter]:
            return False
        header_line_counter += 1
    f.close()

    return header_line_counter == len(header_lines)


def add_header(filepath, header_lines):
    file_lines = get_file_lines(filepath)

    f = open(filepath, 'w')
    f.writelines(header_lines)
    f.writelines(file_lines)
    f.close()


def get_file_lines(filepath):
    f = open(filepath, 'r')
    lines = f.readlines()
    f.close()

    return lines


def main():
    if len(sys.argv) != 3:
        print "Usage: python " + sys.argv[0] + " <root_directory> " + " <header_file>"
        sys.exit(1)

    root_dir = sys.argv[1]
    header_lines = get_file_lines(sys.argv[2])

    for root, dirs, files in os.walk(root_dir):

        for filename in files:
            filepath = os.path.join(root, filename)
            if is_java_file(filename) and not has_header(filepath, header_lines):
                print filepath
                add_header(filepath, header_lines)

if __name__ == "__main__":
    main()

