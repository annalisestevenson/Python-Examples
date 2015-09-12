__author__ = 'Shawn Daniel'
# returns true for integers and numbers with ".0".
# An unorthodox / alternative solution to lesson 3/15 of Codeacademy's Python course
#
#     I call it, "The math idiot solution"

float_zero = []

def is_int(x):
    if x == int(x):
        print "true"
    else:
        del float_zero[:]
        x = str(x)
        for i in x:
            if i == ".":
                float_zero.append(i)
            elif i == "0":
                float_zero.append(i)
            else:
                print "False"
                break
        else:
            if float_zero[0] == "." and float_zero[1] == "0":
                print "True"
            else:
                print "False"

is_int(-24.6)   # input numbers here to test the function