---
layout: lab
num: lab08
ready: false
desc: "Recursion"
assigned: 2018-12-05 8:00:00.00-8
due: 2018-12-09 23:59:59.59-8
csxx: cs8
---

In this lab, you'll get more practice with:

* Writing recursive functions
* Writing tests in pytest for your recursive functions

## This lab may be done solo, or in pairs.

Before you begin working on the lab, please decide if you will work solo or with a partner.

A reminder about working with a pair programming partner:

* Your partner must be enrolled in the same lab section as you.
* You and your partner must agree to work together outside of lab section in case you do not finish the lab during your lab time. You must agree to reserve at least two hours outside of lab section to work together if needed (preferrably during an open lab hour where you can work in Phelps 3525 and ask a mentor for help). You are responsible for exchanging contact information in case you need to reach your partner.
* If you choose to work with a partner, then you must choose a partner you have not worked with before.
* You MUST add your partner on Gradescope when submitting your work <strong>*<u>EACH TIME</u>*</strong> you submit a file(s). After uploading your file(s) on Gradescope, there is a "Group Members" link at the bottom (or "Add Group Member" under "Groups") where you can select the partner you are working with. Whoever uploaded the submission must make sure your partner is part of your Group. Click on "Group Members" -> "Add Member" and select your partner from the list.

Once you and your partner are in agreement, choose an initial driver and navigator, and have the driver log into their account.

# Instructions

In this lab, you will need to create two files:
* <tt>{{page.num}}.py</tt> - file containing function definitions
* <tt>{{page.num}}_student_tests.py</tt> - file containing test cases. A sample test is provided for each function. You will write 3 - 5 (or more) additional tests per function to confirm your code works as expected.
* <strong>Please add a comment with you and your partner's name (if applicable) at the top of each file.</strong>

Starter code is provided for you and are located at (you may need to refresh the page if the links do not load immediately):

* [{{page.num}}.py](https://ucsb-cs8-f18.github.io/lab/lab08/lab08.py)
* [{{page.num}}\_tests.py](https://ucsb-cs8-f18.github.io/lab/lab08/lab08_student_tests.py)


You will complete the portions in the starter code by doing the following:

1.  Create a directory called <tt>~/{{page.csxx}}/{{page.num}}</tt> (using the `mkdir` command) and `cd` into that directory.
2.  Use `idle3` (you might try `idle3 &` if you want to be able to type commands on your terminal window after IDLE opens).
3.  Use "New File" to create empty files called `{{page.num}}.py` and `{{page.num}}_student_tests.py` in that `~/cs8/{{page.num}}` directory.
4.  ONE AT A TIME, copy the function definitions from the starter code, write tests that go along with those functions in `{{page.num}}_student_tests.py`, and get your tests to pass.
   * Before you move on to the next function definition and <em>its</em> tests, get all of the tests you just wrote to pass.
   * Repeat this until you have ALL of the function definitions and their tests, and all of them pass.

You are encouraged to try submitting to Gradescope periodically for several reasons:

* NOTE: that you MUST use recursion to get credit.   If you get your tests to pass by using a
   method other than recursion, your points for passing the tests will be deducted during the
   manual portion of the grading.
* You can get partial credit if some of your tests pass for some of your functions.
* You will have a backup of your file in case you accidentally delete yours, or in case your laptop dies.
* You can move code between your laptop and CSIL by downloading your submitted code from Gradescope

# Upload `{{page.num}}.py` and `{{page.num}}_student_tests.py` to Gradescope.

Once you're done with writing your functions, navigate to the Lab assignment {{page.num}} on Gradescope and upload your `{{page.num}}.py` and `{{page.num}}_student_tests.py` files. <strong>*Remember to add your name, and your partner to Groups Members for this submission on Gradescope if applicable. At this point, if you worked in a pair, it is a good idea for both partners to log into Gradescope and see if you can see the uploaded files for {{page.num}}.*</strong>
