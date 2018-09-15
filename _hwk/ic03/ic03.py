#!/usr/bin/env python3

def hasNoX_2(s):
    if type(s)!=str:
       return False
    for c in s:
        if c!='x' or c!='X':
           return True
    return False

def hasNoX_3(s):
    if type(s)!=str:
       return False
    for c in s:
        if c=='x' or c=='X':
           return False
        return True

def hasNoX_4(s):
    if type(s)!=str:
       return False
    for c in s:
        if c!='x' and c!='X':
           return True
        else:
           return False

def hasNoX_5(s):
    if s!=str:
       return False
    for c in s:
        if c=='x' or c=='X':
           return False
    return True

def hasNoX_6(s):
    if type(s)!=str:
       return False
    for c in s:
        if c=='x' or c=='X':
           return True
    return False

if __name__=="__main__":
    values = ["Fox","Xie","Axe","Pat",12345]
    functions = [
        hasNoX_2,
        hasNoX_3,
        hasNoX_4,
        hasNoX_5,
        hasNoX_6]

    for f in functions:
        print("")
        for v in values:
            print("{}({})={}".format(f.__name__,repr(v),repr(f(v))))
