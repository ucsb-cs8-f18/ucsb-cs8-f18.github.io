---
num: "Lecture 6"
desc: "Creating your own modules, Python Testing, Unix command line basics"
pdfurl: /lectures/pdf/lect06.pdf
ready: true
date: 2018-10-16 9:30:00.00-7:00
---


''' Python Testing '''

# Software testing is essential to ensure behavior works
# as expected.

# Assert statements can be scattered throughout your code
# If an assert statement fails (i.e. not True), then
# your program execution terminates.

"""
print("1st line")
assert 3 == 3 # Test passes, resumes execution.
print("2nd line")

def double(n):
    ''' Returns 2 * n '''
    return 2 * n

assert double(5) == 10
assert double(-2) == -4
assert double("UCSB") == "UCSBUCSB"
"""

'''pytest is a formal testing framework for python'''
def double(n):
    return 2 * n

def test_double_5():
    assert double(5) == 10

def test_double_negative():
    assert double(-2) == -4

def test_double_list():
    assert double([1,2]) == [1,2,1,2]

def test_double_string():
    assert double("UCSB") == "UCSBUCSB"

''' running pytest on functions that start with "test_" and have
an assert statement will "automate" execution of all tests and
show which ones passed and which ones failed.

- Important since this ensures software is working as expected if
many people try to modify the code at the same time
'''

''' import vs. from '''
- Not much of a difference behind-the-scene, but affects naming.

# "import" Example:
import math # gives us access to functionality in the math library

print(math.sqrt(4)) # how to use a math library function.

# "from" Example:
from math import sqrt

print(sqrt(4)) # no need to use "math." when calling sqrt function

'''
- We can "import" our own code in a file using the file name without
the ".py" extension.
- Good for organizing our code in a modular fashion.
	- Can organize all tests within a file and import functionality
	into the file running the tests.
'''

# The `if __name__ == "__main__"` block
<https://ucsb-cs8.github.io/ptopics/main_blocks/>

## Designing functions using Test Driven Development

Its usually too messy to test your functions by repeatedly calling them in the python shell. We will use the pytest framework to automate this process (just like professional programmars)
* Set up pytest - see lab01 writeup

* Step 1: Write a few examples of the function call
* Step 2: Write the type contract which specifies what type of inputs the function accepts and what type of insputs it returns
* Step 3: Write a stub function (only the header and a return statement that returns the right type, no implementation)
* Step 4: Using the examples of the function call from step 1, write test code that checks for equality between the expected output of the function and what it actually returned by the function for a specific set of inputs. For our example problem if you don't have a solution that works for all points in 2D, try to solve the 1D problem first and slowly progress towards a solution
* Step 5: Run the test code and see it fail
* Step 6: Add code to your function to pass the test cases, run the code and modify until the test cases pass
* Step 7: Repeat Steps 4 - 6 until you feel confident about your implementation

```