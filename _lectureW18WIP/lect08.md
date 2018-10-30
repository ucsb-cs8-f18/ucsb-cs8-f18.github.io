---
num: "Lecture 8"
desc: "Iterating through lists, Accumulator Pattern, Nested Loops, While Loops"
ready: true
date: 2018-02-13 14:00:00.00-7:00
---

```
# CS 8, 2-13-18

''' Midterm
    - Average 54.92 / 68
    - Medium: 55.25
    - std: 5.94

- Common mistakes on the midterm
    - print("some string") # removes the quotations when
    outputting to the console
    - 1 / 1 = 1.0 # division returns a float type
    - return statements
        - A function immediately exits whenever it reaches
        a return statement.
        - A function can only return one value (but the
        value could be a collection (such as a list) that
        contains many values.

- Accumulator Pattern
    - Have seen this already in lab, but let's go into more
    detail.
    - Useful for "accumulating" something while traversing
    a collection.
        Example: Count the number of times, count the
        number of characters in a string, ...

#Example

listOfStrings = ["this", "is", "a", "list", "of", "strings"]
numList = [8,2,6,4,0]

def computeLengthManually(someList):
    """ count the number of items in the list manually """
    elements = 0
    for e in someList:
        elements += 1 # elements = elements + 1
    return elements

print(computeLengthManually(listOfStrings))
print(computeLengthManually(numList))
'''
"""
# Another Example
sentence = '''
This is a pretty long sentence, with many many words and
letters, and a bad example of what good sentence structure
would look like, so don't do this
'''
print(sentence)

print(sentence.split())
# split() "splits" a string into a list of strings
# separated by ' ', '\n', or '\t' (whitespace)

print(sentence.split(','))
# split(',') "splits" the string into a list of strings
# separated by ','
# Notice that commas are removed from the actual values
# May be useful for comma separated value (csv) formats

# strip() string method
# Removes the whitespace at the beginning and end of
# strings
x = "     abc    "
print("---" + x + "---")
print("---" + x.strip() + "---") # removes whitespaces at ends

y = "--,!'fj,ka--"
print(y.strip("-,!'")) # removes these characters from
                       # the beginning and end
"""
"""
sentence = '''
This is a pretty long sentence, with many many words and
letters, and a bad example of what good sentence structure
would look like, so don't do this
'''

# Example
def countLongWords(someString):
    ''' counts words longer than 5 characters '''
    counter = 0
    words = someString.split()
    for w in words:
        if len(w) > 5:
            counter += 1
    return counter

print(countLongWords(sentence))
"""
