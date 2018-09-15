---
layout: lab
num: lab09
ready: false
desc: "Image Manipulation: Colors in code, nested loops"
assigned: 2017-11-28 8:00:00.00-7
due: 2017-12-04 17:00:00.00-7
---

# to do : clean up and set up submit.cs

If you find typos or problems with the lab instructions, please report them on Piazza


# Learning Goals

* More practice with the tuple data type!
* Import and export media (picture) files in PIL
* Use your programming knowledge so far to manipulate pixels in picture files
* Invent and implement algorithms to transform pictures 

## Getting started


* Step 1: Log on & bring up a terminal window
This is done following the steps you have performed in lab00.
* Step 2: Create a directory in your cs8 directory named {{page.num}}. 
* Step 3: Start IDLE
* Step 4: For each of the programming exercises in this lab come up with a solution outline by discussing with your partner. Don't be in a hurry to start coding unless you have a fairly clear idea of a solution strategy and your first steps.



## Introduction to the Python Imaging Library (PIL)

Our computers encode all data (pictures, games, files) as sequences of 0s and 1s.  They are just a digital kingdom of bits! Some of the text below is review, but be sure to read it over (quickly) anyway.

In your computer, images (pictures) are files stored on your hard disk. A digital image is logically a rectangular grid of pixels, which appear as squares when enlarged; each pixel then typically consists of 1 byte (8 bits) for a Black-and-White image or 3 bytes (24 bits) for a color image, where one byte (a value between 0 and 255) each is for Red (R), Green (G), and Blue (B). R, G, B are three ingredients for all visible colors; for example: blue is 0 redness + 0 greenness + 255 blueness, white is 255 redness + 255 greenness + 255 blueness, and brown is 165 redness + 42 greenness + 42 blueness, etc.. The following figure by Wikipedia shows a color image with enlarged pixels.

<p align="center">
![](/lab/images/Pixel-example.gif)
</p>

In this lab we'll work with the Python Imaging Library (PIL) which is a graphics library like turle designed for working with image files. So let's warm up!

## Getting familiar with PIL

Download the  "stone bear" picture below and save it in your `~/cs8/{{page.num}} directory. You can do this by right clicking on the image and selecting the option to save. Be sure to save the image as "stoneteddybear.jpg".

<p align="center">

![](/lab/images/stoneteddybear.jpg){:height="400px"}

</p>

Next, launch IDLE in the same directory that you stored the stone bear image.

Before we can manipulate a picture in PIL, we will need to tell Python and PIL where to find it.  To do this, you will need to specify the exact path to the picture on your computer.  You also need to tell Python about the PIL Image library.  We'll start by playing around with the teddy bear image in the shell.  In the shell, type the following to load the Image library into the shell (later you'll put this line at the top of your file).  

```
>>> from PIL import Image

```

Then, you can open the picture you just downloaded as an image as follows:

```
>>> stonebear = Image.open( "stoneteddybear.jpg" )

```

The argument to the open function tells Python where to find the image. If you are getting an error here it's probably because of a typo in your filename, or because you either placed the file in the wrong place or launched IDLE from a directory different from where the image was stored. 

To ensure that the command you just executed works you can show the image you just created:

```
>>> stonebear.show()
```

Logically, an image is a grid of pixels. The size of the "stone bear" picture is 600 x 800, i.e., 480,000 pixels. You can pick a specific pixel from the image by using the `getpixel()` function. The arguments of this function are a picture object and the pixel's X position and its Y position; the function returns the pixel object at the coordinate(X, Y) of the image. Note that in the image grid, the axis is a little different from the usual 2D Cartesian axis, in that it counts from upper left to bottom right. For example, in the following 18 x 18 image grid, the coordinate (11, 7) is the grey block. Note the index starts at 0.

<p align="center">
![](/lab/images/coordinates.gif){:height="400px"}
</p>

So, if you make the following statement:

```
>>> pixel = stonebear.getpixel( ( 100, 200) )

```

the pixel returned is a tuple representing the RGB values of the pixel on the 200th row from top, 100th column from left, in the stonebear image. You can see this by looking at the value stored in pixel.

```
>>> pixel
(166, 201, 239)
```

Now, let's see how to modify the colors of individual pixels in the image.  To modify a pixel use the putpixel function
```
>>> stonebear.putpixel( (100, 200), (0, 0, 0) )
```

The `putpixel` function takes two arguments: 

* a pixel coordinate  represented by an (x, y) tuple.  In the example below our first argument is: (100, 200) , which is a tuple representing a single pixel. Using this function, can modify one pixel at a time.

* a tuple representing the RGB color to set the pixel to.  In the example above, this color is (0, 0, 0), i.e. black.

After running the command above, show the bear image again and see if you can find the modified pixel.  It's there!

If you have a hard time seeing the modified pixel, try the following code to turn a range of pixels black.

```
for i in range(100):
    stonebear.putpixel( (i, 200) , (0, 0, 0) )

```

After running the command above, show the bear image again and see if you can find the modified pixels.  It should be easier to see your modification this time around.

## Hiding the stone bear's face

Now we are going to start working in a file so that we can save our work.  If you haven't done so already, create a new Python file called "imaging.py", and place the appropriate header comment at the top that descibes the content of the file.  Don't forget your header comment!  

Now, after the header comment, tell Python that you want to use the Image module from the PIL library, as follows:

```
from PIL import Image
```

Save your work and commit your change to git using the `git add .` , `git commit -m ""` commands.  Now you're ready to write your first function for this lab.

The stone bear is shy, and he wants you to cover his face using a dark rectangular area. To do this, you will write a function called blockHead which will transform the color of a specified range of the picture to be all black. The header for this function is 

```
def blockHead( im, startx, starty, endx, endy ):
```

`im` is the image to modify, startx and starty represent the x and y coordinates of the upper left corner of the box to paint black and endx and endy represent the x and y coordinates of the lower right corner of the image to paint black.  Your function will not return anything.  For reasons we will discuss in the next week or two, the image will be modified even after the function returns!

You might notice that blockHead is in fact not specific to blocking the head in the stone bear image, but rather will block any rectangle in any image, according to the parameters passed in. For the rest of this lab, we'll ask you to use nested loops and the putpixel method, so feel free to try this here.
Don't forget you can access the [documentation for the Image module](http://pillow.readthedocs.io/en/3.1.x/reference/Image.html)
When you have finished writing your function, test it by calling it in the shell to block the stone bear's face.  Note, to do this you will need to do the following as commands in the shell:

* Create an image from the stone bear file (if you haven't done so already)
* Call your blockHead method, passing in the appropriate arguments  The coordinates of the four corners of the rectangle are (240, 130), (450, 130), (450, 290), and (240, 290), starting from upper left, clockwise.  
* Show the image after you call the function to make sure that the black rectangle appears as expected.
* If your blockHead is implemented correctly, you should have the shy bear's head cover as follows :

           
![blockhead](/lab/images/PIL/blockheadbear.jpg)     

## Saving modified pictures

The last step of our warm-up: be aware you just changed a COPY of the stone bear image! Even though you see the change in the stone bear image, that change will not be saved when you exit Python.  What? What does that mean? 

Even after all your work playing with colors and hiding the bear's face in the previous activities, the original picture file has not changed!  To see this, open your "stone bear" file by opening the picture in your `~/cs8/{{page.num}} directory and double clicking on the image file. You will find nothing changed. It looks like nothing has been done to it. Why?

Basically, the Python functions you've used are not directly processing the stone bear image on the hard disk.  Rather,  when you open an image, PIL makes a duplicate of that image and loads that duplicate copy into  memory. The copy, as you can imagine, is exactly what was assigned to stonebear, so whatever you have done to stonebear only happened to the copy of your "stone bear" image. 

As a programmer, you should always have the concept of the computer memory in your mind. This technique of loading a copy of a file to memory (which is relatively fast) rather than directly handing a file on the disk (slow) is very common. 

What if we we want to save the changes we've made to the file on disk? We will need to force computer to write the latest memory copies back to the disk, so that the files on the disk change, too.

Let's get back to the shy stone bear. If you correctly changed the stonebear, and you want the actual file of "stone bear" picture to be changed accordingly, you should use the Image.save function. Read the documentation to see how it works (HINT: It takes one argument, which is a string specifying where you want the file saved including its name) and save your modified stonebear picture now.  A word of advice: we recommend you don't apply the changes to the original "stone bear" image, but to a different file (let's say, "shystonebear.jpg" somewhere). This way you won't lose your original picture in case you blocked a wrong area of the shy bear.  

That is all for our warm-ups. Make sure you understand how all this works before launching into your tasks below.

## Invert Function

Way back in the days of film cameras and chemical processing of photo images, one step in the processing process produced a negative image.

We can achieve the negative (aka inverted) effect digitally by subtracting each of the original RGB values of a pixel from 255.

For example, if the pixel RGB values are 34, 67, 87, the new RGB values of that same pixel will be 255-34, 255-67, 255-87. Or 221, 188, 168.

But that is only for one pixel and an image consists of thousands, or even millions, of pixels. Here we will use for loops to traverse through the list of pixels in an image. 

Read over this function to get a sense of how to we will use nested loops to modify pictures

```
def invert( im ):
    ''' Invert the colors in the input image, im '''
    
    imsize = im.size
    width = imsize[0]
    height = imsize[1]
    # Note that the previous 3 lines could be replaced by the single line:
    # (width, height) = im.size()
    # We will use this shorthand below.  Ask a tutor if you are confused.

    for x in range(width ):
        for y in range( height ):
            (red, green, blue) = im.getpixel((x, y))
            newRed = 255-red
            newGreen = 255-green
            newBlue = 255-blue
            im.putpixel((x, y), (newRed, newGreen, newBlue))

```

Copy this function into your "imaging.py" file, load it and run it.  Again, you will need to follow the three steps from above to run this function:

* Create the stone bear image
* Run the function, passing in the image
* Show the image after running the function

Tired of typing these lines into the shell? You can actually place the lines that will execute the three steps above into your "imaging.py" file, outside of any function (below all the function definitions). Then, run your program. When you execute the invert function on the stone bear picture given to you. Your result should look similar to this.

<p align="center">
![](/lab/images/PIL/invertedbear.jpg){:height="400px"}
</p>

Functions for you to write

NOTES: 

In all of the functions below, we would like you to use (nested) loops and the putpixel() function on the Image object. PIL already implements many of the things we're asking you to do below. However, we ask that you use the putpixel() function to re-implement this functionality so that you get practice implementing these more complex functions.

You should also test your functions after writing each one.  You should test them on the stone bear image, and AT LEAST ONE OTHER IMAGE. We suggest using your own picture available in one your earlier git hub repos :)

## Greyscale

Now that we have some experience changing the colors in a picture, we'll write functions to make greyscale and black and white (binary) images.  The concept of image luminance will help us out. In layman's terms, luminance is how bright or dark the colors in a pixel are (compared to white).

As (the almighty) Wikipedia calculates it, luminance is 21% red, 72% green, and 7% blue. Intuitively, this makes sense because if you think of standard red, green, and blue, green is the lightest and thus has highest positive impact luminance, while blue is darker and has a lower value for luminance. This is useful! You're going to calculate luminance for pixel operations.

Write a function called greyscale that takes an image as a parameter and modifies it to make it greyscale. For this, you'll want to do something similar to invert, except that we will first calculate the luminance of a pixel and then set each of the three color channels to this value.  Since luminance is an indication of how white/black a pixel is, just insert the same value in each of the three color channels!


<p align="center">

![alt-bear1](/lab/images/PIL/originalbear.jpg){:height="400px"} 
![alt-bear2](/lab/images/PIL/grayscalebear.png){:height="400px"}

</p>


Hint: Getting an OverflowError: unsigned byte integer is greater than maximum? This might be because your luminance calculation results in RGB values higher than 255. Make sure that all of your percentages add up to 1.


## Geometric Transformations!

The following four functions take an image as an argument and modify that image.  They don't return anything.  
Write `mirrorVert`: This function takes an image and modifies the image to mirror the photo across its horizontal axis (i.e., so that the top part is mirrored upside down on the bottom of the image). Hint: Think carefully about which pixels you need to loop over, and where each pixel in the top half needs to be copied to create the mirror effect.  Start with concrete examples as we will see in class.   Then derive the general formula based on the pixel's location (x, y) and the height and width of the image.

<p align="center">

![](/lab/images/PIL/vertmirror.jpg){:height="400px"}

</p>

`mirrorHoriz`: Same as above, but mirroring across the vertical axis. Hint:  Instead of replacing the bottom rows with the reversed top rows (as you did in `mirrorVert`), you'll replace the last half of the pixels in every row with the reversed first half of the pixels.

<p align="center">

![](/lab/images/PIL/horizmirror.jpg){:height="400px"}

</p>


# Submission


Great job working through {{page.num}}! 

## Navigate to the page for submitting {{page.num}}

The page for submitting {{page.num}} is here: <https://submit.cs.ucsb.edu/form/project/{{page.submit_cs_pnum}}/submission>

Navigate to that page, and upload your `{{page.num}}.py` file.

# Submission from CSIL command line

If you are working on the ECI/CSIL/lab linux systems, you can also submit at the command line with this command:

<tt>~submit/submit -p {{page.submit_cs_pnum}} ~/cs8/{{page.num}}/{{page.num}}.py</tt>

Notes on using the command line version of submit:

* This ONLY works on CSIL.  From your own PC or Mac, use the web form for submission.

* The first time you use the `~submit/submit ...` command (or every time if you choose not to save your credentials) you will be asked for your email address: use your full umail address (e.g. `cgaucho@umail.ucsb.edu`).  For password, use the password that you enter for the submit.cs system.    You may save these credentials if you don't want to have to type them in every time.

* Note that if you try to upload a file with a name that does not match EXACTLY the name `{{page.num}}.py`, the system will not allow you to do it.   Once you upload it, you should get a page that shows your submission is pending.  Refresh that page, and you should get one that indicates with either red, or green, whether the test cases for your code passed or failed.



Adapted from SPIS-2016 (UCSD)









