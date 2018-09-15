---
layout: lab
num: lab02
ready: false
desc: "FtoC and CtoF with test cases"
assigned: 2017-08-10 09:30:00.00-7
due: 2017-08-16 17:00:00.00-7
submit_cs_pnum: tbd
---


<div style="font-size:200%; border: 5px solid red;" markdown="1">

PLEASE DON'T START THIS LAB YET!

I'm still doing major surgery on it...

</div>




In this lab, you'll practice:

* Creating a file that has some functions in it
* Testing those functions interactively at the Python prompt
* Creating a file of automatic test cases for those functions
* Running those test cases
* Submitting your functions and test cases to submit.cs for grading


# Step 1: Make a `~/cs8/lab02` folder

In previous labs, you should already have created folders `~/cs8/lab00` and `~/cs8/lab01`.  You are now going to create folder `~/cs8/lab02` for the files for this lab.

In general, its probably a good idea to keep your work for this class under `~/cs8`, in folders called `lab00`, `lab01`, `lab02` etc.     

This isn't exactly *required* (no-one is going to check), but it's probably a good habit to develop.   Here's why:
all the rest of the instructions will be written based on the assumption that you did things this way.  And if you continue to take CS courses at UCSB, you'll often find that's the case from one course to the next.   

So, I'd strongly encourage you to do it. 



# Step 2: Create a file called `tempConversions.py`

The contents of `test_tempConversions.py` should be as shown below.  This contains two Python function definitions that,
at the moment are incorrect.

Choose "File => New File" in IDLE to bring up an "untitled" window, then copy and paste this code into that window.

```

from pytest import approx

# tempConversions.py   A module for converting between fahrenheit and celsius

# The following starting point code passes some test cases, 
# but it fails others.  Your job in this lab exercise is to modify the code
# so that is passes all of the test cases

def fToC(ftemp):
      ''' convert fahrenheit to celsius '''
      return ftemp - 32.0   # TODO: Fix this line of code
  
def cToF(ctemp):
      ''' convert celsius to fahrenheit '''
      return ctemp + 32.0   # TODO: Fix this line of code
      
      
def test_fToC():
   assert( ftoC(212.0)==approx(100.0) )
   assert( ftoC(32.0)==approx(0.0) )
   assert( ftoC(-40.0)==approx(-40.0) )
   
      
def test_cToF():
   assert( cToF(100.0)==approx(212.0) )
   assert( cToF(0.0)==approx(32.0) )
   assert( cToF(-40.0)==approx(-40.0) )   
   
```



# Step 5: Try running your program again 


# Step 3: Try running this program (expecting an error...)

# Step 4: Run: `pip3 install -U pytest`


# Step 5: Try running your program again 


```
def test_fToC():
   assert( ftoC(212.0)==approx(100.0) )
   assert( ftoC(32.0)==approx(0.0) )
   assert( ftoC(-40.0)==approx(-40.0) )
   
      
def test_cToF():
   assert( cToF(100.0)==approx(212.0) )
   assert( cToF(0.0)==approx(32.0) )
   assert( cToF(-40.0)==approx(-40.0) )   
```

Then, see if you can fix the code in `tempConversions.py` so that the tests pass.

This first involves changing the line in the definition of the `fToC(ftemp)` function that says:
```Python
  return ftemp - 32.0   # TODO: Fix this line of code
```

You'll need to correct the formula.  Keep in mind that in Python:
* The `*` symbol is used for multiplication.  In algebra, we can write `1.8x` to mean `1.8` multiplied by `x`, however, this does not work in Python.  In Python you must write `1.8 * x` if you want to multiply the variable `x` by 1.8.
* The `+` and `-` symbols are used for addition and subtraction
* The `/` symbol is used for division, e.g '9.0/5.0' means nine divided by five.  Note that if both numerator and denominator are integers, in Python 2, the result will be an integer.   In this case, the result is 1 (the 0.8 part is thrown away, not rounded up to 2).

Also, the order of operations in Python is that multiplication and division are done before addition and subtraction. Some examples: 
* If `x` is 5, then `x + 2 * 3` gives us 11, not 21.  The multiplication is perfomed before the addition.
* If `x` is 16, then `x - 6 / 2` gives us 13, not 5.   The division is performed before the subtraction.
* If you want to force the addition or subtraction to be done first, you must use parentheses, e. g. `(x + 2) * 3` or `(x - 6) / 2`

When you replace `return ftemp - 32.0` with the correct formula for converting a Fahrenheit temperature to Celsius, you should leave out the comment that says `# TODO: Fix this line of code `.

You'll also want to replace the similar line in the cToF function.


## Step 3: Prepare submission for submit.cs



### Step 3a: Make a `~/cs8/lab02` folder


In previous labs, you should already have created folders `~/cs8/lab00` and `~/cs8/lab01`.  You are now going to create folder `~/cs8/lab02` for the files for this lab.



In general, its probably a good idea to keep your work for this class all in the same folder, and within that folder, create a separate folder for each lab.   This isn't exactly *required* (no-one is going to check), but it's probably a good habit to develop.   Also, the rest of the instructions will be written based on the assumption that you did things this way.  So, I'd strongly encourage you to do it. 

### Step 3b: Set up the files `tempConversions.py` and `test_tempConversions.py` in that directory.

Open up IDLE, and select "File -> New".  Copy and paste the contents of tempConversions.py into that window.  Then choose File->Save on each of those files.

### Step 3c: Click "Run" in the window that has the file test_tempConversions.py.

In the window containing the test_tempConversions.py file, select "Run" (or press F5).

You should see the same output that you saw on the cyber-dojo.org site.

If you do not, then, see if you can determine what went wrong.

Once your tests pass here, you are ready to upload your code to submit.cs

### Step 3d: Upload your tempConversions.py file to submit.cs

You only need to upload tempConversions.py to submit.cs, since the test_tempConversions.py file is already on the submit.cs server.

Here's where to upload it: https://submit.cs.ucsb.edu/form/project/459/submission

If the tests pass, you are finished!

If you have trouble, ask during class, or post your questions to Piazza.

# For further exploration

The information below is not necessarily required to do this lab, but you may find it helpful or interesting.   It contains the answers to some questions that may come up as you try to complete the lab.

## Rules for function definitions

* Every Python function definition must start with a line in this format:
** `def`, exactly like that, followed by at least one space (usually exactly one).
** the name of the function (there are certain rules for these names, including no spaces in the name).
** a list of parameters in parens.  This list my be empty.  If there is more than one parameter, params are separated with commas.


## An aside about working with real numbers

Real numbers are numbers on the number line other than integers, such as -2.5, square root of 2, pi, and so forth.  

Python treats integers such as 2, 4, 100, and -42 differently from real numbers.  This is even true when we write an integer with a decimal point; that is 100 and 100.0 are treated differently in terms of Python's "internal processing", even though they represent the same number.

Python will be precise and exact in representing integers.  However, when representing real numbers, even ones that correspond to integers such as 100.0, there is always the potential for some error.  This is a consequence of the fact that the number of bits used to represent a number is finite, but the number of real numbers in any range is infinite.  

Thati is:
* If we use 32 bits, or 64 bits, or 128 bits to represent an integer, we know precisely how many integers we can represent, and we can be sure each one has a unique, exact representation.    
* Between any two real numbers, there is an uncountably infinite number of additional real numbers.  So, no matter how many bits we use, and no matter what range of numbers we choose to represent, we cannot represent them all exactly and precisely.  Therefore representations of real numbers are always an approximation, and there is always the potential for some error.  
 
This error is usually small and insignificant--but not always.  It can cause at least two kinds of problems:
* In calculations involving many steps, small errors can accmuulate into larger, more significant errors.  Knowing about this problem and designing ways to predict and control the error is part of a topic in Computer Science and Applied Math known as "numerical analysis".   
* When we test for equality, i.e. is cToF(100.0) == 212.0, there is the possibility that the calculation on the left gives us 212.0000000001  instead of 212.0000000000.  That tiny difference could cause the test case to fail, even though the calculation is as close as we can get.

So, in general, it's risky to test for exact equality with floating point numbers. Since this is designed to be a very introductory exercise, we are glossing over that detail.    The calculations we are doing are on numbers small enough that the number of bits of precision we have is likely to give us answers precise enough that the problem will not arise.

Later on, we'll see problems where this problem *does* present itself.  We'll see that the correct practice, when working with any kind of calculation involving real numbers (as opposed to integer) is to check whether the returned value is *approximately equal* to the value expected, i.e. that the difference between the two values is less than some *tolerance*.  This *tolerance* is usually very small, for example, 0.000001, or ten to the minus 6 (which can be written in Python either as `0.000001` or in scientific notation like this: `1.0E-6`).


