
"""
Usage: python walker.py <root_directory> <header_file>

Find all *.java files, paste contents of <header_file> at the top of each java file if the header is not already present.
"""
import os

def main():
    for root, dirs, files in os.walk("."):
        path = root.split('/')
        print (len(path) - 1) *'---' , os.path.basename(root)       
        for file in files:
            print len(path)*'---', file

if __name__ == "__main__":
    main()
	
