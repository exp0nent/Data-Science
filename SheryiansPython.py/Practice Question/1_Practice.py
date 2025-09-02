# Q1. Write a Python program to swap two variables.
'''x=int(input("Enter  x :- "))
y=int(input("Enter  y :- "))
x,y=y,x
print(f"This  is  x = {x}  and this is y =  {y} after swaping")'''

'''x = 5
y = 7
x = x + y
y = x - y
x = x - y
print("After swapping:", x, y)'''

# Q2. Take user input and display it back to the user.
'''user_input = int(input("Enter the input:- "))

print(f"You entered {user_input} it print back and visible to you")'''

# Q3. Write a program to check if a number is even or odd.
'''x = int(input("Enter the number here:- "))
if x%2==0:
    print(f'{x} is a even number')
else:
    print(f'{x} is odd number')'''

'''def check_even_odd(x):
    if x % 2 == 0:
        return f'{x} is an even number'
    else:
        return f'{x} is an odd number'

num = int(input("Enter the number here:- "))
result = check_even_odd(num)
print(result)'''

# Q4. Create a program that prints the multiplication table of a given number.
'''for i in range(5,51,5):
    print(i)'''

'''n=int(input("Which tabel you want to print:- "))
for i in range(n,(n*10)+1,n):
    print(i)'''

#Q5. Write a program to find the largest of three numbers.
'''x=int(input("enter the first number:- "))
y=int(input("enter the second number:- "))
z=int(input("enter the third  number:- "))
if x>y and x>z:
    print(f"{x} is the gratest among them")
elif y>x and y>z:
    print(f"{y} is the gratest among them")
else:
    print(f"{z} is the gratest among them")'''

# Q6. Convert temperature from Celsius to Fahrenheit.
'''celsius = float(input("Enter temperature in celsius:- "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F")'''

# Q7. Write a program to calculate the factorial of a number using a loop.
'''x=int(input("Enter the number:- "))
fact = 1
for i in range(1,x+1):
    fact=fact*i
print(f'factorial of {x} is {fact}')'''

# Q8. Create a program to count the number of vowels in a string.
'''def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    vowels_count = 0
    for char in input_string:
        if char in vowels:
            vowels_count +=  1
    return vowels_count
input_string = input("Enter the String:- ")
print("No of vowels is:", count_vowels(input_string))'''

# Q9. Write a Python script to reverse a given string.
'''string=input("Enter the string:- ")
print(string[::-1])
'''

'''def string_reversr(s):
    return s[::-1]

string=input("Enter the string:- ")
print("This is reverse string:", string_reversr(string))'''

# Q10. Check if a number is a palindrome
'''a = int(input("Enter the no:- "))
rev= (a[::-1])
if a == rev:
    print("This is a pallindrom no")
else:
    print("This is not a pallindrom no")'''

'''a= int(input("Enter a number:- "))
copy=a
rev=0
while a>0:
    rev = rev*10 + a % 10
    a= a//10
if copy==rev:
    print("Pallinrom number")
else:
    print("Not pallindrom")'''

# Q11. Write a program to find the sum of first N natural numbers.
'''def sum_of_natural_no(n):
    sum=0
    for i in range(0,n+1):
        sum = sum+i
    return sum
n= int(input("enter the no:- "))
print(sum_of_natural_no(n))'''

# Q12. Create a number guessing game
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
        print("Sorry you are wrong")'''

# 13 . Check wether the number is prime or not....
'''n = int(input("Cheack the number is prime or not:- "))
count=0
for i in range(1,n+1):
    if n % i == 0:
        count = count+1
if count==2:
    print("Prime Number")
else:
    print("Not Prime Number")'''

'''def no_is_prime_or_not(n):
    count =0
    for i in range(1,n+1):
        if n%i==0:
            count +=i
    if count ==2:
        return True
    else:
        return False
n = int(input("Cheack the number is prime or not:- "))
if no_is_prime_or_not(n):
    print(f"{n} is a prime no")
else:
    print(f"{n} is not a prime no")'''

# Q13. Write a program to print all prime numbers between 1 and 100.
'''def prime_no(n):
    for num in range(1,n+1):
        count = 0
        for i in range (1,num+1):
            if num%i==0:
                count+=1
        if count ==2:
            print(num , end=" ")
n= int(input("enter the range (n): "))
print(f'Prime number between 1 and {n} are:') 
prime_no(n)
'''

'''def prime_no(n):
    for i in range(1,n+1):
        count = 0
        for j in range (1,i+1):
            if i%j==0:
                count+=1
        if count ==2:
            print(i , end=" ")
n= int(input("enter the range (n): "))
print(f'Prime number between 1 and {n} are:') 
prime_no(n)'''

# Q14. Check if a given year is a leap year or not.
'''n= int(input("Enter the year you want to check:- "))
if n%100==0 and n%400==0:
    print(f"{n} This is a leap year")
elif n%100!=0 and n%4==0:
    print(f"{n} This is a leap year")
else:
    print(f'{n} Sorry this is not a leap year')'''

'''def leap_year(n):
    if n%100==0 and n%400==0:
        return f"{n} This is a leap year"
    elif n%100!=0 and n%4==0:
        return f"{n} This is a leap year"
    else:
        return f'{n} Sorry this is not a leap year'
n= int(input("Enter the year you want to check:- "))
print(leap_year(n))'''

# Sum of fibonachi series:
'''n=int(input("enter the number:- "))
a ,b =0,1
sum = 0
for i in range(n):
    print(f'step {i+1}: a = {a},  b = {b}')
    sum += a
    a,b =b, b+a
print(sum)
'''
# Q15. Create a program to print the Fibonacci series up to N terms.
'''n=int(input("enter the number:- "))
a ,b =0,1
sum = 0
for i in range(n):
    print(f'step {i+1}: a = {a},  b = {b}')
    sum = a+b
    a = b
    b= sum
    print(f"this is the sum {sum}")'''

# Q16. Write a program to find the GCD of two numbers.
'''def find_gcd(a,b):
    while b !=0:
        a , b = b,  a%b
    return a
a = int(input("a:- "))
b = int(input("b:- "))
print(find_gcd(a,b))'''

# Q17. Write a program to find the LCM of two numbers.
'''def gcd(a,b):
    while b !=0:
        a , b = b,  a%b
    return a
def lcm(a,b):
    return(a*b) // gcd(a,b)

a = int(input("a:- "))
b = int(input("b:- "))

print(gcd(a,b))
print(lcm(a,b))'''



