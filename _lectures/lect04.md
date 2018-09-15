---
num: "Lecture 4"
desc: "Python Modules and turtle graphics"
ready: true
date: 2017-10-11 1:30:00.00-7:00
---

# Resources from lecture

* [Link to all code written in lecture](https://github.com/ucsb-cs8-f17/cs8-f17-lecture-code)

* [Link to lecture slides and peer instruction questions](https://drive.google.com/drive/folders/0BxIvQwpl4ocoRy1Pa041SThLUFU?usp=sharing)

* [Guidelines for using peer instruction - thanks to Dan Zingaro](https://drive.google.com/file/d/0BxIvQwpl4ocoX2ZpUjJDZW52Wlk/view?usp=sharing)


# Learning Goals
* Modules - how to use them and look up documentation
* Designing functions that are READABLE, REUSABLE and DRY (loops)

#Turtle Graphics: Formal introduction to modules  

* Modules are used to group functions
* Use import to make a module's functions available
* Any file ending in .py can act as a module
* import runs all the code in a .py file
* If we import module_name, we access its functions through
module_name.function_name
* To access function_name without having to type the
module_name prefix, we can use

```
from module_name import function_name
```
* The turtle module gives us access to functions for drawing cool graphics. To use this module, as with all modules - first import it as follows:

```
import turtle
```

Start by creating a new Turtle object using the special function "Turtle"

```
jane = turtle.Turtle()
```

So far we have worked with some basic data types


From here on you can customize what jane looks like and command it to move around on your screen. You can do this by calling the functions that the turtle module provides on our turtle jane using the dot notation.

For example, you can make jane look like an actual turtle using the shape function

```
jane.shape("turtle")
```

Or change jane's color

```
jane.color("red")
```

You can query jane's location on your canvas

```
jane.xcor()
jane.ycor()
```

And finally you can command jane to move forwrad backward and turn left or right 

```
jane.forward(100)
jane.backward(100)
jane.left(90)
jane.right(90)
jane.up()          # Lift the turtle's tail to avoid leaving a trail
jane.goto(100, 20) # Go to location (100,20)
jane.down()     # Put the tail down to start drawing
jane.forward(100)

```

To learn about all the turtle functions that you can use type

```
dir(turtle) or dir(jane)
```

To learn more about the usage of each function use the "help" function:

```
help(jane.forward)
```
Notice the concept of "abstraction" at work. As the user of the function forward() we don't have to know the details of how it was implemented, we only have to know what the function does, what its parameters are and how to use it. This information is exactly what "help" displays. 

Coding example: 
* Draw a square: You just wrote an algorithm! 
* Examine the drawSquare function
  - How can we make it more reusuable? 
  - Add a parameter for a user defined width. 
  - Discuss local vs global variables

* Reuse the code in drawSquare to draw a Rectangle 
  - this is even more general
  - Add fill color 

* Draw two rectangles

* Write a function to draw three rectangles
  - How can we make the implementation of this function more readable? Hint: add a new function to jump between locations
  - How can we make this function more general/reusable? Hint: Add parameters
  - Before modifying your code plan it out

* How can we make a more general version of the previous function? What if we wanted to draw 4, 5, 6, ...or some n rectcangles
  - We could go on adding more lines of code but that doesn't help us come up with a general enough solution. We need something new 

# Repetition using for loops
* Some basic code involving for loops
* The range function 
* Use for loops to implement the drawNRectangles() function
* Cycle through colors
* Go back and refactor your code to keep it DRY














