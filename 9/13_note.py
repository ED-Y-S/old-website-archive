print("hello world")
print("goodbye world")
var1 = "hello"
var2 = "bye"
#var is just an element
print(var1)
print(var2)
print(var1 + " " +var2)

'''
Triple quote is for a long comment

'''
#integers, as the name suggests, don't have a place for decimals. But python can deal with decimals.
#** is exponential
x = 5 ** 9
y = 7
z = x+y
print(z)

#if it has at least a decimal, it is called a "float"
x= .1+.1+.1
print(x)

#Python is an untyped language
#each variable is not assigned a particular "type"
x = "x is str"
print(x)

import math #anything purple is a keyword; math is a package/library
a = 5
b = 1000
c = 3
formula = (-b + math.sqrt(b**2-4*a*c)/(2*a))

print(formula)

a = 10
formula = (-b + math.sqrt(b**2-4*a*c)/(2*a)) #put it here again to define the new "a". Nothing else is changed
print(formula)

#functions let us redo code without typing the code
def quadratic_formula(a,b,c):
    result = (-b + math.sqrt(b**2-4*a*c)/(2*a))
    return result
#to be lazy
x =quadratic_formula(5,1000,3)

print("quadratic formula (5,1000,3)=", x)

x = 5
print(x<10)

print("It\'s a string")#bacl slash lets you use special marks

if '':
    result = 0
else:
    result=1