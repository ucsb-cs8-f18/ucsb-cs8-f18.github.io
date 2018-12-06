---
num: "Lecture 17"
desc: "Final Review"
pdfurl: /lectures/pdf/lect17.pdf
ready: true
date: 2018-12-06 9:30:00.00-7:00
---


# CS 8 Final Exam Review
- Final Exam: Tuesday 12/11, 8am - 11am, BUCHN 1920
- Seating is assigned: check the [seat assignment for F18](https://docs.google.com/spreadsheets/d/1drNXWhbSf7qDbTp8GeiGn22oktQ65GnZDuus69R-Suw/edit?usp=sharing)
- Check the [layout of the room](https://docs.google.com/spreadsheets/d/1DCXIO-g_TtvXU2vV4L5AVtZdrQFIZeuQZ8TpT9JMPWI/edit?usp=sharing) to locate your seat
- Link to code written in lecture: [https://github.com/ucsb-cs8-f18/cs8-f18-lecture-code](https://github.com/ucsb-cs8-f18/cs8-f18-lecture-code)
- Exam will be longer than the midterm (~ twice as long, ~ 2 hours)
- Exam is cumulative (covers everything from print statements
to complex data structures)
- Logistics
    - Bring writing utensil (dark led or pen)
    - Bring your student ID
    - No electronic devices
    - Closed book andonly one sheet of notes. No electronic devices
- Structure of final is similar to the midterms. Types of questions:
    - Evaluate expressions
    - Evaluate types
    - Given code, what is the output
    - Short answer / definitions
    - Read / write assert statements and test code
    - Complete function definitions / write python statements
    - Fill-in-the-blank
        - complete function definition key terms
        - pass in specific paramaters
        - etc.
    - General Advice
        - Read instructions carefully - pay close attention to
        what is being asked
        - Double-check your work

```
'''
## Advice on how to prepare
    - Lecture notes (important to know topics, examples,
    concepts).
    - Review code written in lecture 
      - Type out the code and understand the output 
    - Understanding labs and being able to implement them
    - Reading the textbook for additional details and
    understanding
        - Do the examples to solidify understanding
    - Homework exercises
    - Prototyping - "I wonder how python behaves when ..."
        - write a simple example
        - Helps with code practice as well as understanding the language and edge cases

## Overview of topics covered after midterm 2

* File I/O
    - Read file (infile = open('example.txt', 'r'))
        - infile.read()
        - infile.read(n)
        - infile.readlines()
        - infile.readline()
        - for a_line in infile
    - Write file (outfile = open('example.txt', 'w'))
    - Append file (outfile = open('example.txt', 'a'))
        - outfile.write(somestring)

* Dictionaries
    - key / value pairs
    - Creating a dictionary
    - Adding to a dictionary
    - dictionary methods
        - .pop(key)
        - .get(key)
        - .keys()
        - .values()
        - .items()

* Sets
    - Collection of items with no duplicates
    - Creating an empty set or a set from a list
    - Set operators
        - in, not in, combine(|), intersection(&), difference(-), unique(^)
    - Set comparisons
        - ==, !=, proper subset (<), subset (<=)
    - Set methods
        - .add, .clear


* Recursion
    - Properties of recursion
        - base case
        - recursive calls getting "closer" to base case
    - Examples in class and lab
        - print
        - reconstruct lists and strings (reverse a string or list)
        - computing values (factorial, fibonacci, ...)
        - etc.

## Topics covered before midterm 2 (refer to previous lecture notes)
- Python data types
- Arithmetic
- Python built-in functions
- Comparison operators
- Boolean operators
- Strings
- Lists
- Tuples
- User-defined functions
- Namedtuples
- Testing (assert / pytest)
- For loops
- Nested control structures
- Accumulator Patterns
- Nested (double) for loops
- While loops
    - Break, continue, pass
- 2D Lists
- String functions and formatting
- Random
'''
```