---
title: "Syllabus, CMPSC 8, Fall 2017"
layout: handout
ready: false
---

Basic Facts
-----------

* **Course Web Site**: <http://ucsb-cs8.github.io>
* **Instructor**:  [Diba Mirza](http://www.cs.ucsb.edu/~dmirza)
   * Email is diba@ucsb.edu, BUT please use Piazza for course related communication.
* **Lecture**: MW 12:30pm-1:45pm MUSIC LLCH, ATTENDANCE REQUIRED.
* **TAs**:  {{site.ta_list_full}} (contact via Piazza.com)
* **Lab** (50 minute discussion section) Tuesdays 8am, 9am , 10am , 11am , noon, 1pm - Phelps 3525, ATTENDANCE REQUIRED.                                         
* Office Hours: See: [Dr. Mirza and CS 8 staff office hours calendar](https://calendar.google.com/calendar/embed?src=ucsb.edu_760irs3sq39ukkker6l89gaf4g%40group.calendar.google.com&ctz=America/Los_Angeles")


# Required Resources

* Textbook: "Introduction to Computing Using Python" - Ljubomir Perkovic, 2nd edition
* iclicker remote for in class participation (purchase at the book store)

Official UCSB Catalog Description
---------------------------------

<div style="background-color:#eee; border: 8px inset #333; font-size:90%; margin:1em; width:45em; padding: 0.5em;" markdown="1">

CMPSC 8: Introduction to Computer Science

Not open for credit to students who have completed Computer Science 16 or Engineering 3.

Introduction to computer program development for students with little to no programming experience. Basic programming concepts, variables and expressions, data and control structures, algorithms, debugging, program design, and documentation.

</div>


## A Few Course Policies In Brief

* If you are registered for another UCSB course  that overlaps with this one, you MUST HAVE specific written permission from both instructors, or I am within my rights to give you a failing grade on any work you miss as a result, and will NOT make any accommodations for you.  This includes exams.
* You are permitted one sheet of notes on exams—details later on the syllabus.
* Collaboration is only permitted when specifically allowed for—otherwise, you must do your own work.
   * On most homework assignments  you may collaborate with at most one other person (who must be named).
* Attendance is required at all lectures and labs (discussion sections) and is checked via participation using the iclickers
  * I recognize that some absences (e.g. minor illnesses, mishaps, etc.) are unavoidable.  Litigating whether each of these is "excused" or not isn't a good use of anyone's time, so instead we just drop the lowest four grades from everyone's homework/in-class assignment grades.  In this way, absenses (or failure to turn in homework) does not unduly penalize your grade unless it becomes excessive.
* <strong>You</strong> must turn in your homework using the homework mailbox for CS8 located in the copy room on the second floor of HFH building



You may NOT: 

* Turn in homework on a day other than when it is due (early or late)
* Have someone else turn in your homework for you (that will be considered academic dishonesty).
* Drop it off with the instructor to be graded later.

## What this course is about 

This course is an introduction to Computer Science, and programming. 

Computer Science is the study of <strong>abstractions </strong>and <strong>algorithms</strong>. 

* In Computer Science, an <strong>abstraction</strong> is a useful representation of something from the real world that allows us to work with it more easily or efficiently.

* An <strong>algorithm</strong> is a well-defined, step-by-step sequence of instructions that can be used to mechanically determine the solution to some well-defined problem.

You probably use <strong>abstractions</strong> and <strong>algorithms</strong> every day—for example:

* If you pick up any textbook, you'll probably find an index in the back of the book. The index is an <strong>abstraction</strong>—whether the book is about biology, modern art, political science, or computers, the &quot;way the index works&quot; is the always the same. It is composed of the same pieces (topics and page numbers), and organized in the same way (alphabetically by topic, then lists of page numbers in numerical order from smallest to largest.)

* If you are looking in the index of a U.S. history textbook for &quot;Gettysburg&quot; you'll probably use an <strong>algorithm</strong> to find the entry quickly. Here the input to the algorithm is some topic, and the output is a list of pages on which that topic appears.

* If you are looking for a parking lot on campus, you might use an <strong>abstraction</strong> called a &quot;map&quot; to locate the parking lot. You know the features of a map, and how it corresponds to the reality of a college campus, and parking spaces. The way a map can work to help you find a parking lot (or garage) is the same whether it's a map of UCSB, Downtown Santa Barbara, or the Staples Center in LA.

* If you are searching through a parking lot (or garage) to either (a) find a parking space, or (b) determine that there are no spaces left, you probably use an <strong>algorithm</strong> to do that—again, without even thinking about what you are doing.


## Algorithms have to be both designed, and &quot;coded&quot; so the computer can carry them out 

In the case of using an index, this is probably an algorithm you may have learned in grade school, and it has been so long since you learned it, that now you don't even think about it—you just do it. Finding a space in a parking lot—and knowing when to give up and look elsewhere—is &quot;just common sense&quot;; this probably isn't something you were ever &quot;taught&quot;, or even have to think very much about. You just do it.

Computers don't currently have this capability—i.e. the capability to &quot;pick up things by common sense&quot;—and it seems unlikely that they  will within our lifetime—unless there are major breakthroughs in the field of Artificial Intelligence. Such breakthroughs have been predicted for a while, but they haven't happened yet. (Maybe you'll be the one to figure out how to achieve this!)

So, for the time being at least, it falls to humans to design algorithms that computers can use to solve problems. In many cases, these algorithms are &quot;just common sense&quot;—the computer equivalent of looking for an empty parking space in a parking lot (and knowing when to give up). Algorithms like this are easy to design. Many of the algorithms we'll see in this course are like that.

In other cases, the algorithms are very complex, or very subtle, and coming up with them is a deep intellectual challenge. Furthermore, the impact of a better algorithm on society can be very large. For example, new algorithms in the field of computational science—modeling chemical and biological reactions with computer simulations—can lead to breakthroughs such as new drugs to fight disease, or renewable sources of energy.

And often, what goes along with finding a good algorithm is finding a good abstraction of the real world concepts we are interested in: cells, molecules, oil fields, words, sentences, students, courses, GPAs, etc. Algorithms and abstractions really go hand-in-hand.

## Coding, or Writing Software, or Programming

Coding is expressing algorithms in a programming language.

Human languages such as English and Spanish are not very well suited for expressing algorithms—at least not for expressing them to a computer (they have their problems for communicating with humans too!). So, special languages are used. In this course, we'll learn the Python programming language. We choose Python rather than Java or C++ because:

* If you are learning your first programming language, Python is easier to learn than the others
* Learning Python provides a good foundation for learning C, C++ or Java
* If you only learn one programming language, Python is a good choice—in spite of being easy to learn, it is not a &quot;toy&quot; language by any means. It is widely used by scientists and web application developers just for starters. Many internal systems at Google are based on Python code.
 
This course provides you with the opportunity to become a pretty good beginning programmer, and be well prepared for an intermediate programming course such as CS16 (the first course that counts towards the CS major at UCSB, and which requires at least one quarter of prior programming experience.)

I say that the course &quot;provides an opportunity,&quot; because you will only become a good beginning-level programmer if <strong>you</strong> put a lot of time and effort into this course—that is true no matter how much thought and attention I put in my lectures, assignments, and exams

## The swimming/guitar/painting analogy

You cannot learn to swim, play guitar, or paint from a textbook or a lecture. You can only:

* learn  to swim by spending many hours in the pool
* learn to play guitar by spending many hours playing the instrument
* learn to paint by spending many hours putting brush to canvas

The same is true of programming. Programming is not a series of facts to be memorized—you cannot &quot;cram&quot; for a computer science exam. You must practice, practice, practice.

<div style="page-break-before:always;">
&nbsp;
</div>

# What you need to learn to become <br />a skilled beginning level programmer


So, what is it that you need to know to be a skilled beginning-level programmer in Python? Here's the  list of what you'll need to be ready for CMPSC&nbsp;16 (aka CS16, the next programming course):

<table border="1" cellspacing="1" cellpadding="1" id="topicTable">
  <tr>
    <td><ul class="style11">
      <li>Problem solving
        <ul>
            <li>breaking down a problem into a sequence of steps</li>
          <li>abstracting specific problems into general ones<br />
            and finding general solutions</li>
        </ul>
      </li>
      <li>Memory concepts
        <ul>
            <li>variables, primitive vs. reference variables, name, type, value</li>
          <li>assignment statements</li>
          <li>scope of variables</li>
        </ul>
      </li>
      <li>Control structures
        <ul>
            <li>for loops, if/else, while loops</li>
        </ul>
      </li>
      <li>Lists in Python (similar to arrays in other languages)
        <ul>
            <li>index vs. value, finding sum, min, max, average, count of elements matching some condition, making a new list of elements containing only those that match some condition</li>
        </ul>
      </li>
    </ul>    </td>
    <td><ul class="style11">
      <li>Functions
        <ul>
            <li>function call vs. function definition</li>
          <li>formal vs. actual parameters (arguments)</li>
        </ul>
      </li>
      <li>Testing
        <ul>
            <li>How to test your code</li>
        </ul>
      </li>
      <li>Input/output concepts
        <ul>
            <li>Writing to the terminal</li>
          <li>Reading from the keyboard</li>
          <li>Reading and writing to files</li>
          <li>Neatly formatting output</li>
        </ul>
      </li>
      <li>Program style
        <ul>
            <li>How to write code that other people can read and understand</li>
        </ul>
      </li>
    </ul>    </td>
  </tr>
</table>



Final Course Grades
===================

The formula to determine your course grade average is explained in the table below.

Regardless of any other policies spelled out here, the average used to determine your final letter grade may be no higher than one full letter grade higher than your exam average.

Thus,

-   reasonably good performance on exams is very important to earning a good final grade in the course.
-   an A or B should not be out of reach for anyone that has a reasonably good mastery of course concepts (enough to earn a B or C on the exams), and puts in hard work on the labs and project points.

To convert final averages to letter grades, a standard 10 point scale will be used, with the upper and lower ends of each range as +/- grades, except
for A+ grades, see below.  There is no "rounding up"; a grade of 86.9999 is a B and a grade of 87.0000 is a B+.

A+ grades: These may be awarded to the very best performing students in the class—but the cutoff for A+ grades will be determined at the end of the course at the discretion of the instructor (there is no pre-determined cutoff---an average of 97 or more doesn't guarantee you an A+ grade.)

| Grade Item                                                                   | Percentage of Final Grade |
|------------------------------------------------------------------------------|---------------------------|
| Midterm (2)                                                                    | 20 %                      |
| Lab Exams  (2)                                                                 | 20 %| 
| Final                                                                        | 30 %                      |
| Hwks                                                                          |5%|
| Labs                                                                          |13%|
| Project  | 10 %    |
| iclickers | 2 %   |


<div style="page-break-before:always;">
&nbsp;
</div>



Attendance
==========

This course moves quickly. So attendance is very important.  This is even more true in the summer.

As a result, there will be something you have to turn in at almost
every class. In this way, attendance is taken, and required.

These things you have to turn in will be a combination of in-class
activities, and homework completed outside of class, but handed in on
paper during class.

Missing homework/in-class activities: Drop the lowest 4
-------------------------------------------------------

If you miss a class, you miss the opportunity for the points on that
in-class assignment, or homework that was due. Period.

There is no makeup. In lieu of providing a makeup opportunity, I will
drop the lowest 4 homework/in-class-assignment grades (which may be
zeros if you miss an assignment.) Each homework and in-class-activity
will be of equal value (100 pts).

Notes sheets on exams
---------------------

-   You are permitted one 8.5 x 11 (standard US letter size paper) sheet of notes for each exam.
-   You are permitted only one sheet per exam.
-   Your notes sheet will be collected and WILL NOT BE RETURNED
-   So, if you need a copy of it, make a copy BEFORE you come to the exam.

Questions about grades
----------------------

**Summary: regrade requests must be made only on GradeScope, and always within one week.**

From time to time, the people who grade your papers may make clerical
errors in grading (e.g. adding up points wrong or applying a rubric
incorrectly.) For this reason, you are encouraged to review your
grades as they are posted to Gradescope and Gauchospace. You will
typically get an email as soon as each grade is posted. From the time
the grade is posted, you will have one calendar week to post regrade
requests. These must be made ONLY through Gradescope, ON the correct
problem. (Don't request a regrade for question 4 on the page for
question 7.)

Please note that <b>regrade requests based on clerical errors or
applying a rubric incorrectly are always welcome</b>. Over the course
of the quarter, we'll grade over 10,000 individual problems, so it is
unlikely that we won't make at least some mistakes.

<b>More problematic are challenges to the rubric itself</b>, e.g. "I
don't think you should have taken off so many points for that error"
or "I think I deserve more partial credit for that incorrect
answer". The instructor and TA will always listen, but please know
that we've put a great deal of thought, time and experience into
determining the rubric, and we've done our best to apply it to all
students equitably. You may have a different point of view, we will
not always agree with your assessment—in fact, we seldom will. <b>As
such, regrade requests on this basis are not encouraged.</b> It is
important to approach such conversations in a respectful manner,
accepting that the instructor, TA and grader have been given
responsibility for determining course standards, and applying those in
a fair way to all students.

In any case, once the two week deadline for challenges has passed,
each grade becomes final---and it is your responsibility to come to
scheduled TA or instructor office hours to have this discussion. If
you cannot make office hours, you may request an appointment, but you
must request the appointment within ONE WEEK of the assignment being
posted. If you wait until the last office hours opportunity during the
two week window, and you are not able to be seen (e.g. because of a
long line of students), then you lose the right to appeal your grade.



<div style="page-break-before:always;">
&nbsp;
</div>


Late Labs
---------

The policy is simple, and is based on the idea that the primary
purpose of the deadlines is to allow the TA manage his/her
workload. The number of labs in this course requires that he/she not
have to do "context switching" between grading different labs. All
labs must be graded in one sitting, or he/she just won't be able to
keep up with the workload.

So:

-   If you want your work to be graded without penalty, turn it in on time.
-   If you turn in your lab late, you RISK GETTING A ZERO.
-   We will grade late labs ONLY if it creates no extra inconvenience for the graders, and we WILL impose a penalty between 10-20% (see the individual grading rubrics for the labs.)
-   There is NO GUARANTEE that late labs will be graded at all. The TA will simply start work at some point after the deadline, and grade until he/she is finished. At that time, he/she will "close the books" on that particular lab, and any work not submitted at that time will NOT be considered.

Accommodations for disabilities
-------------------------------

Students with disabilities may request academic accommodations for exams online through the UCSB Disabled Students Program at http://dsp.sa.ucsb.edu/. Please make your requests for exam accommodations through the online system as early in the quarter as possible to ensure proper arrangement.

Managing stress
---------------

Personal concerns such as stress, anxiety, relationships, depression, cultural differences, can interfere with the ability of students to succeed and thrive. For helpful resources, please contact UCSB Counseling & Psychological Services (CAPS) at 805-893-4411 or visit http://counseling.sa.ucsb.edu/ .

Responsible scholarship
-----------------------

Honesty and integrity in all academic work is essential for a valuable educational experience.  The Office of Judicial Affairs has policies, tips, and resources for proper citation use, recognizing actions considered to be cheating or other forms of academic theft, and students’ responsibilities, available on their website at: http://judicialaffairs.sa.ucsb.edu.  Students are responsible for educating themselves on the policies and to abide by them.

Furthermore, for general academic support, students are encouraged to visit Campus Learning Assistance Services (CLAS) early and often. CLAS offers instructional groups, drop-in tutoring, writing and ESL services, skills workshops and one-on-one consultations. CLAS is located on the third floor of the Student Resource Building, or visit http://clas.sa.ucsb.edu


<div style="page-break-before:always" markdown="1">

![Python cartoon](https://foo.cs.ucsb.edu/8wiki/LocalImages/python.jpg)

(Image credit: Randall Munro http://xkcd.com/353/)

Standard Disclaimer
-------------------

This syllabus is as accurate as possible, but is subject to change at
the instructor's discretion, within the bounds of UC policy.

(end of syllabus)

</div>


