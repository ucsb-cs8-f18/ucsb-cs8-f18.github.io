---
num: "Lecture 10"
desc: "File IO"
pdfurl: /lectures/pdf/lect10.pdf
ready: true
date: 2018-11-07 9:30:00.00-7:00
---

```
# Some tools for the labs
# min, max, round

print(max(15.7,2,16.2,8))
print(min(16.2,6))
print("---")
print(round(14.9999999999))
print(round(15.5))
print(round(15.4999999999))

# Files
    - FILES are a valuable tool to help us solve many
    types of problems.

FILES give us PERSISTENCE
    - So far, we've been running our programs in IDLE and
    putting our code into a file.
    	* Data must be entered on every program run
    	* Programs have no way to write permanent output
    - With PERSISTENCE, our data can be "saved" between
    each program execution.

FILE BASICS:
    - We can store files in many different forms
        - Examples: .xls, .docx, .pdf, .jpg, ...
        - For this class, we'll just deal with "plain text"
        files (.txt)
        - These CHARACTERS are represented in something called
        ASCII (American Standard Code for Information Interchange)
        - This was dominant / simple way of representing text
        where each character is 8 bits long
        - UTF-8 is the most popular format in today's web browsers
        - Allows us to represent MANY characters from multiple
        languages

TERMS:
    
   	File: A document
    Directory: A folder containing files and other folders
    File System: Collection of all the files and folders on the
        computer, organized in a heirarchy
    For this class, we'll deal with reading and writing files
    that are in the same directory as our .py file (known as
    our "working directory"
        - This makes our lives much easier

The Unix File system:
- In unix the directory at the highest level of the hierarchy is called the root (denoted by /). All other directories and files are stored within the root
- Path: The path is a sequence (of directories) that specifies the location of a file or directory within the file system. For example, /Users/diba/ says that the directory diba is within the directory Users which is within the root

	* An ABSOLUTE path describes the location of a file or directory starting with the root (/)
	* A RELATIVE path describes the location of a file relative to the current directory. For example ./cs8/lab05/ (Here './' stands for "current directory" ) 

- You can move through the unix file system via the command line (instead of using the graphical interface)
- Few useful unix commands
  - pwd (path to your current working directory)
  - ls  (list all the files and directories within the current directory)
  - mkdir (make a new directory)
  - cd (change into a directory, need to give either absolute or relative path)



FILE I/O:
    - I/O stands for input / output
    - We read data from a file into our program.
    - We write data from our program into a file.
    - Steps for File I/O
        1. Open the file (creates a "connection" between your
        program and the file).
            - Choose if the connection will be for reading,
            writing, or appending to a file.
        2. Read the data / write the data
        3. Close the file (close the "connection"). This should
        to be done once per file.

Common ways to read data from files
    1. read() method - reads the entire file into one string
        - Good for small data (large files may be too big to
        store into memory)
    2. read(n): Read the next n characters from the input
        - Better for larger files since you only need to store
        n characters in memory at a time.
    3. readline(): Reads everything from the current position
        to the next '\n' (or to the end of the file, 'EOF'). If
        nothing left to read, .readline() returns an empty string.
    4. readlines(): Reads all the lines in the file and returns
        a list.
    5. for a_line in infile:
        - a_line represents a line in the file, infile is the
        open file.
'''

'''
# Example reading from 'example.txt'
infile = open('example.txt', 'r')
data = infile.read()
print(data)
infile.close()
'''
'''
# Example writing to a file 'example_2.txt'
outfile = open('example_2.txt', 'w')
outfile.write("Duck\nCow\nCat")
outfile.close()
'''
'''
# Create a list of lines in the file
infile = open('example.txt', 'r')
datalines = infile.readlines() # returns a list of strings
print(datalines)
infile.close()
'''
'''
# Write "overwrites" the existing file
outfile = open("example.txt", 'w')
outfile.write("Something new!\n")
outfile.write("Another line!")
outfile.close()
'''
'''
# Append to an existing file
outfile = open("example.txt", 'a')
outfile.write("Something else!\n")
outfile.write("Yet another line.")
outfile.close()
'''
'''
# read(n)
infile = open("example.txt", 'r')
data = infile.read(3)
print(data)
data = infile.read(6)
print(data)
infile.close()
'''
'''
# readline example
infile = open("example.txt", 'r')
line = infile.readline()
print(line)
line = infile.readline()
print(line)
infile.close()
'''
'''
# Example of copying / writing to another file
infile = open('example.txt', 'r')
outfile = open('copy.txt', 'w')
for line in infile:
    outfile.write(line)
infile.close()
outfile.close()
'''
