---
layout: lab
num: project02
ready: false
desc: "Create a really cool map of the United States!"
assigned: 2017-11-27 11:00:00.00-7
due: 2017-12-08 17:00:00.00-8
submit_cs_pnum: 774
---

## Goals for this lab

The goals for this lab are:

* practice processing text files to extract useful data from them
* practice using data within a Python program to do something interesting
* more practice with Python dictionaries, lists and tuples
* more practice with formatting strings and writing to a file
* create a really cool map of cities within the United States (lower 48, or "mainland" as Hawaiians say)!

![map of US](lower48TurtleMap.png){:height="400px"}

## Getting staretd

* Step 0:  Choose your partner
* Step 1: Log on & bring up a terminal window
* Step 2: Create a directory in your cs8 directory named {{page.num}}.
* Step 3: Start IDLE
* Step 4: Download the cTurtle.py module, [cTurtle.py](cTurtle.py){:data-ajax="false"}, in your home directory or in some other directory in your Python path.


## What to program?

In this lab assignment, you will be reading some data files (already pre-processed from their raw form found on the internet) in order to create a map of the lower 48 States as seen in the figure above.  There are 3 files that you will be working with:

[pop3.txt](pop3.txt){:data-ajax="false"} - a text file with lines of rank, city name, population for all us cities having population greater than 100000 (276 cities total).  Here is a sample of the first 20 lines of this file:

```
1 new york,ny 8391881
2 los angeles,ca 3831868
3 chicago,il 2851268
4 houston,tx 2257926
5 phoenix,az 1593659
6 philadelphia,pa 1547297
7 san antonio,tx 1373668
8 san diego,ca 1306300
9 dallas,tx 1299542
10 san jose,ca 964695
11 detroit,mi 910921
12 san francisco,ca 815358
13 jacksonville,fl 813518
14 indianapolis,in 807584
15 austin,tx 786386
16 columbus,oh 769332
17 fort worth,tx 727577
18 charlotte,nc 709441
19 memphis,tn 676640
20 boston,ma 645169
```

[latLon3.txt](latLon3.txt){:data-ajax="false"} - a text file with lines of latitude (North), longitude (West), city name for all locations with major airports.  Here is a sample of the first several lines of this file:

```
33.58 85.85 anniston,al
32.67 85.44 auburn,al
33.57 86.75 birmingham,al
32.90 87.25 centreville,al
31.32 85.45 dothan,al
31.28 85.72 fort rucker,al
33.97 86.09 gadsden,al
34.65 86.77 huntsville,al
32.38 86.37 maxwell afb,al
30.68 88.25 mobile,al
30.63 88.07 mobile aeros,al
32.30 86.40 montgomery,al
34.75 87.62 muscle shoal,al
32.34 86.99 selma,al
31.87 86.02 troy,al
33.23 87.62 tuscaloosa,al
32.17 110.88 davis-m afb,az
33.68 112.08 deer valley,az
31.45 109.60 douglas,az
```

[stateAdj.txt](stateAdj.txt){:data-ajax="false"} - a text file with lines alternating between state adjacency lists (in 2-letter abbreviated format), and an integer between 0 and 3 which when colored according to that integer guarantees no two adjacent states are the same color.  Here is a sample of the first several lines of this file:

```
AK
1
AL,MS,TN,GA,FL
0
AR,MO,TN,MS,LA,TX,OK
0
AZ,CA,NV,UT,CO,NM
3
CA,OR,NV,AZ
2
CO,WY,NE,KS,OK,NM,AZ,UT
2
CT,NY,MA,RI
2
DC,MD,VA
2
DE,MD,PA,NJ
0
FL,AL,GA
1
GA,FL,AL,TN,NC,SC
2
```

Go ahead and download these files into your {{page.num}} directory now.



## Functions to Implement:

1. createCityPopDict() - return D
2. createCityLatLonDict() - return D
3. createStateColorDict() - return D
4. drawLower48Map() - NO return (draws a map and writes to file)



## Function Details:

* createCityPopDict() - return D.  Write a function which opens and reads (and closes when finished) file pop3.txt and returns a dictionary of city : pop associated key:value pairs.  For example,

'new york,ny' : 8391881
'los angeles,ca' : 3831868
'chicago,il' : 2851268

should be the first 3 key:value pairs entered into D.

 NOTES:

 1) Be careful that cities with spaces in their names, like new york,ny, are treated the same as cities without spaces, like chicago,il.  To handle this, for each line of the file, split it into a list, L.  Now L[0] is the city's rank and L[-1] is the city's population.  Everything in between (starting with L[1] and ending at L[-2]) are the words of city's name.  You will want to join these words together with spaces in between to form the city's full name.

 2) Strings like '8391881' will need to be converted to int type.

* createCityLatLonDict() - return D.  Write a function which opens and reads (and closes when finished) file latlon3.txt and returns a dictionary of city : latlon associated key:value pairs.  For example,

```
'anniston,al' : (33.58, -85.85)
'auburn,al' : (32.67, -85.44)
'birmingham,al' : (33.57,- 86.75)
'centreville,al' : (32.90, -87.25)
'dothan,al' : (31.32, -85.45)
'fort rucker,al' : (31.28, -85.72)
```

should be the first 6 key:value pairs entered into D when building it.



NOTES:

1) Again, be careful that cities with spaces in their names, like fort rucker,al, are treated the same as cities without spaces, like auburn,al.  To handle this, for each line of the file, split it into a list, L.  Now L[0] is the city's latitude and L[1] is the city's longitude.  Everything from L[2] to the end L[-1] are the words of the city's name.  You will want to join these words together with spaces in between to form the city's full name.

2) The values in this dictionary are tuples containing latitude (North) and negative longitude (West) angles as their 0th and 1st items.  By making the longitude negative, cities further west will have more negative longitudes that we will use for the x-coordinate in the cTurtle drawing.

3) Finally, strings like '32.67' will need to be converted to an float type.



* createStateColorDict() - return D.  Write a function which opens and reads (and closes when finished) file stateAdj.txt and returns a dictionary of stateAbbreviation : colorNumber associated key:value pairs.  For example,

```
'ak' : 1
'al' : 0
'ar' : 0
'az' : 3
'ca' : 2
```

should be the first 5 key:value pairs entered into D when building it.



NOTES:

1) The list of adjacent states following the first state abbreviation are not actually used in the function, so disregard them.  For example, on line 3 we have AL,MS,TN,GA,FL but yet we never use ,MS,TN,GA,FL.

2) We want our state abbreviations to be lower cased in our dictionary.

3) You may (or may not) find list slicing helpful during this step.



* drawLower48Map() - NO return (draws a map and writes to file).



## Preliminary parts:

1) Create a city : pop dictionary and name it cityPopDict.  Do this by calling your helper function createCityPopDict.

2) Create a city : latlon dictionary and name it cityLatLonDict.  Do this by calling your helper function createCityLatLonDict.

3) Create a stateAbbreviation : colorNumber dictionary and name it stateColorDict.  Do this by calling your helper function createStateColorDict.

4) Create a list of 4 colors (your choice) to use to draw the city dots on your map, and name it colorList.  Remember that cTurtle colors can be specified either as strings or (r, g, b) tuples.

5) Find minimum and maximum latitude and longitude values over all the cities in cityLatLonDict.  There are many ways to do this, and you are free to choose.  One way is to build two lists of the latitude and longitude values, respectively.  Then use the built-in Python functions min and max.  These min and max values will be used to setWorldCoordinates for the turtle map you will draw next.



## Turtle drawing parts:

6) Create a Turtle object (matthew ?) to do some drawing.  After creating, use the min and max latitude and longitude coordinates to setWorldCoordinates.  You can get fancy if you wish and leave a little space (I prefer about 10%) on the sides, top and bottom so that cities aren't drawn right on the edge of the cTurtle window.  I also like to hide the turtle when creating the map using Turtle method .ht().

7) Loop through the cities in cityLatLonDict and have matthew draw a dot at each city's (lon, lat) coordinates, where longitude (lon) is the x-coordinate and latitude (lat) is the y-coordinate of the city.  The area of the dot should be roughly proportional to the population of the city (if available), and the color of the dot should be the color from colorList corresponding to the state's color index defined in stateColorDict.  You can also sort the cities in some way if you feel so inclined, but not required.  If you sort, you will need to create a list of tuples sortedCityList from dictionary cityLatLonDict.  The 0 item of each tuple should be the sorting parameter (for example, a simple approximation from distance (in miles) from Santa Barbara is d = 70*math.sqrt((lat - 34.4)**2 + 0.58*(lon - 119.8)**2)) ), and the 1 item should be the city name.  This gives a cool effect of having your cities plotted radiating away from Santa Barbara!

So let's elaborate a bit....As we loop through the cities in cityLatLonDict (or sortedCityList), we will want to answer the question: Is this city in cityPopDict?  If it is, then the population value can be used to set a dotSize = 4 + math.ceil(math.sqrt(population/50000)).  If the city is not in cityPopDict, then it either has less than 100000 people or it was written differently between the two raw text files from which these data sets were derived.  For example, in the latLon data set, Colorado Springs, CO is written as Colo Springs, CO.  We would need some form of artificial intelligence to catch all such possibilities (maybe an advanced area to explore ;-)).  Regardless, we set a dotSize = 4 in this case.

You might be wondering how to get a city's color index from stateColorDict.  Well, we need to extract the state abbreviation from the city name.  Can you think of how to do that based on the format of all city names?  For example, 'new york,ny', 'los angeles,ca', 'chicago,il', etc.



## File writing part:

9) Once you have succeeded at having your turtle draw the US city map, then do one more thing.  Write the output to a file (called 'output.txt') with 6 columns.  Let the 6 columns be: i) city name, ii) latitude, iii) longitude, iv) population (if known, otherwise leave blank), v) dot size, and vi) dot color.  Be sure to add the newline character ('\n') at the end of each line.  Provide a header line for your output file which indicates the data for each column.  Left justify each column in a field width of i) 30 characters, ii) - vi) 15 characters.  Here is my [output.txt](output.txt){:data-ajax="false"} - yours should look the same except sorting and my last column of distance from Santa Barbara is not required.



Once you have finished the lab, sit back and admire your work.  Show a friend what you have created, and think about all the possibilities of cool things you can do if you continue to learn more computer science!



## Challenge extensions (Optional) (if time permits and you are curious):

A1.  Can you make your cities appear from west to east instead of randomly?  Or perhaps in order of their state abbreviation alphabetically?

A2. You may notice that most maps of the US have a curvature to them so that Washington and Maine appear higher than Minnesota, for example.  This provides a way to visualize the curvature of the earth and represent land areas more accurately on a two-dimensional map, and is an example of what is called a [cartographic projection](https://en.wikipedia.org/wiki/List_of_map_projections).  Can you think of how you might modify your map to create such an effect?





## Submitting via submit.cs

Note that this week, although we are using submit.cs, it is NOT the case that the grade you get from submit.cs is your final grade for the assignment.

The grade on submit.cs is just a PART of your grade--you will get 10
points for basically submitting *anything* that is a valid Python
program that has the name <tt>{{page.num}}.py</tt>.

However, the other 90 points for this lab will come from an instructor
or TA doing a manual inspection of your code to see if it complies
with the requirements listed above.

If you want reassurance that your code is in good shape, you may ask a
TA or instructor to look it over during office hours or lab.

To submit your code, use:

### Navigate to the page for submitting {{page.num}}

The page for submitting {{page.num}} is here: <https://submit.cs.ucsb.edu/form/project/{{page.submit_cs_pnum}}/submission>

Navigate to that page, and upload your `{{page.num}}.py` file.

If you are working on the ECI/CSIL/lab linux systems, you can also submit at the command line with this command:

```
~submit/submit -p {{page.submit_cs_pnum}} ~/cs8/{{page.num}}/{{page.num}}.py
```

It will ask for your email address: use your full umail address (e.g. `cgaucho@umail.ucsb.edu`).  For password, use the password that you enter for the submit.cs system.    You may save these credentials if you don't want to have to type them in every time.


Note that if you try to upload a file with a name that does not match EXACTLY the name `{{page.num}}.py`, the system will not allow you to do it.

Once you upload it, you should get a page that shows your submission is pending.

Refresh that page, and you should get one that indicates with either red, or green, whether the test cases for your code passed or failed.

If you got all green, and 10 points, then your submission was accepted---but to emphasize, for this week, the other 90 points will be assigned by a human grader.   You'll be notified of that grade [via Gauchospace](https://gauchospace.ucsb.edu).

Thnaks to Matt Buoni for this lab
