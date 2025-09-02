# Multiplication of number including string
#(3)Polimorphism in function
def multiply(p1,p2):
    return p1*p2
print(multiply(2,3))
print(multiply('a',5))
print(multiply(5,'a'))

#Function return multiple values
#(4) --> Create a function that return both the area and circumference of a circle of a given its radius.
import math
def circle_stats(radius):
    area =  math.pi * radius** 2
    circumference = 2 * math.pi * radius
    return area , circumference
a , c =circle_stats(2)

print("Area: ", a, "circumference: ", c)

#(5) Default parameter value 
# Q- Write a fun that greets a user. if no name is provided, it should greet with a default name.
def greet(name = "user"):
    return "hello,"+ name + " !"

print(greet("chai"))
print(greet())

#Lambda fun
#(6) create a lambda fun to compute the cube of a no.
def add(a,b):
    return a+b
result=add(1,2)

def cube(num):
    return num ** 3
cube = lambda x: x ** 3
print(cube(3))

#Function with *Args
#(7) Write a function that takes a variable number of arguments and return their sum.

def sum_all (*args):
   # print(*args)
    print(args) #we get tuples in this case
    for i in args:
        print(i * 2)
    return sum(args)
print(sum_all(1,2,3)) 
# print(sum_all(1,2,3,4,5)) CL
# print(sum_all(1,2,3,4,5,6,7,8)) 

#Function with **kwargs
#(8)Create a function that accept any numbers of keywords arguments and print them in the format key:value
def print_kwargs(**kwargs):
    for key , value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="bob", power="dance")
print_kwargs(name="bob")
print_kwargs(name="bob", power="dance")
enemy=("dr. kumar")