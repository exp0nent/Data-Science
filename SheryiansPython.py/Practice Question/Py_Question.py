# 1. First N natural number
n=int(input("Enter the number you want to print: "))
i =1
while(i<=n):
    print(i)
    i=i+1

num = int(input("Enter any number : "))
print("Natural numbers from 1 to", num)
for i in range(1, num + 1):
    print(i, end=" ")

n = int(input("enter the number: "))
def printNaturalNumbers(n):
    for i in range(1, n + 1):
        print(i, end=" ")
#n = int(input("enter the number: "))
printNaturalNumbers(n)

# (2) Sum of first N natural number.
n=int(input("Enter the number: "))
i=1
sum=0
while(i<=n):
    sum=sum+i
    i=i+1
print("The sum is: ", sum)

n=int(input("enter the number: "))
sum = 0
for i in range(1,n+1):
    sum = sum+i
    i = i+1
print("The sum is this ", sum)

n=int(input("Enter the number you want to add: "))
def findsum(n):
    return n*(n+1)//2
# n=int(input("Enter the number you want to add: "))
print("The sum is: ",findsum(n))


# (3) Find the sum of square of first natural number.
n=int(input("Enter the number: "))
i=1
sum=0
while(i<=n):
    sum=sum+(i*i)
    i=i+1
print("The sum is: ", sum)

n=int(input("enter the value:"))
sum=0
for i in range (1, n+1):
     square= i*i
     sum = sum+square
print(sum)

# (4) Find the sum of first n natural number if any number in between is perfect square then add the square value.
def special_sum(n):
    sum = 0
    for i in range(1, n + 1):
        if int(i ** 0.5) ** 2 == i:  # check if perfect square
            sum += i * i
        else:
            sum += i
    return sum
n=int(input("Enter the no: "))
print(special_sum(n))

# (5) Sum the first n natural numbers, if a number is a perfect square, add its square value in addition to the number itself.
def custom_sum(n):
    total = 0
    for i in range(1, n+1):
        total += i
        if int(i ** 0.5) ** 2 == i:  # check if i is a perfect square
            total += i * i
    return total
print(custom_sum(5)) 

# (6) Find the maaximum of 3 numbers.
x=float(input("Enter first number: "))
y=float(input("Enter secont number: "))
z=float(input("enter third number: "))
if x>y:
    if x>z:
        print("the gratest no is: ", x)
    else:
        print("the gratest no is: ",z)
else:
    if y>z:
        print("the gratest no is: ",y)
    else:
        print("the gratest no is: ",z)

def max_of_3no(x,y,z):
    return max(x,y,z)
x=int(input("enter 1st no:"))
y=int(input("enter 2nd no:"))
z=int(input("enter 3rd no:"))
largest = max_of_3no(x,y,z)
print("max among them is", largest)

# (7) Check no is even or odd.
number=int(input("enter the no: "))
if(number % 2 == 0):
        print("Given no is Even")
else:
        print("Given no is Odd")

# (8) Calculate x^n
x=int(input("Enter Number: "))
y=int(input("Enter Power: "))
Ans=x**y
print("solution is: ", Ans)

x=int(input("Enter Number: "))
b=int(input("Enter Power: "))
y=x
for i in range(0,b-1):
    y=x*y
print(y)

