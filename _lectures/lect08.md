---
num: "Lecture 8"
desc: "for loops, iterating through lists and strings using for loops"
pdfurl: /lectures/pdf/lect08.pdf
ready: false
date: 2018-10-30 9:30:00.00-7:00
---


```

''' Midterm
    - Average 86.54
    - Medium: 89.75
    - std: 11.91

Common mistakes on the midterm

Q1:  
* 1.5 and 1.14: Incorrect indexing (1st element in a list starts at index 0). 
* person[0:2] is [0 is included, 2 is excluded].
* 1.7: string[-1] is not an error, returns the last char in the string


Q2: 
* Use of escape characters , when to use single vs. double quotes
* Forward slash vs  backslash 
* "I\'m " or 'I\'m' not 'I'm' or "I\'m"
* print("some string") # removes the quotations when outputting to the console
* Incorrect use of eval

Q3: Commas in the print statement are used to separate different arguments to print e.g. print("Hi", name). Here the comma is not actually printed as part of the  output, issues with slicing e.g. name[2:] 

Q4: Had trouble moving the turtle back to the initial position - didn't know how or missed it.  

(1) Some code works only if the initial position is at (0,0)
(2) Forgot pen up() and pen down() when returning the turtle to its initial position, some students retraced the L which is correct


Q5: 

* trouble using the type function
* syntax errors in the if statement (missing the ending colon)
* using /= instead of !=
* Assuming \ that the if statement stores the values and tries to use the logic at the end -
    - EX: type(a) and type(b) and type(c) == int

* Missing the colon in the def statement
* Calculating the result first and then checking the type 
* print vs return 


Q6: 
* Missed that test functions in pytest need to be prefixed with test_
* Use of assert , forgot the == comparison, just called the function
* misunderstanding of pytest.approx: passed in call to quadratic

Q7.1 issues with formatting the output
Q7.3 missed the print inside the function (possible issue with tracing function calls)
Q7.3 Assumed that a return is always needed in the function
Q7.4. Local vs global 



# Loops

# More on loops
name = "Bob"
for c in name:
    print(c)
    print("----")

print("resuming program execution")

# range function
    - range() is a function used for looping if we know
    the number of iterations we want to make.
    - range(x) returns a collection of numbers including
    0 up to (but not including) x
    - Think of range(4) as [0, 1, 2, 3]
'''
'''
# Example using range()
for x in range(4):
    print("Hello!" * x)
    print("----")
'''
'''
# Example looping from numbers 2, 3, 4, 5 using range
for x in range(2,6):
    print(x)
    print("----")

# range is similar to substring - 1st parameter defines
# the 1st number and loops up to (but not including)
# the 2nd parameter's number
'''
'''
# Example using range with steps
for x in range(0, 10, 2):
    print(x)
    print("----")
'''
'''
# Example by manually updating a variable in the loop
intList = [2,4,8,16,32,64,128,256,1024]
counter = 1
for x in intList:
    print("2 ^ ", counter, "=", x)
    counter = counter + 1
'''


# Example: Write a function and run some assert tests

def hasOddNumber(list):
    ''' Returns True if the list has an odd number.
        Returns False otherwise
    '''
    for x in list:
        if (x % 2 != 0):
            return True
    return False

numbers1 = [2,4,5,6,8]
numbers2 = [0,10,20,30]
numbers3 = []

# Test by observation
print(hasOddNumber(numbers1))
print(hasOddNumber(numbers2))
print(hasOddNumber(numbers3))

# Test by assertions
assert hasOddNumber(numbers1) == True
assert hasOddNumber(numbers2) == False
assert hasOddNumber(numbers3) == False

- Accumulator Pattern

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



