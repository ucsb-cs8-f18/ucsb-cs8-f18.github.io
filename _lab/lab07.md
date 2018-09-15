---
layout: lab
num: lab07
ready: true
desc: "Scrabble word finder: Python lists, dictionaries and file I/O"
assigned: 2017-11-21 8:00:00.00-7
due: 2017-11-28 17:00:00.00-8
submit_cs_pnum: 874
---


## You may pair or work alone on this lab.

If you choose to pair, please start by registering your pair on submit.cs in the normal way.  Go to
<https://submit.cs.ucsb.edu>, log on, navigate to the link for {{page.num}}, then follow the links to invite your pair partner to form a group.   Make sure your pair partner logs in and accepts your invitation.

## Goals for this lab

The goals for this lab are:

* more practice using Python lists
* practice using Python dictionaries
* read data (words) from a text file and put them into a list
* create a Scrabble word finder
* use list method sort() to sort words in order of descending point value
* print formatted output to the screen
* write formatted output to a file

## Getting started


* Step 1: Log on & bring up a terminal window
This is done following the steps you have performed in lab00.
* Step 2: Create a directory in your cs8 directory named {{page.num}}.
* Step 3: Start IDLE

The terminal command for this is "idle3 &".  When you have the IDLE window up, you are ready for some programming!


## What to program?

In this lab assignment, you are going to make your own Scrabble word finder function, `scrabbleWords()`.  In the end, you will simply input a string of letters and the program will print out (to the screen and to a file) a list of all the possible words you can make along with their point values in descending order (neglecting things like triple letter, double word squares, etc. in the real game of Scrabble).  For example, if I input 'bouni' as my string of letters, this is what I get:

```
>>> scrabbleWords('buoni')
obi      5
nub      5
nob      5
nib      5
bun      5
bio      5
bin      5
bi       4
uni      3
ion      3
on       2
nu       2
no       2
in       2
u        1
i        1
```

So, how did our program know which letter combinations were valid words?......We have to specify a file of words, which you can find here: [wordlist.txt](wordlist.txt){:data-ajax="false"} .  This file must be downloaded (right click and "save as") and put into your {{page.num}} directory before you begin, so do that now.  Note that this file contains a fairly complete list of English words, so beware that there may be some expletive and/or raunchy words - please don't hold me personally responsible if you are offended.  Perhaps this will be motivation for some of you to complete the assignment.  

You can choose to start from scratch or use the starter code we have provided here: <https://github.com/ucsb-cs8-f17/lab07-starter-code.git>


### Functions to Implement:

1. **createWordList(filename)** - return L
2. **canWeMakeIt(myWord, myLetters)** - return True or False
3. **getWordPoints(myWord, letterPoints)** - return points
4. **outputWordPointPairs(pointWordList, myLetters, toFile)** - NO return (just prints a formatted list or writes it to file).
5. **scrabbleWords(myLetters)** - NO return (just calls other functions)


### Function Details:

1. **createWordList(filename)** - return L.  Write a function which reads the file `filename` and returns a list `L` containing all the words in the file.  Note that the last character of every line of the file is the invisible "new line" character '\n' and needs to be sliced off.



2. **canWeMakeIt(myWord, myLetters)** - return True or False.  Write a function which answers the question: Can I form the word `myWord` from the string of letters `myLetters`?  The function should return a boolean True or False.  Converting `myLetters` to a list and using the pop() or remove() method may come in handy. You do not need to use all the letters in `myLetters`. It's possible that `myLetters` will contain multiples of the same letters. In the example above if myLetters = "buoni"  and myWord="boon" it should return False. If the input is not the correct type then return ```False``` Try to write an algorithm on paper first before attempting to write the code. Think about the list functions at your disposal and the tools you've learned up till now.


3. **getWordPoints(myWord, letterPoints)** - return points.  Write a function that calculates and returns the total point value of `myWord` given the Python dictionary object `letterPoints` which consists of letter:pointValue pairs. If a character in `myWord` is not a key in the provided dictionary then its score value is 0. If any of the input is incorrect type then return 0. Note that you do not need to create the `letterPoints` dictionary in this step - it is a parameter to our function and will be created in `scrabbleWords()`.

4. **outputWordPointPairs(pointWordList, myLetters, toFile)** - NO return (just prints a formatted list or writes it to file).

* Write a function which will output the (pointValue, word) pairs in pointWordList to the shell or to a file depending on the bool value `toFile`

* When `toFile` is ```False```,  print all the words followed by their point value.  Format the output so that your word is left justified in a field of width 4 more than the number of letters in `myLetters`, and the point value follows immediately afterwards.  You can do this with the format string method by carefully forming the '{...}' string first.  Hint: Use string concatenation with `str(len(myLetters) + 4)`.

* If `toFile` is ```True```, write the same text as your formatted screen output from above to a text file.  Name the file the string of letters contained in `myLetters` followed by .txt.  So in the example above with scrabbleWords("buoni"), the file that is created is buoni.txt.  Note that every time you want to write to a new line, you will need to include the newline character '\n' in your file.write() statement.  You can see what the output should look like in the example here: [buoni.txt](buoni.txt){:data-ajax="false"} .  Do not download this file, but simply verify that when you run your program you produce this same file.

### Putting it all together:

**scrabbleWords(myLetters)** - NO return (just calls the helper functions above).  Here you will call upon your "helper functions" created in steps 1-4 to form a list of all the words (from wordlist.txt) that can be formed from the set of letters contained in myLetters:

* Create a Python list of words from wordlist.txt and name it `wordList`.  You will want to call helper function `createWordList()`.

* Create a list of all the words that we can make with `myLetters` by looping through every word in `wordList` and checking if it can be made with `myLetters` - name this list `myWords`.  You will want to call helper function `canWeMakeIt()`.

* Create a dictionary of letter: pointValue pairs - name it `letterPoints`.  The image below shows the Scrabble point value for each letter, but note that your dictionary keys should be the lower case letters. Any character that is not shown in this image has a point value of 0. You don't have to add 0 point keys to your dictionary, rather make sure that your `getWordPoints` uses a point value of 0 if a letter is not in the provided dictionary.

![letter points](scrabble_letters.png){:height="200px"}

* Create a list of tuples consisting of (pointValue, word) pairs by looping through the list `myWords` and getting the point value for each word - name this list of tuples `pointWordList`.  To calculate pointValue, you will want to call helper function `getWordPoints()`.

* Sort `pointWordList` in descending order.  Now, you can use the list method sort() to sort the tuples according to their first entry, pointValue.  But sort() arranges a list in ascending order by default....can you think of a way to reverse this?

* Call your `outputWordPointPairs()` to output to print your formatted string output to terminal. And then make a second call to `outputWordPointPairs()` to output to a .txt file named after the string in `myLetters`.

## Write test code in lab07_student_tests.py

You must write test code using pytest for the following functions: 
* `createWordList(filename)`
* `canWeMakeIt(myWord, myLetters)`
* `getWordPoints(myWord, letterPoints)`

Write the test code before you implement the functions. This is a way of demonstrating that you understand what each function is supposed to do.

You should test the other two functions manually, although you are welcome to write test code for them as well.

Put your test code in lab07_student_test.py and submit it along with your lab07.py
This test code is worth some amount of points for this lab. We recommend writing at least 3-5 test cases per function, but feel free to write more until you're confident with your solution.

Note that the submit system will only give you a partial score (similar to lab exam 01). We will show the outcome of some of the instructor test cases but not all!

### What lab07.py should look like

```
#!/usr/bin/env python3
import pytest
import sys
"other import statements"

def createWordList(filename):
  #Your code

def canWeMakeIt(myWord, myLetters):
  #Your code

def getWordPoints(myWord, letterPoints):  
  #Your code

def outputWordPointPairs(pointWordList, myLetters, toFile):
  #Your code

def scrabbleWords(myLetters):
  #Your code

if __name__=="__main__":
  if len(sys.argv) >= 2:
	scrabbleWords(sys.argv[1])
  else:
    print("Invalid input please try again")

```
### What lab07_student_tests.py should look like

```
#!/usr/bin/env python3
import pytest
from lab07 import createWordList

def test_createWordList_0():
  #Your test code


def test_createWordList_1():
....


from lab07 import canWeMakeIt

def test_canWeMakeIt_0():
  assert(canWeMakeIt('ape','pae') == True)

...
from lab07 import getWordPoints
letterPoints = {'a':1, 'b':3, 'c':3, 'd':2, 'e':1, 'f':4,\
                'g':2, 'h':4, 'i':1, 'j':8, 'k':5, 'l':1,\
                'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1,\
                's':1, 't':1, 'u':1, 'v':4,  'w':4, 'x':8,\
                'y':4, 'z':10}

def test_getWordPoints_0():
  assert(getWordPoints('ape',letterPoints) == 5)
...
```


# Running the final product

Just like in lab04, in order to run the program from the terminal you need to include the shebang as the very first line of the file.

```
#!/usr/bin/env python3
```

After doing so, make lab07.py an executable by typing the following into the terminal.

```
chmod u+x lab07.py
```

Now you can run the program from terminal by typing or other similar commands:

```
./lab07.py buoni
```

Make sure you have this main function at the bottom of the file for this to work.

```
if __name__=="__main__":
  if len(sys.argv) >= 2:
	  scrabbleWords(sys.argv[1])
  else:
    print("Invalid input please try again")
```

you're finished!  Now have fun and experiment with the word finder ;-).

# Submission

## Navigate to the page for submitting {{page.num}}

The page for submitting {{page.num}} is here: <https://submit.cs.ucsb.edu/form/project/{{page.submit_cs_pnum}}/submission>

Navigate to that page, and upload your `{{page.num}}.py` and `lab07_student_tests.py` files.

# Submission from CSIL command line

If you are working on the ECI/CSIL/lab linux systems, you can also submit at the command line with this command:

<tt>~submit/submit -p {{page.submit_cs_pnum}} ~/cs8/{{page.num}}/{{page.num}}.py lab07_student_tests.py</tt>

Notes on using the command line version of submit:

* This ONLY works on CSIL.  From your own PC or Mac, use the web form for submission.

* The first time you use the `~submit/submit ...` command (or every time if you choose not to save your credentials) you will be asked for your email address: use your full umail address (e.g. `cgaucho@umail.ucsb.edu`).  For password, use the password that you enter for the submit.cs system.    You may save these credentials if you don't want to have to type them in every time.

* Note that if you try to upload files with names that do not match EXACTLY the names `{{page.num}}.py` and `lab07_student_tests.py` the system will not allow you to do it.   Once you upload it, you should get a page that shows your submission is pending.  Refresh that page, and you should get one that indicates with either red, or green, whether the test cases for your code passed or failed.

Thanks to Matt Buoni for this lab!
