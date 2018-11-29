---
num: "Lecture 15"
desc: "More Dictionaries and Sets"
pdfurl: /lectures/pdf/lect15.pdf
ready: true
date: 2018-11-29 9:30:00.00-7:00
---

```
# CS 8

# Simple way to get key / value
for x in D:
    print(x) # Prints the keys
    print(D[x]) # Prints the values
'''
''' Restrictions on using Dictionaries
- Keys must be an immutable type (int, str, namedtuples, - not
lists for example).
- Values can be anything (mutable or immutable objects)
- For our purposes, KEYS are UNIQUE. Don't define something like
{'Joe':17, 'Joe':18}.
- Python is actually OK with duplicate keys and it will return
the last key/value in the dictionary.
- Again, for our purposes, we should never use duplicate key
values (kinda defeats the purpose of dictionaries).
'''

''' dictionary methods
    D.pop(key) # remove and return the value
    D.update(D2) # combine values in D and D2
    D.get(key) # returns item if it exists. If not, returns None or a default value
    D.keys() # dict_keys([ LIST OF KEYS ])
    D.values() # dict_values([ LIST OF VALUES ])
    D.items() # dict_items([ LIST OF KEY,VALUE ])
'''
'''
value = D.pop('John')
print(D)
print(value)
D.update({'Jess':25,'Jerry':27})
print(D)

# What if something is not in the dictionary and we try to access it?
#print(D["CS8"]) #ERROR - "CS8" key doesn't exist.
print(D.get("CS8"))

# Can define the default return value if key doesn't exist
print(D.get("CS8", "not in dictionary!"))

print(D.keys())
print(D.values())
'''
'''
for item in D.keys():
    print(item)
'''
'''
keys = D.keys()
#print(keys[2]) # ERROR - Not a list!
print(list(keys)[2]) # OK
'''

# Example of adding to a dictionary
D = {}
print(D)
D['CS8'] = "UCSB"
print(D)
D['CS16'] = "UCSB"
print(D)
'''

''' SETS: Like a mathematical set
- A collection of items with:
    - no duplicates
    - order and position does not matter
- Useful for certain problems
    - Keep track of unique items (active IDs, SSN, Driver's License)
- Under the hood, similar to the implementation of dictionaries
    - Uses hashing to map a set's value to a particular index
        - Instant lookup times (better than "walking down" the
        collection until you find the item).
Syntax:
{<value1>,<value2>,...,<valuen>}
'''
s = {1,2,3,4}
d = {'a':1, 'b':2}
print(type(s))
print(type(d))

empty_set = set()
empty_dict = {}
print(type(s))
print(type(d))

# create a set from a list
s2 = set([2,4,6,6])
print(s2)

# common set operators:
# in, not in

print(3 in s2)
print('a' in d) # also works for dictionary keys
print(5 not in s2)
print(len(s2))

# Combine values from two sets:
s3 = set([4,5,6])
combined_set = s2 | s3
print(combined_set)

# Get the common elements from two sets:
intersecting_set = s2 & s3
print(intersecting_set)

# Remove elements of a set from another set
difference_set = s2 - s3 # {2} Removes the elements of s3 from s2
print(difference_set)
difference_set = s3 - s2 # {5} Removes the elements of s2 from s3
print(difference_set)
# order matters!

# Get unique items in two sets
symmetric_difference_set = s2 ^ s3
print(symmetric_difference_set)


s2 = set([2,4,6])
s3 = set([4,5,6])

# Set comparisons
print(s2 == s2)             # True
print(s2 == s3)             # False
print(s2 != s3)             # True
print({1,2} < {1,2,3})      # True, < indicates "proper" subset
print({1,2,3} < {1,2,3})    # False
print({1,2} > {1})          # True
print({1,2,3} > {1,2})      # True
print({1,2,3} >= {1,2,3})   # True
print({1,2,3} >= {2})       # True , <= indicates a subset

print({1,2,4} == {2,1,4})   # True , order doesn't matter

# Set methods:
s2.add(100)
print(s2)
s2.add(100) # Doesn't add duplicates
print(s2)
s2.remove(2)
print(s2)
#s2.remove(10101) # ERROR, 10101 does not exist
s2.discard(10101) # same as remove, but doesn't crash if not there
s2.clear()
print(s2)


```