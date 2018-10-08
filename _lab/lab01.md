---
layout: lab
num: lab01
ready: true
desc: "Turtle Graphics: Basic shapes"
assigned: 2018-10-10 08:00:00.00-7
due: 2018-10-16 23:59:00.00-7
csxx: cs8
---


Goal
====

The goal of this exercise is to practice with Turtle Graphics in
Python by producing some functions that draw particular shapes.

This is a warmup for a more detailed drawing lab that comes later.


What you'll be drawing
----------------------

You'll be writing functions to produce two basic shapes: a rectangle and a triangle. Each function takes parameters that specify the size, pen color, and fill color of that shape. The `drawRectangle` function additionally allows us to specifiy the tilt of the rectangle relative to the x-axis in degrees. The function definitions are given below:

-   `drawRectangle(t, width, height, tilt, penColor, fillColor)`
-   `drawTriangle(t, side,  penColor, fillColor)`

The parameter `t` is a turtle that is used in that function to draw something.

The output produced when each function is callled with specific parameter values is shown in the following figure.

![basicShapes](basicShapes.png){:height="300px"}

The above drawings are the result of calling either <code>drawRectangle(...)</code> or <code>drawTriangle(...)</code>. In each drawing, the turtle stamp shows the initial location and heading of the turtle right before the corresponding function is called. For example the top left drawing is the output of the following line of code, when the turtle named `chris` is at the top left corner:

```
drawRectangle(t=chris, width = 50, height = 100, tilt = 0, penColor = "red", fillColor = "")
```

The subsequent three drawings on the same row are the output of repeatedly moving the turtle to the right, and calling the <code>drawRectangle</code> function changing the tilt, penColor and fillColor. The function calls and parameter values to produce these drawings are given below:


```
drawRectangle(t=chris,  width = 50, height = 100, tilt = 20, penColor = "green", fillColor = "yellow")
...
drawRectangle(t=chris, width = 50, height = 100, tilt = 60, penColor = "blue", fillColor = "blue")
...
drawRectangle(t=chris, width = 50, height = 100, tilt = 90, penColor = "red", fillColor = "red")

```

Similarly, the drawings on the next row are the result of repeatedly calling **<code>drawTriangle()</code>** with the following parameter values (in each case, the `t` parameter which is the turtle is named `chris`):

|   <code>side</code>   |    <code>penColor</code> |  <code>fillColor</code> |   
|-----------------------|-------------------------| ------------------------| ----------------------- |
|   30                  |     <code> "red" </code>  |  <code> ""</code>       |
|   40                  |     <code> "green" </code>|  <code> "yellow"</code> |
|   50                  |    <code> "red"</code>   |  <code> "red"</code>    |
|   100                  |     <code> "blue"</code>  |  <code> "blue"</code>   |


In a later project, we will use these functions to create more interesting drawings. 

# The programming part

## Step 1: Create a {{page.num}} directory under your {{page.csxx}} directory

Create a directory called <tt>~/{{page.csxx}}/{{page.num}}</tt> for a file
we are going to call `drawings.py`.

To do that, use the commands below.

(Just like last week, your prompt may not be exactly like the one shown here.  Instead of `-bash-4.2$ `, you might have something like `[cgaucho@cstl-15 ~]$ `.    The `cgaucho` here is your username, the `cstl-15` is where you are logged in, and the `~` is your current directory.    Don't be distracted by this detail.)


<div style="white-space: pre; font: fixed;" markdown="1">
-bash-4.2$ <strong>cd</strong>
-bash-4.2$ <strong>pwd</strong>
/<em>cs</em>/<em>student</em>/<em>yourusername</em>
-bash-4.2$ <strong>cd {{page.csxx}}</strong>
-bash-4.2$ <strong>pwd</strong>
/<em>cs</em>/<em>student</em>/<em>yourusername</em>/{{page.csxx}}
-bash-4.2$ <strong>mkdir {{page.num}}</strong>
-bash-4.2$ <strong>cd {{page.num}}</strong>
-bash-4.2$ <strong>pwd</strong>
/<em>cs</em>/<em>student</em>/<em>yourusername</em>/{{page.csxx}}/{{page.num}}
-bash-4.2$
</div>

## Step 2: Open `idle3` and create `drawings.py`

Open up `idle3` and select the menu option `File => New File` to create a new file.

In this file, put this code (but put your name instead of "your name goes here"). Do not copy and paste the code, instead type it out.

```
# drawings.py, your name goes here
import turtle

if __name__=="__main__":
    chris = turtle.Turtle()

```

If you need a reminder about what the `if __name__=="__main__":` part does, you can visit [this page for an explanation](https://ucsb-cs8.github.io/ptopics/main_blocks/).

You can name your turtle anything you like; I used `chris` because it's a nice name.

Optionally, you can make your turtle look like a turtle by typing this (the third line is the new one that makes it look like a turtle):

```
if __name__=="__main__":
    chris = turtle.Turtle()
    chris.shape("turtle")
```

And you can set your turtle to move at the fastest possible speed on the screen - which will help make your drawings as quickly as possible.

```
    chris.speed(0)
```
Also, you can change the pen width to make your drawings look more prominent

```
    chris.width(4)
```

To move the turtle forward by say 100 pixels add the line: 

```
    chris.forward(100)
```

Save this, and run it.   You should see a horizontal line with a turtle at the final position of chris. 


## Step 3: Create a function for drawing a rectangle

Next, you are going to define a function to draw a rectangle. Your final function will be named `drawRectangle` but before you implement that, read and try out a couple of different versions of that function with simpler specifications. 

Below is the first version of the function. It doesn't take any parameters, instead it draws a rectangle with a fixed width (50), a fixed height (100), a fixed orientation (0 degrees with respect to the x-axis). To write the code we should first come up with a plan, a sequence of steps or algorithm (CS speak). Here is a very simple algorithm: Orient the turtle to point right at 0 degrees with respect to the x-axis. Move the turtle forward by 50 units, turn the turtle left by 90 degrees, move the turtle forward by 100 units, turn left 90 degrees, move forward by 50 units, turn left by 90, move forward by 100...(we are repeating ourselves, but that's fine for now. In later labs we will express the same algorithm in a more concise way). Here is the code that does what we just described: 

```
def drawRectangle_1(t):
    """
    Draw a rectangle with width 50 and height 100. Use a turtle called t to create the drawing
    Note that the parameter is called t; t stands in place of whatever turtle was passed in.
    """
    t.seth(0)        # Set the initial orientation of the turtle to 0 degrees
    t.forward(50)    # Move the turtle forward by 50 units in the direction that it was pointing
    t.left(90)       # Turn the turtle left by 90 degrees relative to the direction it was pointing
    t.forward(100)   # Move the turtle forward by 100 units
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(100)
    t.left(90)       # Make sure the turtle is oriented back to its initial orientation
    
```

Add this function to your <tt>drawings.py</tt> file, right before the `if __name__=='__main__':` block, NOT indented inside it.

After entering the function definition, at the bottom try a sample function call (`drawRectangle_1(chris)`).  Put this code inside the `if __name__=='__main__':` block, indented with the other code, like this:


```
if __name__=="__main__":

    chris = turtle.Turtle()

    chris.shape("turtle")
    chris.speed(0)
    chris.width(4)
   
    drawRectangle_1(chris) #replace chris.forward(100) by this line
   
```


Try running it and see if the rectangle looks ok.  Change the first line: `t.seth(0)` to `t.seth(90)`. Save and run your code again. What changed?

(Hint: `seth` is not the name "Seth", but actually an abbreviation for "set heading".)

We will now update our `drawRectangle_1` function definition to draw a rectangle with a green boundary and yellow interior. To do that, write the following statement before the very first line in the body of the function:

```
  t.color("green", "yellow") # Sets the pen color to green and fill color to yellow
``` 

The first parameter is the pen color and the second is the fill color. To actually fill the rectangle with the specified color, you must precede the code that draws the rectangle with `t.begin_fill()` and follow it with `t.end_fill()`. Below is the complete code. Save and run it. 

```
def drawRectangle_1(t):
    """
    draw a rectangle with width 50, height 100, tilt 0, pen color green and fill color yellow. Use a turtle called t to create the drawing
    """
    t.color("green", "yellow")
    t.seth(0)        # Set the initial orientation of the turtle to 0 degrees
    t.begin_fill()   
    t.forward(50)    # Move the turtle forward by 50 units in the direction that it was pointing
    t.left(90)       # Turn the turtle left by 90 degrees relative to the direction it was pointing
    t.forward(100)   # Move the turtle forward by 100 units
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(100)
    t.left(90)       # Make sure the turtle is oriented back to its initial orientation
    t.end_fill()
```

Save and run it. Then call the function from the Python shell as follows.  

```
>>> drawRectangle_1(chris)
```

This is just one possible solution. As you continue through this course, you will soon discover that there are many different ways to solve any problem. Computer Scientists almost always care about *correct* solutions that run the fastest on any computer - in fact there is a whole field within CS dedicated to finding such solutions - its the field of algorithms. Good programmers take a lot of care to express their algorithms in code in the simplest and most understandable way. We will strive towards this goal in general. For now, our goal is to come up with correct solutions.

Think of an alternate solution and discuss it with your lab partner. You don't have to implement it, but it you do, define a new function drawRectangle_2(t) and put your implementation within that function.

## `drawRectangle_1(chris)` vs.`def drawRectangle_1(t):` 

Note again: we use `chris`, the name of an actual instance of a `Turtle` object when we are *calling* the function.

We use `t`, a variable that refers to an "abstract" turtle when we *define* the function.  The variable `t` stands for "whatever *actual* turtle we pass in when we *call* the function".   

Refer to the [turtle documentation](https://docs.python.org/3.6/library/turtle.html) to understand all the commands we have used so far and possible alternatives to them (like `t.goto()`)

## Step 4: Implement a `drawRectangle` function that is reusable

Now, we want to make sure that we implement a function for drawing a rectangle that is general enough:

* at different heights, widths and orientation
* with different pen and fill color


What you need to do is to write the final version of this function that takes 5 parameters as shown below:

```
def drawRectangle(t, width, height, tilt, penColor, fillColor):
    """
    draw a rectangle with a given width, height, penColor and fillColor,
    with the current location of the turtle being the 
    lower left corner, and the bottom side tilted by an angle tilt (specified in degrees)
    relative to the horizontal axis. After the rectangle is drawn, the turtle should return to its original position with an orientation of 0 degrees with respect to the x-axis.
    Use a turtle called t to create the drawing
    """

    pass   # remove this line and replace with code to draw the rectangle

```

We want to be able to use this function like this, with a turtle named `chris`:

```
drawRectangle(chris, 50, 100, 0, "red","")
```

Or like this with a turtle named `taylor`:

```
drawRectangle(taylor, 100, 50, 30, "blue","green")
```

Write the above code below the previous function definition. You may use the code for the previous version as a starting point.

Next we want to draw two rectangles at different locations. To make sure that you can do that, change the function call
at the bottom of the file (inside the main) from something like this:

```
drawRectangle(chris, 50, 100, 0, "red", "") 
```

to something like this:

```
   drawTwoRectangles(chris)  # call the function to draw two rectangles of different sizes and colors
```

Then define the drawTwoRectangles function so that it draws a rectangle with a given size and color,  picks up the pen and moves to a new location, and then draws another rectangle with a different size and color. Here is the final code:

```

def drawTwoRectangles(t):
    
    drawRectangle(t, 50, 100, 0, "red", "") 

    t.seth(0)   # Set the absolute heading of the turtle to 0 degrees (pointing east)


    # Move the turtle right by 200 units without leaving a trail 
    t.up()     
    t.forward(100)  
    t.down()

    drawRectangle(t, 100, 150, 22, "green", "yellow") 
   
```

When you run the code, you should see the following output, with the rectangles very close but not touching: 

![twoRects](twoRects.png){:height="200px"}

If you get the above output, then you are ready to move to the next step.

## Step 5: Add the function to draw an equilateral triangle

Now we are going to add two other functions: `drawTriangle` and `drawTwoTriangles`. The first  function should draw an [equilateral triangle](https://en.wikipedia.org/wiki/Equilateral_triangle) given the length of a side, pen color and fill color. The base of the triangle should be along the x-axis as shown in the figure on top of this page. 
Keep the code that has the actual function calls *at the bottom* of the file, inside the `if __name__=='__main__':` block.

The order should be:

* First, any import statements you need, e.g.

```
import turtle

```

* Second, the functions definitions for `drawRectangle`, `drawTriangle`, etc., e.g.

```
def drawRectangle_1(t):
    # code for the first version of drawing a rectangle

def drawRectangle(t,width, height, tilt, penColor, fillColor):
    # code for the final version of drawing a rectangle 
 
def drawTwoRectangles(t):
    # Code for drawing two rectangles is here

def drawTriangle(t,side penColor, fillColor):
    # Code for drawTriangle is here

def drawTwoTriangles(t):
    # Code to draw two isosceles triangles of different sizes and colors
     
```

* Then the main block, with two parts: first, the code that imports and sets up the turtle, i.e.

```
if __name__=='__main__':
    chris = turtle.Turtle()
    chris.shape("turtle")
    chris.speed(0)
    chris.width(4)
   
```

Then, finally, a part, still indented inside that block, that makes your drawing.

```
    drawTwoRectangles(chris)   # You may comment out this line when testing your drawTriangle() function
    drawTwoTriangles(chris)
    # etc ...
   
```
   

Remember, before implementing a new function, you need to come up with a plan that you can eventually turn into an algorithm (a sequence of steps to achieve the task you set out to do). Here is one possible algorithm for the drawTriangle function:


1. Orient the turtle at 0 degrees with respect to the x-axis
2. Move forward by the number of units specified by the parameter "side"
3. Turn left by some angle that you must calculate in advance
4. Move forward by the number of units specified by the parameter "side"
5. Turn left by some angle that you need to calculate
6. Move forward by the number of units specified by the parameter "side"
7. Orient the turtle at 0 degrees with respect to the x-axis

You can choose to go with the above algorithm or come up with your own. The above algorithm can be implemented in code using a series of `t.forward()` and `t.left()` commands. You may find this easier compared to an algorithm where you calculate the absolute coordinates of the three corners of the triangle and then use a series of goto statements. The difficulty there is just in the trignometry part and not necessarily the code. If you would like to use trigonometry functions you must import the math module. Feel free to use any algorithm that appeals to you.



Now go ahead place the following code below your other functions and the fill in the code for the drawTriangle() function:

```

    
def drawTriangle(t, side, penColor, fillColor):
    """
    draw a equilateral triangle using turtle t, with a given side, penColor and fillColor,
    with the current location of the turtle being the 
    lower left corner. The base of the triangle should be at 0 degrees with respect to the x-axis. 
    Do not assume anything about the initial orientation of the turtle. 
    The final orientation of the turtle should be 0 degrees with respect to the x-axis. 
    """

    # Insert code to draw the triangle

def drawTwoTriangles(t):
    """ Draws two non overlapping triangles with different sizes and colors
    """
    

```

## Step 6: Checking your code before submission

When you are finished with the lab, ask a TA, tutor or instructor to look it over and give you some feedback on it.  

It should be structured in a way that there is 

1. A single file called `drawings.py`

2. Any `import` statements are at the top of the file, e.g. `import turtle` and `import math`


3. Next, function defintions.   Each of these

```
def drawRectangle_1(t):
   " docstring here "
   pass

   
def drawRectangle(t,width, height, tilt, penColor, fillColor):
   " docstring here "
   pass      

 
def drawTwoRectangles(t):
   " docstring here "
   pass

def drawTriangle(t, side, penColor, fillColor):
   " docstring here "
   pass

def drawTwoTriangles(t):
   " docstring here "
   pass      

```

4. At the bottom of the file, an `if __name__=="__main__":` block.  The first thing in that block should be code that
   sets up a turtle.  Call your turtle anything you like (`mary`,`chris`, etc.)
   

5. Finally, still indented inside that block, code that calls those functions to draw two non overlapping rectangles and two triangles as specified before. Your code must draw both for full credit

If you code meets all those criteria, you should be in good shape to submit it.

## Step 7: Submitting via Gradescope

Note that this week, although we are using Gradescope, it is NOT the case that the grade you get from Gradescope is your final grade for the assignment.    The grade on Gradescope is just a PART of your grade--you will get 10 points for basically submitting *anything* that is a valid Python program that has the name `drawings.py`.   However, the other 90 points for this lab will come from an instructor or TA doing a manual inspection of your code to see if it complies with the requirements listed above.      

If you want reassurance that your code is in good shape, you may ask a TA or instructor to look it over during office hours or lab.

To submit your code, navigate to the page for submitting {{page.num}} on Gradescope.

If you got all green, and 10 points, then your submission was accepted---but to emphasize, for this week, the other 90 points will be assigned by a human grader.   You'll be notified of that grade via Gradescope.

(Lab created by Diba Mirza, edits by P. Conrad)
