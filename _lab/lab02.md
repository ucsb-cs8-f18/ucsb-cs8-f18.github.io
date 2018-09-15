---
layout: lab
num: lab02
ready: true
desc: "More functions with test cases"
assigned: 2017-10-10 08:00:00.00-7
due: 2017-10-17 17:00:00.00-7
submit_cs_pnum: 826
---

In this lab, you'll get more practice with

* Writing functions
* Testing function with pytest
* Submitting your functions and test cases to submit.cs for grading

You will also work with a pair partner for the first time.

<div style="margin: 1em; padding: 1em; border: 1em inset red; font-size:120%; text-align:center;" markdown="1">

Pair programming for this lab is required, not optional.

If you do not have a pair partner, please do not start this lab, 
unless you have prior permission from the instructor.

</div>

# Step 0: Locate a pair partner with whom you are going to work

First, please fill out the handout, [IC01](/hwk/ic01/).   

Then, if you have already identified a pair partner to work with:
   * Compare answers and ensure that you are compatible as pair partners.
   * If so, register your pair on submit.cs
   
If you have not identified a pair partner, GO TO PHELPS 3526 where you will
be able to find others who also are partnerless.

DO NOT SIT DOWN AT A COMPUTER TO WORK ON THIS LAB UNTIL YOU HAVE A PAIR PARTNER.

Once you do, you may continue.

# Step 1: Register your pair on the submit.cs system

To register your pair in submit.cs, navigate to the page for this assignment:

<https://submit.cs.ucsb.edu/p/826/group>

You should see a {{page.num}} link.  Click that.

Then, you  should see a “Join Group” button. Click this button.  

The subsequent page will allow you to accept and reject invitations from your classmates, as well invite one of your classmates by their umail address to join your pair.

<strong>NOTE:</strong> Only UCSB <strong>umail</strong> addresses will work, since those are the email addresses linked to submit.cs accounts.

While multiple students can invite you to join a pair, the system only permits you to have one outstanding invitation at a time. You must revoke an invitation if you would like to invite someone else.

Once grouped together, both the members of a pair will be able to see all the submissions made by each partner in the pair (but only for that project), regardless of when the submission was made. 

Additional notes on pairs:

* Pairs exist only within the context of a specific programming assignment&mdash;you can be in a different group/pair for each programming assignment.

Once you've registered, you are ready to move on to the next step.

# Step 2: Fill out the last part of IC01 together, and turn it in.

The last part of [IC01](/hwk/ic01/).    is to be filled out after you've paired with someone.  It indicates when the two of you commit to working together, and gives you access to each others contact information.    After its scanned and uploaded to Gradescope, you'll have access to your working agreement in terms of when you can meet to work on the assignment (if that becomes necessary).

# Step 3: Review the ideas of Pair Programming, and "Falco's Strong Style Pairing" 

* Review with each other how Pair Programming is supposed to work.
* Make an agreement to be respectful and work together to maximize your learning benefit
* Decide whether you are going to use classic pair programming, or strong-style pairing (as discussed in lecture).
   * I recommend that you <em>try</em> strong-style pairing for at least some of your pairing experience. 
   * But ultimately, the two of you need to find the style that works best.
* Decide how often you are going to switch roles.
   * Many pairs find that once per "step" in the lab is good.
   * Others set a timer for 10, 15, or 20 minutes.

Then, choose an initial driver and navigator, and have the driver log into their account.

# Step 4: Verify that pytest is working on the machine where you plan to work.

You may choose to work on your own machine, or on a CSIL machine.  Either
way, you will need `pytest` installed.  

As in lab01, we check whether pytest is installed by doing the `import pytest` command
at the Python shell prompt.  If it returns no error message, then `pytest`
is installed.  If you get an error, refer back to
[lab01](/lab/lab01/) for instructions on installing it.

```
[cgaucho@csil-12 ~]$ python3
Python 3.4.3 (default, Aug 9 2016, 15:36:17) [GCC 5.3.1 20160406 (Red Hat 5.3.1-6)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import pytest
>>>
```

# Step 5: Make a `~/cs8/{{page.num}}` folder

The easiest way to create this is to do the following, which
will work from any directory:

`mkdir -p ~/cs8/{{page.num}}`

That form of the `mkdir` command, with the `-p` has the advantage that

* It creates the entire path of directories in case any of the intermediate
   ones don't exist (that is, it will create a `~/cs8` directory too if it
   isn't there yet)
* If the directory being create already exists, it won't complain
* Since the directory being created starts with `~`, it's an absolute
   path, and thus the command works regardless of the current directory.

Then, to get yourself into that directory, type:

`cd ~/cs8/{{page.num}}`

Again, since that's an absolute path, it works from any directory.

# Step 6: Create a file called `{{page.num}}.py` in your `~/cs8/{{page.num}}` directory

To start out {{page.num}}, write the line:

```
import pytest
```

Then, copy this function definition into your
{{page.num}}.py file.

```
def perimRect(length,width):
   """
   Compute perimeter of rectangle
   """
   return -42.0 # stub  @@@ replace this stub with the correct code @@@

   
```

Then, copy these function definitions into your file.  These are a special kind of function called a <em>test case</em>.  These particular test cases are written in the style used by the <em>pytest</em> testing framework, and they follow these rules:

1. The name of each test cases function must start with `test_` or end with `_test`.
2. Each one ends (typically) with a line of code that starts with the keyword `assert`, followed by a boolean expression.
   * If the expression is `True`, the test case <em>passes</em>
   * If the expression if `False`, the test case <em>fails</em>
3. Each test case function must have a different name (hence: `test_perimRect_1`, `test_perimRect_2`, `test_perimRect_3`, etc.)  They don't have to be consecutive numbers&mdash;we could use `_a`, `_b`, `_c` or anything really, as long as they are all different.

```

def test_perimRect_1():
   assert perimRect(4,5)==18

def test_perimRect_2():
   assert perimRect(7,3)==20

def test_perimRect_3():
   assert perimRect(2.1,4.3)==pytest.approx(12.8)

```

Finally, run the code, and ensure that you don't have any syntax errors
in your Python code.

# Step 7: Test your code by hand

Because I want to be sure that you continue to practice the skill,
test your code by hand first.

That is, select "Run Module" in IDLE, and then type in a few function calls
at the Python Shell Prompt.   Here are a few:

```
>>> perimRect(4,5)
-42.0
>>> perimRect(7,3)
-42.0
>>> 
```

Ok, so that's sort of pointless as long as we haven't fixed the function yet.  The point
is that
* you need to know how to check the value of a function call by typing it in.
* you need to see that right now, the function *always* returns -42.0, no matter what.

There is a reason for that.  We call this a "stub value".  It returns the wrong answer
*on purpose* so that we can check that all of the tests fail.   We want to see all of
the tests fail, THEN see all of the tests pass.  That's the general idea.

* We want so see them *all fail* when the function is wrong
* Then if they *pass* when the function is right, we *trust* the test.

# Step 8: Run pytest on the file so far

As a reminder, you run pytest OUTSIDE of idle, at the regular terminal
prompt.

You may find it helpful to bring up a second terminal window and use

```
cd ~/cs8/{{page.num}}
```

to get into the correct directory.  Then use:

```
python3 -m pytest {{page.num}}.py
```

You should see three test failures. If you do, then you ready to fix the code so that it works, which is the next step.

(If you need a refresher on how to interpret
the output of `pytest`, refer back to [lab01](/lab/lab01/])


# Step 9: Fixing the code for `perimRect`

So, if you have failing test cases, the thing to do is fix the code so
that the test cases pass.

Of course the formula for the perimiter of a rectangle with length $$ l $$ and width $$ w $$ is, in math notation: $$ p = 2l + 2w $$.   But you'll have to convert that into Python, and use the variables `length` and `width` to get it to work properly.   

Once you have the code correct, try testing both using interactive testing as well as by running `pytest`.

# Step 10: Submit your partially completed work to submit.cs

You are by no means finished with this lab.   But, we want to encourage you to make
a submission to submit.cs now anyway.  Here is why:

1.  It will be a way that you can share your work in progress with your pair partner.
    Both of you will be able to login to submit.cs and access the file you uploaded.
    
    That way, if later on, one of you is unavailable, the other can continue the work.

2.  It provides a backup copy of your work in case something goes wrong with your
    computer or your CSIL account.
    
3.  It provides a staging ground for you to move your file between your laptop and CSIL.

4.  You also will be able to see some progress towards completion of the lab&mdash;
    partial credit for completion of this step.

To submit your file to submit.cs, you can visit this page:

<https://submit.cs.ucsb.edu/form/project/{{page.submit_cs_pnum}}/submission>

Navigate to that page, and upload your `{{page.num}}` file.

Or, if you are working on the ECI/CSIL/lab linux systems, you can also submit at the command line with this command, provided you are in the correct folder/diretory:

<tt>~submit/submit -p {{page.submit_cs_pnum}} {{page.num}}.py</tt>

If you have done the steps so far, you should be able to earn 40/100 points:

* 20 for having a python file that compiles called `{{page.num}}.py`
* 10 for passing the test cases that you yourself put into the file (you get to see these);
* 10 more for passing instructor supplied test cases (these, you do not get to see,
   but in this particular case, they are exactly the same as the ones you were given to
   type in.)

Once you've submitted and you see that you have 25/100 points, you are ready to
continue with the rest of the lab.

# Step 11: Read these instructions about how the rest of the lab will work

In each of the steps that remain, you will add an additional function definition,
and some test cases.

You should try to make the function pass the test cases that you put in.

In some cases you'll be given the test cases.  In other cases, you have to supply
these test cases yourself.

At each step, you should first try to get the test cases to pass by running
pytest at the Unix command line as shown.

* Please do this BEFORE submitting to submit.cs
* Please DO NOT submit to submit.cs without testing locally first

Once you see that they are passing, THEN submit a version to submit.cs to see
if you also pass the instructor test cases for that step.

If you do, proceed to the next function definition and set of test cases.

If you pass your own tests, but NOT the instructor supplied tests, then try to
see if you can figure out why.  Is there some case that you did not consider?
The problems may have hints.

You can also ask questions on Piazza. This is a good situation to use a "private
post" to the instructors.  We can see your submissions on submit.cs,
so you don't have to share your code with us--just tell us your name, which lab you are
working on, and which step you need a hint for with instructor tests not passing.

Once you understand all how this is going to work, you are ready to start coding
the additional functions.

# Step 12: Write an `areaRect` function and some test cases for it

Now, add the definition of a function called `areaRect`.

It should have two parameters, length and width, and return the area.

Although it is tempting to write the function correctly from the start,
since the definition is SO easy, I encourage you to follow the practice
of initially putting in a stub such as the following, so that you can
"test the test":

```
   return -999
```

In addition, define three test cases.

The code for the first two test cases should look like this:

```

def test_areaRect_1():
   assert areaRect(3,4)==12

def test_areaRect_2():
   assert areaRect(0.5,0.4)==pytest.approx(0.2)


```

The third test case should be one that you come up with yourself. The restrictions are that it must be:

* a function called `test_areaRect_3`
* it should have an `assert` statement
* the assert keyword should be followed by a call to `areaRect` with some other argument values, different from the ones in the first two test cases, followed by a test for equality operator `==`, and the value that you expect `areaRect` to return for those argument values

Please write this third test case.

Then:

* test your code with "Run Module" to make sure it compiles ok (i.e. no red error messages)
* use `python3 -m pytest {{page.num}}.py -k areaRect` to run just the test cases for the `areaRect` function (there should be three of them, and three skipped test cases)
* some should  fail (because you have a stub value, -999)
* finally, replace the code in the function definition for areaRect with the correct code, and see all the tests pass.

Then, submit to submit.cs again, and you should see that you get 20  more points toward
your maximum possible score of 100.


# Step 13: Write an `isString` function and some test cases for it

Here is an example of a function that tests whether something is a list or not.


```
def isList(x):
   """
   returns True if argument is of type list, otherwise False
   """
   
   return ( type(x) == list )   # True if the type of x is a list
```

Your job is to write a similar function that takes a parameter `x` and returns
`True` if `x` is a string (type `str` in Python), and returns `False` if it is
not a string.

Here's a stub for that function.  Add it into your {{page.num}}.py file.

```
def isString(x):
   """
   returns True if argument is of type str, otherwise False
   """
   
   return "stub" 


```

And here are three test cases. Add those also:

```
def test_isString_1():
   assert isString("UCSB")

def test_isString_2():
   assert not isString(42)

def test_isString_3():
   assert not isString(["UCSB"])
```

Then, add two more test cases, following the examples above. Those
test cases should be functions named `test_isString_4` and
`test_isString_5`.  One of those should check something that you think
*is* a string, and one more that you think checks something that is
*NOT* a string.   Try to come up with different test cases than the ones given.

Finally, go through all the same steps that you did before:

* make sure the file compiles ok
* test with `pytest` and see some of the tests fail
* fix the function and see the `pytest` tests pass

As a reminder, you can use `-k blah` to run only the tests that have `blah` in their name&mdash;for example, for this step, you'd use:

```
python3 -m pytest {{page.num}}.py -k isString
```

Then finally, try submitting to submit.cs and see if you get the credit for the tests for this function.  You should be able to get up to 80/100 at this step.  When you do, keep going&mdash;you are almost at the finish line.


# Step 14: Write an `isNumber` function and some test cases for it

Our last function is one called `isNumber` that should take a parameter `x` and return
`True` if the value `x` refers to is either of type `int` or of type `float`.  In any other case, it should return `False`.

You should write the function definition, and you should write exactly five test cases,
with function names:

* `test_isNumber_1`
* `test_isNumber_2`
* `test_isNumber_3`
* `test_isNumber_4`
* `test_isNumber_5`

Follow the model from earlier.

Test your code with:

```
python3 -m pytest lab02.py -k isNumber
```

Then test your code by submitting to submit.cs.


# Step 15: See perfect score on submit.cs; profit.

At this point, you should see that you have a perfect 100 points on submit.cs, and
you are finished with the lab!

EDIT: You will only see 20/20 points. The remaining 80 points will be graded by the TAs and final scores will be posted on Gauchospace. 
