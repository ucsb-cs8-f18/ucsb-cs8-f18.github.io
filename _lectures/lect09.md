---
num: "Lecture 9"
desc: "Named tuples, Nested for loops and other nested control structures"
pdfurl: /lectures/pdf/lect09.pdf
ready: false
date: 2018-11-01 9:30:00.00-7:00
---


```


''' Nested Loops
- Depending on how data is organized, it's common to see
loops within loops.
- For example, given a list of strings, we may want to
manually count how many vowels exist throughout the list
'''
'''
# Nested-for loop example
listOfStrings = ["this", "is", "a", "list", "of", "strings"]

def countVowels(strList):
    """ Count vowels in list of strings """
    vowels = "AEIOUaeiou"
    numVowels = 0
    for s in strList:   # s is an str element in strList
        for c in s:     # c is a character in s
            if c in vowels:
                numVowels += 1
    return numVowels

print(countVowels(listOfStrings))
'''

''' While Loop
- Another looping construct we'll use in this class
    - While loops are used when you want to repeat a set
    of statements indefinitely
    - Note: the number of times that goes through the
    loop is independent on the number of elements in a
    collection.
    - Examples: Web servers, OSes, ...

Syntax:
while BOOLEAN_EXPRESSION:
    STATEMENT(S)

Semantics:
- if BOOLEAN_EXPRESSION is true, perform statements in the
body of the loop
- if BOOLEAN EXPRESSION is false, skip the loop entirely
and continue execution.

- Keyword "break"
    - It's possible to exit the loop and jump out of it
    using the break statement

while True: #Loop forever - common in some UI/Game/servers
    # Somewhere in the middle, we can change our mind
    # and check to see if we want to break out
    if BOOLEAN_EXPRESSION:
        break
    ...
'''
'''
# Example:
x = 0
while True:
    x = x + 1
    print("Start of while body, x =", x)
    if x > 3:
        break
    print("End while body, x =", x)
    print("------")
print("outside of while loop")
'''
'''
- Keyword "continue"
    - It's possible to check and see if you want to
    continue executing the loop body, or go back
    and evaluate.
'''
# Example
x = 0
while True:
    x = x + 1
    print("Start of while body, x=",x)
    if x % 2 == 0: #if x is even
        continue
    if x >= 5:
        break
    print("End of while body, x=", x)
    print("------")
print("Outside while loop")
```



