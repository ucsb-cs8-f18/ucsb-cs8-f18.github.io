---
num: "Lecture 3"
desc: "Python functions, testing with pytest"
ready: true
date: 2017-10-09 1:30:00.00-7:00
---

# Resources from lecture

* [Link to all code written in lecture](https://github.com/ucsb-cs8-f17/cs8-f17-lecture-code)

* [Link to lecture slides and peer instruction questions](https://drive.google.com/drive/folders/0BxIvQwpl4ocoRy1Pa041SThLUFU?usp=sharing)

* [Guidelines for using peer instruction - thanks to Dan Zingaro](https://drive.google.com/file/d/0BxIvQwpl4ocoX2ZpUjJDZW52Wlk/view?usp=sharing)

# Announcements

* lab01 and lab02 are now ready for you to work on it.
* Eventually, we'll explain how to work on labs on your own computer.
   * If you want a head start on that, come to office hours with your laptop, and we'll go over it with you.


   
# Python Functions

* Functions are the basic building blocks in your program. If your program were a house, then functions would be the doors, windows, piping, roof and every other part of the house that can be descibed in an 'abstract' way. In other words, a FUNCTION is an abstraction for some piece of computation/work in your program. 

* For now, we will focus on the general concept of a function. In the next lecture we will see how you can describe a program as a collection of functions


## Defining functions

* In general a function takes an input (or a set of inputs), computes something (using the inputs) and gives us back a value. In math, for example, 

f(x) = x<sup>2</sup>

The same function in Python would be DEFINED as follows - beware of details related to syntax

```
def f(x):
    return x**2

```
- What is f(2)? How about f(3)?

The above function definition demonstrates the following important rules related to writing any function:

* Start with the keyword `def`. This tells Python we are about to define a new function
* `f` is the name of the function. 
* The name of the function is immediately followed by a pair of paranthesis
* The INPUT variables are placed inside the paranthesis. In this case our function takes only one input (variable x which is expected to be a number)
* The input 'x' is also known as the parameter of the function. It is only visible from within the function
* The `:` is part of the syntax and tells Python: what follows is the sequence of instructions that describe the computation performed by the function. These instructions are also known as the body of the function
* Note that each instruction within the body must be indented using a single tab - Python is strict about indentation.
* `return` is a keyword that terminates the function and tells Python you are about to compute the value that the function will return: in this case its an expression that evaluates to square of x
* When you define a function and run your code, nothing really happens except Python gets to know that your function exists. The actual code within the function is only executed when you CALL the function

- Exercise 1: Code up f(x) 

## Calling functions

Once we have defined the function f(x), we can CALL it as many times as we like to compute the square of any number. To do that type the following at the Python shell:

```
>>f(10)
>>f(3.0)
>>f("CS8") # Error "CS8" is a string because the ** operator is not defined on strings
```

* When we call the function, we pass a value to the parameter of the function e.g. 10 or 3.0 or "CS8". This value is stored in the parameter in this case the variable x and Python starts executing the instructions in the body of the function using that specific value of x until it either reaches the terminating "return " or the reaches the last statement of that function.
* When the function has finished executing, we get the return value wherever the function was called
* You may either print that value such as `print(f(10)) or store it in another variable such as `y = f(10)`. In general: the function call is replaced by its return value


- Exercise 2: Code a few other functions and call them: 
* times(x,y) - returns x times y
* answerToLife() - returns 42 


```
>> times(4,5)
>> times(8.7*2.3)
>> times("CS8",3)
```

Main points from coding exercise:
* a function may have multiple parameters or none at all
* The type of the function parameter is determined when the function is called

- PI questions

## Example worded problem

Given two points p1 and p2 in 2D Cartesian coordinates, find the Euclidean distance between them


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



## Lab01 Warmup--experiencing floating point inaccuracy

* Review from lab01 writeup
* Never compare two floating point numbers using equality (==). Instead use pytest.approx
* Command to run your code using the pytest framework from the command line

```
python3 -m pytest funcs2.py
```


## Good coding style tips

Add a desription of what the function does:
```
def f(x):
    '''
    Returns the square of the input x
    '''
    return x**2

```

* Normally its good practice to add some text that describes what the function does. These are enclosed within a pair of triple quotes - also known as the docstrings. The docstrings is not really code just additional info about the function

* In general you should always use a meaningful name for your function. A better name for the function f(x) would have been `computeSquare`. Stylize the name of your functions in [Camel Case](https://en.wikipedia.org/wiki/Camel_case)


















