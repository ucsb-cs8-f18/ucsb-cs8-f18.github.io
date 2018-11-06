---
num: "Lecture 10"
desc: "File IO, String Formatting"
pdfurl: /lectures/pdf/lect09.pdf
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
    - Between each run, our data is cleared and everything
    has to be reloaded again.
    - With PERSISTENCE, our data can be "saved" between
    each program execution.

FILE BASICS
    - We can read from files
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
    File: A document
    Directory: A folder containing files and other folders
    File System: Collection of all the files and folders on the
        computer
    For this class, we'll deal with reading and writing files
    that are in the same directory as our .py file (known as
    our "working directory"
        - This makes our lives much easier

The Unix File system:
- Files are stored in directories, directories are stored in other directories. In unix the topmost directory stores all other directories and files. This directory is called the root (denoted by /) 
- You can move through the unix file system via the command line (instead of using the graphical interface)
- Few useful unix commands
  - pwd (path to your current working directory)
  - ls  (list all the files and directories within the current directory)
  - mkdir (make a new directory)
  - cd (change into a directory, need to give either absolute or relative path)

- Path: The path is a sequence (of directories) that specifies the location of a file or directory within the file system. For example, /Users/diba/ says that the directory diba is within Users which is within the root

* An ABSOLUTE path describes the location of a file or directory starting with the root (/)

* A relative path  describes the location of a file or directory starting at the current directory. For example ./cs8/lab05/ (Here './' stands for "my current directory" ) 

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

# STRING FUNCTIONS
# We've seen several of these - .split(), .strip()
# We'll introduce some more...


s = "CS 8: Intro to Programming"
'''
print("Where does the first 'mm' occur in s?")
print(s.find("mm"))
print(s.find("jfklahgl"))

text = """This
string
has
multiple
lines"""

first_newline = text.find("\n")
print("First newline position:", text.find("\n"))
print("First line of text:", text[:first_newline])
print("String after first newline:", text[first_newline + 1:])
'''
'''
# .startswith method
print("Check if s starts with 'CS':", s.startswith("CS"))
print("Check if s starts with 'Computer':", s.startswith("Computer"))

# .endswith method
print("Check if s ends with 'P':", s.endswith("P"))
print("Check if s ends with 'inG':", s.endswith("inG"))
print("Check if s ends with 'ing':", s.endswith("ing"))

# .count method
print("Times 'm' is in s:", s.count("m"))
print("Times 'i' is in 'Mississippi':", 'Mississippi'.count('i'))
MS = "Mississippi"
print("Times 'ss' is in 'Mississippi':", MS.count('ss'))

# .replace method
print("Change all 'i' to '!' in 'Mississippi':", MS.replace("i", "!"))
print("Change all ':' to '#' in s:", s.replace(":", "#"))
print("Remove all 'i' in 'Mississippi':", MS.replace("i",""))

# Strings are immutable (these methods won't change the string)
print(s)
print(MS)

# Change the value with reassignment
s = s.replace("m", "M")
print(s)

# upper / lower case
print(s.lower())
print(s.upper())
print(s) # still didn't change
'''

# Examples of String formatting

price = 18.00
print("The price is ${}. That's cheap!".format(price))
print("The price is ${}. {}.".format(price,"wow!"))
print("{3:} {2:} {1:} {0:}".format('a','b','c','d'))

''' Format specification:
{ : }. Left side of colon say which argument to place into {}

To the right we specify a FIELD WIDTH (i.e., how many spaces/
columns on the screen to devote to this
'''
'''
print("-->{}<--".format(price))
print("-->{:20}<--".format(price))
print("-->{:20}<--".format("18"))
# We can use '>' or '<' to justify left or right
print("-->{:<20}<--".format("18"))
print("-->{:>20}<--".format("18"))
# we can use '^' to center.
print("-->{:^20}<--".format("18"))
'''
print("-->{:20.2f}<--".format(price))
# without 'f' , price appears in scientific notation

# More examples
price = 12345.6
print("-->{:10.2f}<--".format(price))
print("-->{:6.2f}<--".format(price))

# can identify specific types that should be expected with
# 's'- string, 'd' - int, 'f' - float
name = "Chris Gaucho"
age = 21
print("Name is {:12s}; age is {:2d}; price is ${:0.2f}".format(name,age,price))
print("Name is {:12}; age is {:2}; price is ${:0.2}".format(name,age,price))
# still works if s,d,f is not included, but removing 'f' will look strange

```