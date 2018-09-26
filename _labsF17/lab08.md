---
layout: lab
num: lab08
ready: true
desc: "Recursive functions"
assigned: 2017-11-28 8:00:00.00-7
due: 2017-12-02 17:00:00.00-8
submit_cs_pnum: 904
---

## Learning Goals
* Solve problems using recursion
* Determine the base case and recursive step in a recursive solution.
* Learn to reason about your program, and justify its correctness.
* Find and fix errors in simple Python functions.
* Reason about the quality and completeness of test cases.

This lab may be done individually or in pairs
## Getting started

* Step 1: Log on & bring up a terminal window
* Step 2: Create a directory in your cs8 directory named {{page.num}}.
* Step 3: Bring up idle and create two new files called `{{page.num}}.py` and `{{page.num}}_student_test.py` in your ~/cs8/{{page.num}} directory. The first file should contain your implementation and the second should contain test code using the pytest framework.
* Step 4: For each of the programming exercises in this lab come up with a solution outline by discussing with your partner. Don't be in a hurry to start coding unless you have a fairly clear idea of a solution strategy.

**Note: All your solutions must use RECURSION**

## Multiply without the `*` operator

In `{{page.num}}.py` file create a stub for the function `recProduct` that takes two integer arguments `a` and `b` and returns the product of the two numbers. Your task is to implement this function without using the * (multiply) operator, only + (addition) and RECURSION instead of loops. Your program should work for positive, and negative values of `a` and `b`.

Before implementing the function, work on developing an algorithm.
For starters, consider the case where `b` takes only non-negative values and `a` may be positive, negative or zero. Recognize that:

```
a * b = a + a + a + ... + a (with b copies of a added together)
```

E.g.,

```
3 * 4 = 3 + 3 + 3 + 3
```

The above describes a form of the solution that does not use the multiply operator just the '+' operator. The next step is to write the recursive form of your solution.

Just for practice, take a minute to (a) determine the base case and (b) write the recursive step without looking below.  After you've got it, read on. If you don't know where to ask, please ask for help. Scroll down when you have an answer.


<div style="margin-bottom:32em">
</div>


Your base case probably looks something like:

```
a * 0 = 0
```
That is, when b is 0, then the product of 0 times any number is 0.

Your recursive step should be something like:

```
a * b = a + a * (b-1)
```

In a recursive implementation, you must have (1) a base case (2) a recursive case where the * operator in the expression `a + a * (b-1)`
is replaced by a call to the very function you are implementing: `recProduct`

Now, implement your `recProduct()` function. Once you have that, its time to test you code. Using the pytest framework, test your code for some typical inputs. Add your test code to `{{page.num}}_student_tests.py`

For example check that your program does the following:


`recProduct(0,5)` returns 0

`recProduct(1,5)` returns 5

`recProduct(-1,5)` returns -5

<div style="width:80%; margin-left:auto; margin-right:auto; background-color: #efe; border: 5px inset #3f3;" markdown="1">

## A Useful tip from lab06

As you know, this Unix shell command runs the tests in {{page.num}}_student_tests.py

```
python3 -m pytest {{page.num}}_student_tests.py
```

If you have LOTS of tests in your file, and you ONLY want to run some of them, you can use -k string to run ONLY the tests that contain a certain string. For example, suppose you want to focus ONLY on the tests for recProduct. You can run:

```
python3 -m pytest {{page.num}}_student_tests.py -k recProduct
```

Change recProduct to any function that you want, and only the tests that contain that string will be run. The others will be “de-selected”.

</div>

Once you have tested your code for the cases where the parameter `b` is non-negative, while `a` is any integer (positive, negative or zero), try to write a few additional test cases where the parameters `b` is negative. Here are a few example cases:

`recProduct(5,-1)` should return -5

`recProduct(-5,-1)` should return 5

Implement the logic needed to handle the case where `b` is negative in order to pass the additional test cases.

## Check if a string is a palindrome  
In `{{page.num}}.py` file create a stub for the function `isPalindrome` that takes one string as argument and returns `True` if the string is a palindrome and `False` otherwise. You should also return `True` if the string is empty. Assume that your input is just a single word with no spaces. Your solution MUST use recursion.

A palindrome is a sequence of characters which reads the same backward as forward, such as 'madam', 'racecar' or 'detartrated'.  You must ignore the case of the characters when comparing them, so your function should return `True` for the word 'raCecaR'

Add test cases to test `isPalindrome()` in `{{page.num}}_student_tests.py`. Then implement your function.  Just like the previous problem, remember that you need to first write the base case that returns the correct value for the smallest possible input, which may be an empty string or a string with just one letter. This is known as the 'base case'. You then need to write the recursive case. The recursive case describes your problem in terms of itself (but on a smaller input size). In this case, your function not only calls itself but also makes progress towards the base case.



# Submission

Great job working through {{page.num}}!

## Navigate to the page for submitting {{page.num}}

The page for submitting {{page.num}} is here: <https://submit.cs.ucsb.edu/form/project/{{page.submit_cs_pnum}}/submission>

Upload your `{{page.num}}.py` and `{{page.num}}_student_tests.py` file.

# Submission from CSIL command line

If you are working on the ECI/CSIL/lab linux systems, you can also submit at the command line with this command:

<tt>~submit/submit -p {{page.submit_cs_pnum}} ~/cs8/{{page.num}}/{{page.num}}.py {{page.num}}_student_tests.py</tt>

Notes on using the command line version of submit:

* This ONLY works on CSIL.  From your own PC or Mac, use the web form for submission.

* The first time you use the `~submit/submit ...` command (or every time if you choose not to save your credentials) you will be asked for your email address: use your full umail address (e.g. `cgaucho@umail.ucsb.edu`).  For password, use the password that you enter for the submit.cs system.    You may save these credentials if you don't want to have to type them in every time.

* Note that if you try to upload a file with a name that does not match EXACTLY the name `{{page.num}}.py`, the system will not allow you to do it.   Once you upload it, you should get a page that shows your submission is pending.  Refresh that page, and you should get one that indicates with either red, or green, whether the test cases for your code passed or failed.





Adapted from SPIS-2016 (UCSD)
