---
num: "Lecture 9"
desc: "Named tuples, Nested for loops and other nested control structures"
pdfurl: /lectures/pdf/lect09.pdf
ready: true
date: 2018-11-01 9:30:00.00-7:00
---


```
from collections import namedtuple
Student = namedtuple('Student', 'name perm major gpa')
s1 = Student("Nick", 12345, "PSYCH", 3.9)
print(s1)
#s1.gpa = 4.0 # ERROR, namedtuples are IMMUTABLE (they cannot be changed)

''' seems intuitive to do something like changing an
attribute, but it's illegal because namedtuples are
IMMUTABLE.
'''

# Q: How can we change it?
# 1: Create a new object and reassign to variable
s1 = Student(s1.name, s1.perm, s1.major, 4.0)
print(s1)

# 2: Use a _replace method
s1 = s1._replace(gpa= 4.0)
# ._replace returns a new namedtuple and we assign back
# to the variable s1
print(s1)

''' Q: Why should we even care?
- It's the behavior of the language!
- Depending on whether or not something is immutable or
mutable, it affects how the data is treated when passing
it into a function.
'''

'''More on the accumulator pattern
'''

def countElements(lst):
  '''returns the number of elements in lst'''
  return "stub"


def countOddNumbers(lst):
  '''returns the number of odd numbers in lst'''
  return "stub"


def countWords(sentence):
  '''returns the number of words in the sentence'''
  return "stub"


def countWords(sentence, len):
  '''returns the number of words in the sentence with length greater than len'''
  return "stub"


def createOddList(lst):
  '''returns a new list that contains all the odd numbers in lst'''
  return "stub"

 
    

''' Nested Loops
- Depending on how data is organized, it's common to see
loops within loops.
- For example, given a list of strings, we may want to
manually count how many vowels exist throughout the list
'''
'''
# Nested-for loop example

def drawRectangle(width, height):
  '''print a rectangle with given width and height using the character *
    (instead of turtle)'''
  return

def drawTriangle(height):
  '''print a right triagle with given height using stars(*).
     Assume the size of the base and height are equal'''
  return


def countVowels(strList):
  """ Count vowels in list of strings """
  
  
listOfStrings = ["this", "is", "a", "list", "of", "strings"]

print(countVowels(listOfStrings)) # should return  6
'''
```


