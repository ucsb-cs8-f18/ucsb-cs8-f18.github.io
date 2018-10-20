#!/usr/bin/env python3

import turtle
import math

      
def drawRectangle(t, width, height, tilt, penColor, fillColor):
    t.color(penColor, fillColor)
    t.begin_fill()
    t.seth(tilt)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.end_fill()
    t.seth(0)

def drawTriangle(t, base, height, penColor, fillColor):

    t.begin_fill()
    t.color(penColor, fillColor)
    t.forward(base)
    turnAngle = 180 - math.degrees(math.atan2(height,base/2))
    t.left(turnAngle)
    side = math.sqrt((base/2)**2 +(height**2))
    t.forward(side)
    t.left(2*(180-turnAngle))
    t.forward(side)
    t.seth(0)
    t.end_fill()
     

if __name__=="__main__":
  jane = turtle.Turtle()
  jane.shape("turtle")
  jane.speed(0)
  jane.width(8)

  drawTriangle(jane, 100, 200, "blue", "green")

  jane.getscreen().exitonclick()
