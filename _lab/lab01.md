---
layout: lab
num: lab01
ready: false
desc: "Turtle Graphics: Basic drawings"
assigned: 2018-10-10 08:00:00.00-7
due: 2018-10-16 23:59:00.00-7

---


Goal
====

The goal of this lab is to vizualize how simple Python programs run using Turtle Graphics.


What you'll be drawing
----------------------

You'll use the Python editor to write a program that draws two rectangles, where the smaller rectangle is contained within the larger one. 

The output produced when you run your program is shown in the following figure.

![basicDrawing](basicRect.png){:height="200px"}

Your drawing should satisfy the following requirements:

* Each edge of the inner rectangle should be at an equal distance from the corresponding edge of the outer rectangle
* Your turtle should end up at the same position and orientation as shown in the figure (relative to the outer rectangle)

Your drawing may vary from the one shown in the figure in the following ways:

* The inner and outer rectangles can be of the same color
* You may choose any dimensions for the two rectangles as long as your figure looks similar to the one shown

# The programming part

## Step 1: Create a {{page.num}} directory under your cs8 directory

Create a directory called `~/cs8/{{page.num}}` for a file
we are going to call `{{page.num}}.py`.

To do that, use the commands below.

(Just like last week, your prompt may not be exactly like the one shown here.  Instead of `-bash-4.2$ `, you might have something like `[cgaucho@cstl-15 ~]$ `.    The `cgaucho` here is your username, the `cstl-15` is where you are logged in, and the `~` is your current directory.    Don't be distracted by this detail.)


<pre>-bash-4.2$ <strong>cd</strong>
-bash-4.2$ <strong>pwd</strong>
/<em>cs</em>/<em>student</em>/<em>yourusername</em>
-bash-4.2$ <strong>cd cs8</strong>
-bash-4.2$ <strong>pwd</strong>
/<em>cs</em>/<em>student</em>/<em>yourusername</em>/cs8
-bash-4.2$ <strong>mkdir {{page.num}}</strong>
-bash-4.2$ <strong>cd {{page.num}}</strong>
-bash-4.2$ <strong>pwd</strong>
/<em>cs</em>/<em>student</em>/<em>yourusername</em>/cs8/{{page.num}}
-bash-4.2$
</pre>

## Step 2: Open `idle3` and create `{{page.num}}.py`

Open up `idle3` and select the menu option `File => New File` to create a new file.

In this file, put this code (but put your name instead of "your name goes here")

```
# {{page.num}}.py, your name goes here
import turtle

t = turtle.Turtle()

```

You can name your turtle anything you like; I used `t` because it's short to type.

Optionally, you can make your turtle look like a turtle by typing this:

```
t.shape("turtle")
```

And you can set your turtle to move at the fastest possible speed on the screen - which will help make your drawings as quickly as possible.

```
t.speed(0)
```
Also, you can change the pen width to make your drawings look more prominent

```
t.width(4)
```
Now you can write a command to draw a line by moving your turtle forward by 50 pixels

```
t.forward(50)
```

Save the file as {{page.num}}.py, and run it.   You should see a turtle appear. The turtle is not moving because we haven't given it instructions to move. 


## Step 3: Complete your drawing

Add more code to your file to complete drawing the inner rectangle. Run your program to make sure you get an output similar to the one shown below:

![one Rect](oneRect.png){:height="200px"}

If you get an error, don't panic - just raise your hand and one of the TAs or tutors will help you out.

Your next task is a little more challenging. You have to move the turtle to the right spot on your canvas to begin drawing the second rectangle. Remember you can move the turtle relative to its current position using the forward and backward commands. You can change the orientation of the turtle by turning it left or right by an angle using the left/right commands. Your turtle moves on a cartesian coordinate system with (0,0) at the center of the screen. If you'd like to move it to an abosolute X,Y location, use the goto command. For example the following command makes the turtle jump to the location (20, 80)

```
t.goto(20,80)
```

To avoid drawing a line as you move the turtle to a new spot, lift the turtle's pen prior to moving it using the following command:

```
t.up()
```

Then move the turtle to a new spot

Finally, place the turtle's pen down again using the following command:

```
t.down()
```

To draw the outer rectangle your main task if to calculate the location of the bottom left corner of the outer rectangle relative to the turtle's current location or its absolute location. Then use either the backward, forward, left, right commands or the goto command to jump to this new spot. Now draw the outer rectangle. 

A correct implementation should produce the following output:

![basicDrawing](basicRect.PNG){:height="200px"}

## Step 4: Submit your code on gradescope

Navigate to the {{page.num}} assignment on gradescope and submit the file {{page.num}}.py. If you don't recall how to do this refer back to the instructions in lab00

If your code runs without any syntax errors, you should see a score of 10/50. The remainder of the grade will be assigned by a TA manually according to the following rubric

* 10 points for correctly drawing the inner rectangle
* 20 points for drawing two rectangles such that the inner and outer rectangles don't intersect and one rectangle is embedded within the other
* 10 points for making sure that each edge of the inner rectangle is at an equal distance from the corresponding edge of the outer rectangle


## Step 5: Get your code checked off by a TA or tutor

Before you leave the lab, show your code and  output to a TA or tutor.



