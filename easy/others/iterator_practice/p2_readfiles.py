"""
Write a program that takes one or more filenames as arguments and prints all the lines which are longer than 40 characters.
"""

def readfiles(files):
    for f in files:
        for line in open(f):
            yield line

def main(filenames):
    lines = readfiles(filenames)
    for l in lines:
        if len(l) > 40:
            print l

if __name__ == '__main__':
    main(['data.txt'])    
    
    
