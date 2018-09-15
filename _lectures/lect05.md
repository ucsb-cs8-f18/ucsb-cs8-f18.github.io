---
num: "Lecture 5"
desc: "Remote Login via ssh, Boolean expressions, Conditionals if-else"
ready: true
date: 2017-10-16 12:30:00.00-7:00
---

# Resources from lecture

* [Link to all code written in lecture](https://github.com/ucsb-cs8-f17/cs8-f17-lecture-code)

* [Link to lecture slides and peer instruction questions](https://drive.google.com/drive/folders/0BxIvQwpl4ocoRy1Pa041SThLUFU?usp=sharing)

* [Guidelines for using peer instruction - thanks to Dan Zingaro](https://drive.google.com/file/d/0BxIvQwpl4ocoX2ZpUjJDZW52Wlk/view?usp=sharing)

# Announcements:
* Upcoming lab- Tuesday 10/17: Drawing basic shapes using turtle - [lab03](/lab/lab03/)
* In class assignment [ic02](/hwk/ic02/) - worksheets will be given out during Tuesday labs. Complete and submit in lab. If you don't submit in lab, bring to Wed lecture and submit next week in lab.This is a companion worksheet for project01. Please read lab03, project01 and this worksheet before coming to the Tuesday labs

# Topics
* Remote Login via ssh

* <https://ucsb-cs8.github.io/topics/csil_via_macos/>

* <https://ucsb-cs8.github.io/topics/csil_via_windows/>

## For Mac OS

* Install XQuartz from https://www.xquartz.org/

* Use this, but substitute YOUR username in place of username, and any number from 01 to 48
   in place of 04:

```
ssh -X username@csil-04.cs.ucsb.edu
```

Password reset for CSIL accounts:

<https://accounts.engr.ucsb.edu>

If you get this error:

```
_tkinter.TclError: no display name and no $DISPLAY environment variable
```

then either:

* (a) you forgot the `-X` on the `ssh -X` command OR
* (b) you lost the X11 part of your connection (disconnect and start over), OR
* (c) you didn't install XQuartz on Mac


# The `if __name__ == "__main__"` block

<https://ucsb-cs8.github.io/ptopics/main_blocks/>

# Other topics

* Boolean expressions
* Conditionals if-else
* Review of for loops













