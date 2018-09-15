---
layout: lab
num: lab06
ready: true
desc: "min/max, index vs. value"
assigned: 2017-11-07 8:00:00.00-7
due: 2017-11-09 17:00:00.00-8
submit_cs_pnum: 830
---

## Mid-quarter evaluations (10 points)

Please complete this anonymous evaluation during your lab section on the lab computers.
[Evaluation form](https://goo.gl/forms/Sq20AbSNdGfvb3bO2)

The form will take 10 minutes of your time. You must show the final screen of the form to a TA/tutor to get credit for filling the form

## You may pair or work alone on this lab.

If you choose to pair, please start by registering your pair on submit.cs in the normal way.  Go to 
<https://submit.cs.ucsb.edu>, log on, navigate to the link for {{page.num}}, then follow the links to invite your pair partner to form a group.   Make sure your pair partner logs in and accepts your invitation.

## Instructions

This lab proceeds in an identical fashion to lab05.  The topics are different,
but the way of working is the same.

For this lab, you will create two files:

* `{{page.num}}.py`, a file containing some function definitions
* `{{page.num}}_tests.py`, a file containing some test cases

There is starter code for each of these (.py files) at the following link:

* <https://github.com/ucsb-cs8-f17/lab06-starter-code>

I suggest you proceed as follows:

1.  Create a directory called ~/cs8/{{page.num}} (using the `mkdir` command) and `cd` into that directory.
2.  Use `idle3` (you might try `idle3 &` if you want to keep your prompt handy) to bring up idle3.
3.  Use "New File" to create empty files called `lab06.py` and `lab06_tests.py` in that `~/cs8/lab06` directory.
4.  ONE AT A TIME, copy the function definitions from the starter code, and the tests that go along with those, and get the tests to pass.
   * By one a a time, what I mean is, at your first step, copy ONLY the first function definition from  the starter code `lab06.py` and copy only the test cases from `lab06_tests.py` that go with that function definition.
   * Then, before you move on to the next function definition and <em>its</em> tests, get all of the tests from the one you just copied to pass.
   * Then, and only then, copy the next function definition and its tests into your files.
   * Repeat this until you have ALL of the function definitions and their tests, and all of them pass.
   
Note that what you are given differs from function to function: either a complete function definitions 
* In some cases you are given a function definition that is complete, but contains a bug.  In this case, you 
   need to fix the function definition.
* In some cases you are given a function definition that is correct. In this case, the code is there for you as an example&mdash;it is code that may be helpful to you in writing the other function definitions in the lab.   There is nothing you need to do other than study the code to learn how it works.
* In some cases, you are given a stub.

When you've done that, you are ready to try submitting to submit.cs for a final grade.  HOWEVER, you are encouraged to try submitting to submit.cs earlier, for several reasons:

* You can get partial credit if some of your tests pass for some of your functions
* You will have a backup of your file in case you accidentally delete yours from CSIL, or in case your laptop dies
* You can move code between your laptop and CSIL by downloading your code from the submit.cs submission
* You can ask the instructor or TA questions about your code on Piazza in a private instructor post.

# A Useful tip

As you know, this Unix shell command runs the tests in {{page.num}}_tests.py

```
python3 -m pytest {{page.num}}_tests.py
```

If you have LOTS of tests in your file, and you ONLY want to run some of them, you can use `-k string` to run ONLY the tests that contain a certain string.  For example, suppose you want to focus ONLY on the tests for `isList`.  You can run:

```
python3 -m pytest {{page.num}}_tests.py -k isList
```

Change `isList` to any function that you want, and only the tests that contain that string will be run.  The others will be "de-selected".


# Submission

### Navigate to the page for submitting {{page.num}}

The page for submitting {{page.num}} is here: <https://submit.cs.ucsb.edu/form/project/{{page.submit_cs_pnum}}/submission>

Navigate to that page, and upload your `{{page.num}}.py` file.

# Submission from CSIL command line

If you are working on the ECI/CSIL/lab linux systems, you can also submit at the command line with this command:

<tt>~submit/submit -p {{page.submit_cs_pnum}} ~/cs8/{{page.num}}/{{page.num}}.py</tt>

Notes on using the command line version of submit:

* This ONLY works on CSIL.  From your own PC or Mac, use the web form for submission.

* The first time you use the `~submit/submit ...` command (or every time if you choose not to save your credentials) you will be asked for your email address: use your full umail address (e.g. `cgaucho@umail.ucsb.edu`).  For password, use the password that you enter for the submit.cs system.    You may save these credentials if you don't want to have to type them in every time.

* Note that if you try to upload a file with a name that does not match EXACTLY the name `{{page.num}}.py`, the system will not allow you to do it.   Once you upload it, you should get a page that shows your submission is pending.  Refresh that page, and you should get one that indicates with either red, or green, whether the test cases for your code passed or failed.

