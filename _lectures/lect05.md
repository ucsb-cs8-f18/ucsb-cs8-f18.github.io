---
num: "Lecture 5"
desc: "Print vs. Return, Mutable vs. Immutable"
pdfurl: /lectures/pdf/lect05.pdf
ready: true
date: 2018-10-11 9:30:00.00-7:00
---


# Resources from lecture

* [Link to all code written in lecture](https://github.com/ucsb-cs8-f18/cs8-f18-lecture-code)



# "None" return type 

```python
# If a function does not return a value, then
# the "data" is "None".

# It's up to the developer to decide if a function should
# or should not return data depending on the intention
# of using the function

# Example
# print() # print function returns None
print(print()) # print(None) -> None

# Function that returns None
def noReturn():
    ''' prints and returns nothing '''
    print("in Function noReturn()")
    # return optional, but None is returned if there isn't a value

print(noReturn())
"""
```

# Print vs. Return

On the surface both these functions seem to be doing the same thing: given an input x , output double of x

```python
def return_dbl( x ):
   return x*2

def print_dbl( x ):
   print(x*2)

```

Here is when they seem to behave the same way

```python
>>>return_dbl(10)
20
>>>print_dbl(10)
20
```

But, here is when it gets weird...

```python
>>>print(return_dbl(10))
20
>>>print(print_dbl(10))
20
None
```
Try...

```python
>>>return_dbl(return_dbl(10))
?
>>>return_dbl(print_dbl(10))
?
```



```python

''' Mutable vs Immutable Types

- Lists in Python are MUTABLE (can change them in place)
'''
"""
# Example

L = [10, 20, 30, 40]
print(L)
L[2] = 300
print(L)

T = (10, 20, 30, 40)
print(T)
#T[2] = 300 # ERROR, tuples are IMMUTABLE
T = (10, 20, 300, 40)
print(T)

school = "UCSB"
#school[3] = "D" #ERROR, strings are IMMUTABLE
school = "UCSD"



''' Q: Why should we even care?
- It's the behavior of the language!
- Depending on whether or not something is immutable or
mutable, it affects how the data is treated when passing
it into a function.
'''

def add_to_end(s, i):
    ''' Returns a string with i appended to s '''
    s = s + i
    return s

name = "Apple"
print(add_to_end(name, "!"))
print(name)

# When immutable types are changed in a function, a local
# COPY of the data is made and used within the function.
# Once the function returns, the immutable variable
# does not change (See Chapter 3.5)

def add_to_list(L, i):
    ''' Returns a list with value i appended to it '''
    L.append(i)
    return L

someList = [2, 4, 6, 8]
print(someList)
print(add_to_list(someList, 10))
print(someList)

''' When mutable values are passed into a function,
the actual value is modified '''



```
