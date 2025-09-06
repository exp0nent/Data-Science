'''print("Hello mr")

age = 12 # age= is a variables and we store 12 in that
        # We can not use number in the starting of declearing variables in the python.
        # We can not use spaces of declearing variables in the python.
        #We can not use special character of declearing variables in the python.

# There are the ways to write variables in python.
AatirAli = "Student" # This is a pascal case
aatirAli = "Student"  # This is a Camel case
aatir_ali = "Student"  # This is a Snake case

# Variables basically store data type(it is thing we store in the variables and it defines what datatype variables are)
# (1) INT
a = 12
print(type(a))

b = 2.3
print(type(b))

c = 2 + 3j
print(type(c))

# (2) STRING This is used to store anything in python, literally anything that are available on your keyboard.
a = "jack"
print(type(a))

# (2) Boolean Theres nothing much to say this is the data type which will and always give the result of True and False.
x = True
print(type(x))

"""Strings"""
a = "A"
print(ord(a)) #ORD convert character to unicode number

a = 65
print(chr(a)) # Chr convert unicode number to character

# Indexing in string
a = "hello brother"
print(a[7])
print(a[-2])
print(a[3],a[8])

# String Slicing:
a = "Aatir Ali"
print(a[0:5:1])
print(a[6:9:1])

# Type Conversion [int(), float(), str(), bool()]-> this is type conversion function
a = 12
print(type(a))

a = str(12)
print(a)

a = int(a)
print(type(a))
print(a)

# Please read bool type conversion

# Explicit and implicit
# implicit: In this python automatically converts data from one data type to another
# Explicit: In this we as a user use in build function to convert one data type to another. 

a =12
print(12/3) # Example of implicit


# Operators
# (1) Arthmetic Operators (+,-,*,/,%,//,**)
a=12
b=13
print(a+b)
print(b-a)
print(a*b)
print(b/a)
print(b%a) # it give us reminder
print(b//a) # it gives us queitent

a=5
b=20
print(b//a)

print(5**20)

# (2) Assignment Operator (=,)
a = 23

# Compound assignment operation: (+=,-+,*=,/=,**=)
a =  20
a += 20
a += 40
a += 60
print(a)

#(3) Comparsion operator: (>,<,>=,<=,==,!=)
a=12
b=12
print(a==b)
print(a!=b)

print(ord("A")) #Assci Value things start from here. assci value = 65
print(ord("B")) #Assci value = 66

print("A">"B") # So, this statement is false.
print("ABC">"ACD")

# (4) Logical operator: It is used to combined multiple operation (AND,OR,NOT)

print(123>100 and 34==34)
print(123>100 or 34==34)
print(not 12==12)''' 

# Conditional Statement (if,elif,else)
# If else statement
# 1 Que
'''a = 13
if(a>10):
    print("I will do task A")
else:
    print("I will do task B")

a = 9
if(a>10):
    print("I will do task A")
else:
    print("I will do task B")'''

# 2nd [Problem]
'''Money=int(input("please provide me the money :- "))

if Money==10:
    print("I will hane a chocobar icecream")
else:
    print("I will have a mango dolly")'''

# 3rd problem
"""Money=int(input("please provide me the money :- "))

if Money==10:
    print("I will hane a chocobar icecream")
elif Money==20:
    print("I will have a mango dolly")
else:
    print("I will have a cone")"""

# Problems 1
'''a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
if a>b:
    #print("a is the gratest: " )
    print(f"{a} is the grater then {b}")
else:
    #print("b is the gratest: " )
    print(f"{b} is the grater then {a}")'''

# Problems 2
'''gen = str(input("please tell your gender as character (M or F) :- "))

if gen == "M" or gen == "m":
    print("Good morning SIR")
elif gen== "F" or gen == "f":
    print("Good morning MAM")
else:
    print("Given charater is not correct")'''

# Problems 3 Even odd number  
'''a = int(input("Enter the number:- "))

if a%2==0:
    print("a is even number: " )
else:
    print("a is odd number")'''

# Problems 4
'''name = input("Please tell your name:- ")
age = int(input("Now tell your age:- "))

if age>=18:
    print(f"hello {name} you are a valid voter")
else:
    print(f"hello {name} you are not a valid voter")'''

# Problems 5 (Leap year)
'''year = int(input("Enter the year:- "))

if year%100 == 0 and year%400 == 0:
    print("It is leap year")
elif year%100 != 0 and year%4 ==0:
    print("It is a leap year")
else:
    print("Its a normal year")'''

#Loops in python:
#range() #it is a function that store 3 thing (start , stop, step)

'''a = range(1,20,2)
for i in a:
    print(i)'''

'''for i in range(1,20,2):
    print(i)'''

'''for i in range(21):
    print(i)'''

'''for i in range(16,0,-1):
    print(i)'''

# (1)Lets print tabel of 5:-
'''for i in range(5,51,5):
    print(i)'''

'''n=int(input("Which tabel you want to print:- "))
for i in range(n,(n*10)+1,n):
    print(i)'''

# Loops for string:
# 1st method
'''a = "Sheryians"
for i in range(len(a)):
    print(a[i])

Here, range(len(a)) generates numbers from 0 to len(a)-1.
i is an index (0,1,2...).
Then a[i] picks the character at that index.
More control, because you can use the index for extra logic if needed.

#2nd method
a = "SAHERYANCE IS COOL"
for i in a:

    print(i)'''

'''Here, for i in a directly takes each character from the string.
i itself is the character ('S', 'A', 'H'...), not an index.
Cleaner and simpler if you just need characters.'''

# Break and Continue statement
'''for i in range(1,21):
    if i == 15:
        break
    else:
        print(i)'''


'''for i in range(1,21):
    if i == 15:
        continue
    else:
        print(i)'''

# For Loop pe Questions practice.......
# 1. Accept an integer and print hello world n times....

'''n = int(input("please enter the number:- "))
for i in range(n):
    print("Hello world")'''

# 2. Print natural number up to n...
'''n = int(input("Enter the number:- "))
for i in range(n):
    i = i+1
    print(i)'''

'''n = int(input("Enter the number:- "))
for i in range(1,n+1):
    print(i)'''

# 3. reverse for loop n to i....
'''n = int(input("Enter the number:- "))
for i in range(n , 0, -1):
    print(i)'''

# 4. Print the tabel
'''n = int(input("Which tabel you want to print:- "))
for i in range(1,11):
    print(f"{n} * {i} = {n*i} ")
'''

# 5. Sum up to n terms.
'''n = int(input("Enter the number:- "))
sum = 0
for i in range(1, n+1):
    sum = sum + i
    print(f"your sum is {sum}")'''

# 6. factorial 

'''n = int(input("Enter the number:- "))
fact = 1
for i in range(1, n+1):
    fact = fact * i
print(f"your Factorial is {fact}")'''

# 7. Print the sum of all even and odd number in a range separately.
'''n = int(input("Tell your number:- "))
even = 0
odd = 0
for i in range(1,n+1):
    if i%2==0:
        even = even + i
    else:
        odd = odd+i
print(f"your even and odd sum are {even}, {odd}")'''

# 8. Print all the factors of a number.
'''n = int(input("Enter the number:- "))

for i in range(1, n+1):
    if n%i == 0:
        print(i)'''

# 9. Accept a number and check if it a perfect number or not. A number whose sum of factors is equal to the number itself Ex - 6 = 1, 2, 3 = 6

'''n = int(input("Enter the number:- "))
sum = 0
for i in range(1,n):
    if n%i == 0:
        sum = sum +i
if sum == n:
    print("Perfect Number ")
else:
    print("Not Perfect Number")
'''
# 10. Check wether the number is prime or not....

'''n = int(input("Cheack the number is prime or not:- "))
count=0
for i in range(1,n+1):
    if n % i == 0:
        count = count+1
if count==2:
    print("Prime Number")
else:
    print("Not Prime Number")'''

# 11. Reverse a string without using in build functions.
'''a = "Aatiralirsh"
print(a[::-1])'''

'''a= "Aatiralirsh"
b =""
for i in range(len(a)-1,-1,-1):
    b = b+a[i]
print(b)
'''
# 12 cheack string is pallindrome or not
'''a= "NAMAN"
b =""
for i in range(len(a)-1,-1,-1):
    b = b+a[i]
if b == a:
    print("your string is pallindrome")
else:
    print("string is not pallindrome")'''

# While Loop:- 
# The while loop repeats a block of code as long as a condition is True. It is useful when the number of iterations is unknown before execution.-

'''a = 1
while a<=30:
    print("A is True")
    a= a+1
    '''
# While loop questions

# 1. Separate each digit of a number and print it on the new line.
'''a=int(input("Enter the number:- "))
while a>0:
    print(a%10)
    a= a//10'''

# 2. Accept a number and print its reverse. 
'''a=int(input("Enter the number:- "))
rev = 0
while a>0:
    rev = rev*10 + a%10
    a= a//10
print(rev)    '''

# 3. Accept a number and check if it is a pallindromic number (If number and its reverse are equal)
'''a=int(input("Enter the number:- "))
copy = a
rev = 0
while a>0:
    rev=rev*10 + a%10
    a= a//10
if copy==rev:
    print("pallindrome number")
else:
    print("not pallindrome number")'''

# 4. Create a random number using while loop.
'''import random
num = random.randint(1,10)
tries=0
while True:
    guess=int(input("Please Guess the number between 1 to 10 :- "))
    if num==guess:
        tries += 1
        print(f"you are right you guess the number is {tries} tries")
        break
    elif num<guess:
        print("go a little lower")
        tries += 1
    elif num>guess:
        print("go a little higher")
        tries += 1
    else:
        tries += 1
        print("Sorry you are wrong")
'''

# Functions 
'''Functions in Python group reusable code into a block that can be executed by calling the function name. This helps avoid repetition and makes programs modular and readable'''

'''def hello():
    print("this is a hello function i am doing hello")
hello()'''

# Parameters and arguments
# Parameters:- The thing you accept is parameters---> jaha function define hota hai ye waha hota h.
# Arguments:- The thing you provide to parameters is argument
'''def sum(a,b):
    print(f"The sum of the number is {a+b}")
sum(5,6)
sum(34,43)'''

'''def hello(name,age):
    print(f"your name is {name} and your age is {age}")

hello("akash", 28)
hello(age=30, name="aatir")'''

# Check pallindrome using function:
"""def pallindrome(st):
    rev = ""
    for i in range(len(st)-1,-1,-1):
        rev = rev + st[i]

    if rev == st:
        print("pallindrome")
    else:
        print("not a pallindrome")

pallindrome("naman")
pallindrome("cursor")
"""
# RETURN function
'''def hello():
    return "hello how are you"
print(hello())'''

# Data Stracture: 
# Data structures are used to store, organize, and manipulate data efficiently. Python provides several built-in data structures.
# And for storing multiple values we will again use variables.
# Now in python we have 4 types of in-build data structure (List, Tuple, Dictionary, Set.)

# List Powers:
'''Before starting we need to understand some of the terminology.
1) Mutability refers to whether an object's value can be changed after creation. And List allows this.
2) we know data structures are used to store multiple values so duplicates means same value occuring multiple time. List allows this.
3) List maintains ordered data structure maintains the sequence of elements as they were inserted. This means you can access elements using their position
(index).
4)List have heterogenous nature that means we can have multiple data types inside the list.'''

# List []
'''a = [12,13,14,15,45,33,3.14,True,print()]
print(a[0])
print(a[0:5:1])'''

# List traversing and methods:

# First way using index:
'''a = [12,13,14,15,45,33,3.14]
for i in range (len(a)):
    print(a[i])'''

# Second way directly on values
'''a = [12,13,14,15,45,33,3.14]
for i in a:
    print(i)'''


#help(list)

# List Methods:
'''l = [12,13,14,15,45,33,3.14]
l.append(65)
print(l)'''

'''l =[1,3,4,5]
l.insert(1,2)
print(l)'''

'''l=[1,2,3,4,5]
l.remove(1)
print(l)
'''
'''l=[1,2,3,4,5]
l[0]=10
print(l)
'''
# Questions on list:
# 1. Print positive and negative elements of a list.
'''l=[-45,67,12,-68,-69,34]

print("positive elements are ")
for i in l:
    if i>=0:
        print(i)

print("negative elements are ")
for i in l:
    if i<0:
        print(i)'''

# 2. Find mean of the list element:
'''l=[45,67,12,68,69,34,12,4]
sum=0
for i in l:
    sum = sum+i
print(sum/len(l))'''

# 3. Find the gratest element and its index too in list.
'''l=[45,67,12,68,69,34,12,4]
largest=l[0]
index=0
for i in range(len(l)):
    if l[i]>largest:
        largest=l[i]
        index=i
print(f"Your largest number is {largest} at index {index}")'''

# 4. Find the second largest element in a list.
'''l =[12,16,13,19,17]

largest = l[0]
sec_largest=l[0]
for i in l:
    if i>largest:
        sec_largest=largest
        largest=i
    elif i>sec_largest:
        sec_largest=i
print(sec_largest,largest)'''

# 5 Check list is sorted or not:

'''a=[12,13,14,15,16]

for i in range(len(a)-1):
    if a[i]<a[i+1]:
        continue
    else:
        print("your list is not sorted")
        break
else:
    print("your list is sorted")'''

# Tupple: Before starting we need to understand some of the terminology.
# Tuples are not mutable you cannot change the values of tuple.
# You can have duplicate values in tuple there are no restriction.
# Set are ordered and you can access them through index values.
# Set also have heterogenous nature and can have different types of data structure in tuple

'''a=(1,2,3,4,5)
for i in a:
    print(i)'''

'''a=(1,2,3,4,5)
for i in range(len(a)):
    print(a[i])'''

#print(type(a))

#   Tupple method:
'''1) INDEX finding method & count karne ke liye'''

'''a=(1,2,3,4,5,5,6,7,7,5,print(),"hello")

index = a.index(5)
print(index)

count = a.count(5)
print(count)'''

# Tupple unpacking:
'''a,b,c,d=(1,2,3,4)
print(a)
print(b)
print(c)
print(d)'''

# Set Powers: Before starting we need to understand some of theterminology.
"""
mutable: Sets are mutable you can change the values of set.
Duplicates: You cannot have any duplicate values in set that means every element will be unique.
Unordered - Sets are unordered and you cannot access them through index values.
Heterogenous - Set is semi-heterogenous it can store some data types like string, numbers, tuples but not everything"""

'''s={1,2,3,4,5,6}
print (type(a))'''

# Hashing
'''b=hash("hello")
print(b)'''

'''c=hash((1,2,343))
print(c)'''

# Set traversing: 
'''A set cannot be traversed using the index values cause it is unordered and has no index.
So many times it will give random values. you can watch the video for complete understanding'''
'''a={1,8,9,"hello",2,3,4,5}
for i in a:
    print(i)'''

# Set traversing methods:
'''Now set methods are very powerful cause you don’t have any indexing you cannot change the values but set is mutable so we use methods for this.
For adding and removing the elements you can use methods as follows'''

'''a = {1,2,3,4,5}
a.add(6)
print(a)
a.remove(2)
print(a)
a.pop()
print(a)
a.clear() #remove all the element
print(a)'''

# Union & Intersection
'''a={1,2,3,4,5}
b={4,5,6,7,8}
s=a.union(b)
# print(s)
t=a.intersection(b)
# print(t)
u=a.difference(b)
u=b.difference(a)
print(u)'''

#Dictionary:---> in this we perform crud operation.
#                       Before starting we need to understand some of the terminology.
# Dictionaries are mutable, meaning you can change, add, or remove key-value pairs after creation.
# Keys must be unique, but you can have duplicates in values.
# Dictionary follows insertion order.
# A dictionary can store different types of keys and values, like integers, strings, lists, or even another dictionary.

'''D={}
print(type(D))'''

'''d={1:"hello", 2:34}
print(d)
'''

# Dictionary traversing->
'''We can traverse both keys and values in dictionary, but
default loop is set on keys and you can access the values
because of keys'''

# So technically you can traverse on both keys and values at the same time

'''d={10:100,20:200,30:300,40:400}'''

'''for i in d:
    print(i) # it print keys
    print(d[i]) #it print values in the dictionary.'''


'''for i in d.values(): #it print values in the dictionary.
    print(i) '''

'''d={10:100,20:200,30:300,40:400}
d.clear()'''

# Deep & Shallow Copy

# This is a deep copy.
'''a=[1,2,3,4,5]
b=a
b[0]=10
print(a)'''

# This is a shallow copy.
'''a=[1,2,3,4,5] 
b=a.copy()
b[0]=100
print(b)'''

# Dictionary Questions
# 1. Write a Python script to merge two Python dictionaries.

'''d1={10:100,20:200,40:300}
d2={40:400,50:500,60:600}'''
'''d3=d1.update(d2)
print(d3)'''

'''for i in d2:
    d1[i]=d2[i]
print(d1)'''

#2 Write a Python program to sum all the values in a dictionary.
'''d1={10:100,20:200,30:300}
sum =0
for i in d1:
    sum = sum + d1[i]
print(sum)'''

#  3.Count the frequency of each element on a list.
'''a=[1,1,2,1,2,2,2,3,3,4,4,4,5,5,6,7,8]
d={}
for i in a:
    if i in d.keys():
        d[i]+=1
    else:
        d[i]=1
print(d)'''

#4. Write a Python program to combine two dictionary by adding values for common keys.
''' d1={10:100,20:200,40:300}
    d2={40:400,50:500,60:600}
for i in d2:
    if i in d1.keys():
        d1[i]+=d2[i]
    else:
        d1[i]=d2[i]
print(d2)'''

# Exception Handling:->  Exceptions are unexpected events or errors that occurs during the execution of a program, which disrupts the normal flow of the program.

'''a = int(input("tell your number:- "))
print(10/a)

print("ok i have done the division")'''

'''print("start")
print("10/0")  # raise zerodivisionerror
print("end")   # This line will never print'''

'''a = int(input("tell your number:- "))
try:
    print(10/a)
except ZeroDivisionError:
    print("sorry you cant divide by zero")
    
print("ok i have done the division")'''

'''a = int(input("tell your number:- "))
try:
    print(10/a)
except Exception as err:
    print(f"sorry there is an err as {err}")
else:
    print("good there is no exception")
finally:
    print("i will run no matte what")

print("ok i have done the division")'''

# Concept of value error
'''age=int(input("tell your age:- "))
try:
    if age<10 or age>18:
        raise ValueError("Your age must be b/n 10 and 18")
    else:
        print("Welcome to the club")
except Exception as err:
    print(f"an error occured as {err}")

print("the club will start soon")'''

# File handling: Any name with an extension as .pt,.eml.xml.csv is called file and many more.
