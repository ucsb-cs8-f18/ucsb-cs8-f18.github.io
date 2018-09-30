---
num: "Lecture 2"
desc: "Elements of simple programs in Python"
ready: true
date: 2018-10-02 9:30:00.00-7:00
---


## Announcements: 

* Complete [ic00](/hwk/ic00) and bring it to your lab section tomorrow
* During the first 10 minutes of the lab, try to find a suitable lab partner 
* My office hours: Wed 3:30 - 5:00 pm (HFH 1155)

## Concept Questions

* Check your understanding: [Lect 02 Concept Questions](lect02-concept.md){:data-ajax ="false"}
* You'll need your iclickers to participate in class


## Today's lecture:

* Python as a calculator
* Storing data using variables
* More than just a calculator (working with other data types)
* Interacting with a program using `print` and `input`
 

### Python as a calculator

* Numerical data types
    - Integer representing non-decimal values
    - float: Floating point number representing a decimal
        (fractional) value
* Operations with numeric types
    - Arithmetic (+ - * /), Comparison(== < > <= >=)

* Evaluating expressions:
    - Just like writing math expressions
    - Mixed types are okay     

Numerical type examples (type these in the shell to see what happens)


```python

>>> 1

>>> 1+2

>>> 4/2

>>> 1/3

>>> 6/2

>>> 1/0

>>> 1+2*4

```
 
### Storing data using variables

* Think of a variable as a box with a name
* Just like you can store things in a box, you can store values in a variable (for now we'll only store numeric values, but you can store other types as well)
* Names of variables must...
    - Start with a letter or underscore (the former is more common)
    - Remaining letters in variables names can consist of letters, numbers,
           or underscores
    - Names are case-sensitive (name and NAME are considered two different
           variables).

```python
>>>x = 10 #What is the value of x?

>>>x = x * 10 # 10 * current value of x is stored back into x


```

### More than just a calculator
* Other data types
    - int: Integer representing non-decimal values
    - float: Floating point number representing a decimal
        (fractional) value.
    - string: Represents a collection of characters
        - Examples of characters: 'A', 'a', '1', ' ', ...
    - bool: Evaluates to either True or False
        - Ex: 4 <= 6 True
        - Ex: 1 == 2 False
    - Note: 3 and 3.0 are considered different types
        - 3 is an integer
        - 3.0 is a float
    - Python knows what type these numbers are based on
        its value.

* Numerical type examples

```python
x = 1
print(x)
print(type(x))

x = 4 / 2
print(x)
print(type(x))

y = 4 * 2
print(y)
print(type(y))

z = 4 * 2.0
print(z)
print(type(z))

x = "CS 8"
print(x)
print(x*2)

x = "8.0" # string not float
print(x) #8.0
print(type(x)) #str

print(x + 2) #ERROR
print(x + "2") # No error, uses concatenation

print(float(x) + 2) # No error, 10.0

x = "8.0" # Be careful ...
print(int(x)) #crashes

x = "8"
print(int(x))

x = "8.0"
y = "8.0"
z = "8.00"

print(x == y) #True
print(x == z) #False
print(float(x) == float(z)) #True
print(2 * 3 > 5) #True
print(type(2 * 3 > 5)) # bool

```

* Indexing strings and substrings
    - In a string, we can extract certain pieces from it.
    - This is known as "parsing" a string
    - Positions in a string start at index 0

```python
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
                       
# compute salary
hours = 40
rate = 10
salary = hours * rate
print("Salary is $", salary) # Notice quotes aren't displayed on the string in the outpout

```
 
### Interacting with a program using `print` and `input`
* When we write software, we're modeling the real world
    - ... or at least we do it as best we can
    - You can think of everything with respect to things
        and actions.
        - Things (nouns) - Objects
        - Actions (verbs) - Functions, operators, ...
    - Python (and generally all languages) gives some way
        to represent and combine these.
    - There are also ways to interact with the program
        - Generally, we call this "user input"
        - Reading files
        - clicking on buttons
        - keyboard characters
    - In order to interact with our program using text,
        Python has the input() function for us to use

```python
# Example
print("Hi, please enter your name: ")
userName = input()
print("Hello", userName)


# We use something called ESCAPE CHARACTERS to print
# special characters including quotes.

print("\"Hi!\"") # \" is the double quote characters
print("Hi\nthere\n!") # \n is the newline character


# Another larger example
TAX_RATE = 0.1
print("Hi, please enter your name: ")
userName = input()
print("Hi", userName, ". What is the amount of your bill \
(not including tax and tip)?")
totalBill = float(input()) #be careful, will crash if not float
print("What is the tip percentage you would like to leave?")
tipPercentage = float(input())
taxAmount = totalBill * TAX_RATE
tipAmount = totalBill * (tipPercentage / 100)
print("The total amount to pay is $", totalBill + taxAmount + tipAmount)
```

