---
num: "Lecture 3"
desc: "Python Strings, Lists and Functions"
ready: false
date: 2018-10-04 9:30:00.00-7:00
---

## Today's lecture:

* Working with strings and lists
* Functions: Using existing ones, defining new functions

## Concept Questions

* Check your understanding: [Lect 03 Concept Questions](lect03-concept.md){:data-ajax ="false"}
* You'll need your iclickers to participate in class

```
# CS 8, 2018-10-04

'''
# Some more Terminology

Syntax: Grammar, how you say something
Semantics: Meaning, what it does.

syntactically incorrect PI equals 3.14159
semantically incorrect PI = "apple"
'''

'''

'''
Strings: Collections of characters (a-z, A-Z, 0-9 + special characters)
Indexing strings and substrings
    - In a string, we can extract certain pieces from it.
    - This is known as "parsing" a string
    - Positions in a string start at index 0

schoolName = "UCSB"
print(len(schoolName)) # 4
print(type(schoolName)) # str
print(schoolName[0])
print(schoolName[3])
#print(schoolName[4]) #ERROR
print(schoolName[-1]) # B - refers to the last index
#print(schoolName[-5]) # ERROR

#Extract a substring
print(schoolName[1:3]) # from position 1 up to (but not
                       # including) position 3

print("Does", school, "contain 'S'?", 'S' in school)

'''
Lists
    - A list is a collection of multiple values
    (similar to how a str is a collection of
    characters).
    - Note: In python, lists can be of heterogenous
    (different) types
    - Lists can have duplicate values
'''

'''
#Examples
evenNumbers = [2, "4", 6, "8"]
print(evenNumbers)
print(type(evenNumbers))
print(evenNumbers[2])
print(evenNumbers[-1])
evenNumbers.append(10)
print(evenNumbers)
#print(evenNumbers[1] + evenNumbers[2]) # ERROR
print(int(evenNumbers[1]) + evenNumbers[2])

print(evenNumbers.pop(1))
print(evenNumbers)
print(evenNumbers.pop())
print(evenNumbers)

names = ["Rick", "Morty", "Summer"]
names.sort()
print(names)
oddNumbers = [5, 3, 1]
oddNumbers.sort()
print(oddNumbers)
names.append(2018)
print(names)
names.sort() # ERROR, incompatible types 2018 is int
print(names)
'''

# Function definition
def double(n):
    ''' Returns 2 times the parameter '''
    return 2 * n

'''
- The "def" indicates a function definition
- "double" is the name of the function
- (n) denotes the parameter(s) of a function
- name + parameters is known as a function SIGNATURE
- The actual code (instructions) (ex: return 2 * n)
is known as the function BODY
- Note: The function body needs to be indented so python
can associate the body's instructions as part of the
function's definition
- If the function returns a value, then a RETURN statement
is needed
'''
# Examples calling double()
print(double(10)) # --> print(20)
print(double(double(2))) # --> print(double(4)) --> print(8)
value = double(5) + double(6)
print(value)

print(double("2"))
print(type(double("2")))
print(double(2.5))
print(type(double(2.5)))
print(double([2,4,6]))
```
















