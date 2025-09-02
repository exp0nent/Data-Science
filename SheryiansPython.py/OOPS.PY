# What is OOPS :-> 
# 1. For understanding oops first lets see what we were doing in python for creating a program of addition we first use imperative approach.
"""
a=12
b=13
print(a+b)
"""
#This approach is simple just use 2 variables and add them one problem with this is you have to make 2 other variables for adding 2 other numbers

# 2. Next approach is using functions to add 2 numbers this is functional approach
"""
def addition (a,b):
    return a+b
print(addition(12,23))
print(addition(54,87))
"""
# Here the good thing is we can add multiple numbers without using multiple variables.

# 3. And our next approach is object oriented programming approach.
# (a) OOPS (Object-Oriented Programming System) is a programming paradigm based on the concept of "objects", which can contain data (attributes) and code (methods)
# (b) I know it is tough to understand right now but it will be easy after learning there are many concepts that we have to learn like classes, objects , Encapsulation, inheritance, Polymorphism, etc.

'''class Addition:
    def __init__(self,a,b):
        print(a+b)
obj=Addition(12,12)'''

#Classes: A class is like a blueprint or template for creating objects 
#Think of a class like the blueprint of a house. It defines what the house should have (rooms, windows, etc.) but doesn’t build the house. An object is the actual house built using that blueprint.
'''Creating a class is super simple now lets see what is inside class. 
There are 2 types of things inside class Attributes and Methods.

1. Attributes - Variables defined inside the class are Attribute
2. Methods - Functions defined inside a class are Methods.
'''
'''class Factory:
    a= 12 # This is attribute

    def hello(self): #This is Method
        print("hello how are you")
    print("hello how are you i am getting initialized")

print(Factory().a)
Factory().hello()
'''

'''class Factory:
    a= 12 # This is attribute

    def hello(self): #This is Method
        print("hello how are you")

obj= Factory() # this is a object.

print(obj.a)
obj.hello()
obj2=Factory()'''

# Constructor:-> A constructor is a method that runs automatically when we call a class and this constructor function will target the objects location.
'''class Factory:  
    def __init__(self, material,zips,pockets):
        self.material=material
        self.zips=zips
        self.pockets= pockets
    def show(self):
        print(f"your objects details are {self.material},{self.pockets},{self.zips}")    

reebok= Factory("leather", 3 , 2)
campus= Factory("plastic", 2, 3)

print(campus.pockets)
print(reebok.material)
reebok.show()'''

# Types of Attribute
# 1) Class attribute - A normal variable created inside a class is is a class attribute and thats it.
# 2) Instance attribute - A attribute created using an instance like self.name, self.age etc. It is known as instance attribute.
'''class car:
    wheels= 4 # it is a class attribute.

    def __init__(self, color):
        self.color=color # it is a instant attribute'''


# Types of Methods:
# 1) Instance Method -> An instance method Works with instance (object) of the class. This method can access and modify instance attributes.
'''class MyClass:
    def instsnt_method(self):
        print("This is a instant method")'''


# 2) Class Method -> This method works with the class itself it will not target the instance (object). we have to use @classmethod decorator for creating the class method and it takes cls as their first parameter.
'''class MyClass:
    @classmethod
    def class_method(cls):
        print("This is a class method")'''

# 3) Static Method -> This method doesn’t access class or instance directly it also uses a decorator @staticmethod it just acts like a regular function placed inside a class. 

'''class MyClass:
    @staticmethod
    def static_method():
        print("This is a static method")'''

'''class Animal:
    name = "lion" # Class attribute

    def __init__(self, age):
        self.age=age #instante attribute
    
    def show(self):
        print(f"how are you, your age is {self.age}") # instant method

    @classmethod
    def hello(cls):
        print("How are you brother") #class method
    
    @staticmethod
    def static():
        print("how are you")


obj=Animal(12)

obj.show()
obj.hello()'''

#Inheritance:-> In general terms Inheritance means property or any possession that comes to an heir But our python neither have an old man or a child then inheritance works where? 
# 1) It works between classes.
# 2) Inheritance allows a class (child class) to inherit properties and behaviors (attributes and methods) from another class (parent class)
# 3) Benefits of using inheritance is 3:-> Code reusability, Organized structure, Easy to maintain and extend

'''class Factoryinmumbai: # Parent class/Super class
    a = "i am an attribute mention inside a factory"

    def hello(self):
        print("hello i am a method mention inside a factory")

class Factoryinpune(Factoryinmumbai): # Child class /Subclass
    pass

obj= Factoryinmumbai()
obj2= Factoryinpune()

print(obj.a)
print(obj2.hello())
'''

# Constructor in Inheritance:-> 
# Lets say you have created a parent class with a constructor function inside it and then this class is inherited by another class then 
# the constructor function of parent class will work for the child class as well. 

'''class Animal:
    def __init__(self,name):
        self.name = name

    def show(self):
        print(f"hello your name is {self.name}")

class Human(Animal):
    pass

person1 = Human("Akash")
Animal1 = Animal("Lion")

person1.show()'''

# Now lets say you need a new parameter in your child class you have to create a constructor function for your child class but the 
# parameters that can be initialized in the parent class will be initialized using the super() function. Super function will target the parent class.

'''class Animal:          #  (8:15 VIDEO)
    def __init__(self,name):
        self.name = name

    def show(self):
        print(f"hello your name is {self.name}")

class Human(Animal):
    def __init__(self, name,age):
        super().__init__(name)
        self.age= age
        
    def show(self):
        print(f"hello your name is {self.name} and your age is {self.age}")

person1 = Human("Atir", 23)
Animal1 = Animal("Lion")

person1.show()'''

# Types of Inheritance
# Single Inheritance):-> All the inheritance we saw above was single level.
# Multiple Inheritance:-> Multiple Inheritance means there will be 2 parent classes and only 1 child class and the child class will inherit all the attributes and methods of both parents. Note - The constructor function will be inherited of the first class that has been Inherited. This is MRO(Method Resolution Order) followed by python
# Multilevel Inheritance:-> This is a basic case where we will have grandparent class → parent class → child class The attributes and methods are passed on through all the classes.

# Multiple inheritance
'''class Animal:
    def __init__(self,name):
        pass
class Human:
    def __init__(self,name,age):
        pass
class Robots(Animal,Human):
    name3="Charli123"

obj = Robots()'''

# Multilevel Inheritance
'''class Factory:
    def __init__(self,material,zips):
        self.material = material
        self.zip = zips
class BhopalFactory(Factory):
    def __init__(self, material, zips, color):
        super().__init__(material, zips)
        self.color=color
class PuneFactory(BhopalFactory):
    def __init__(self, material, zips, color, pocket):
        super().__init__(material, zips, color)
        self.pocket=pocket

obj = PuneFactory("polister",3,"black",3)
print(obj)'''


# POLYMORPHISM: Polymorphism is a core concept in Object-Oriented Programming (OOP). The word means "many forms" and in programming, 
# it allows the same interface or method name to behave differently depending on the object or context.

# Types of Polymorphism:-> A same name having many different form.
# Polymorphism can be achieved in python in two ways well if we talk about compile time languages there are 3 ways but python does not support Method overloading

# 1) Method overloading means having same name methods inside a class but parameters will be different but in python the latest definition will overwrite the previous one.

# 2) Method Overridingo:-> This is where a child class overrides a method of the parent class, and Python decides at runtime which method to call, based on the object type.
# Example of Method Overiding: If we have one class that you have parent class and a another class that is child class. parent class and 
# child class have a same name method now if the object is calling the method the method is call for our child clssss.
'''class Animal:                             ^
    def show(self):                          |
        print("hello i am Aatir Ali")        |
class Human(Animal):                         |
    def show(self):  #           This is overriding senirio
        print("how are you")

obj=Human()
obj.show() 
'''

# Duck Typing:->  Python follows the philosophy  If it walks like a duck and quacks like a duck, it must be a duck.
'''class Animal:
    def show(self):
        print("I am showing")
class Human:
    def show(self):
        print("hello i am also showing")

obj = Animal()
obj2 = Human()

obj.show()
obj2.show()'''
# In the speak() function, we don’t care if it's a Duck or a Human we only care that the object has a talk() method.

# Encapsulation:
'''Encapsulation means putting data (variables) and code (functions) together in one place inside a class.
It also means hiding the internal details of how things work, and only showing what is needed.
It keeps data safe from being changed by mistake.
It makes your code clean and easy to use.
It gives control over what others can access or change.'''

'''class Factory():
    a="pune"

    def show(self):
        print("hello i am pune factory")

obj = Factory()

print(obj.a)'''

#  Access modifiers in python:->  Access modifiers means how we give access of our attributes and methods to the object or inherited classes. There are 3 types lets see them one by one.
''' 1. Public Attributes and Methods.
        Till now every attribute and methods we have created are
        public means the inherited classes and objects can access them no matter what.'''

'''class Factory():
    a="pune"

    def show(self):
        print("hello i am pune factory")

class Bhopal(Factory):
    def show2(self):
        print(super().a)
obj = Bhopal()
obj.show2()'''


'''2. Protected Attributes and Methods.
        python protected members are created using a single underscore but it still can be accessed from outside the class so you might wonder whats the point of using them.
        python doesn't enforce protected access like other languages (e.g., Java or C++). But it uses a naming convention to tell developers.'''

'''class Factory():
    _a="pune"

    def _show(self):
        print("hello i am pune factory")

class Bhopal(Factory):
    def show2(self):
        print(super()._a)

obj = Bhopal()
obj.show2()'''

'''3. Private Attributes and Method.
A private variable or method means:->  It cannot be accessed from outside the class only from inside the class where it is defined.
In Python, we use two underscores (__) before the name to make it private.'''

'''class Factory():
    __a="pune"

    def __show(self):
        print("hello i am pune factory")

class Bhopal(Factory):
    def show2(self):
        print(super().__a)

obj = Bhopal()
obj.show2()'''

'''class Factory():
    __a="pune"

    def __show(self):
        print("hello i am pune factory")

obj = Factory()
print(obj.__a)'''

'''Example:
class Demo:
    def __init__(self):
        self.name="public member"  #Public
        self._age=21               #Protected
        self.__salary=50000        #Private
    def show(self):
        print("inside the class:")
        print("public:", self.name)
        print("protected:", self._age)
        print("private:", self.__salary)'''


# Abstraction:
'''Abstraction does not exist in python but we can achieve it using a library we will see what is a library later.
Abstraction is used to simplifying complex systems by focusing on essential features and hiding unnecessary details.
It is used to define a common interface for different subclasses.'''

# Abstract classes and methods 
'''Abstract classes are classes that contains one or more abstract methods. A method that is defined but not implemented in the abstract class. 
subclasses must provide the implementation.'''

'''from abc import ABC, abstractmethod

class abstract(ABC):
    @abstractmethod
    def perimeter(self):
        pass
    @abstractmethod
    def area(self):
        pass

class Square(abstract):
    def __init__(self, side):
        self.side=side

class Circle(abstract):
    def __init__(self, radius):
        self.radius=radius

    def perimeter(self):
        print("i have created rerimeter")

    def area(self):
        print("i have created area also")

obj= Circle(7)'''

# What are Dunder methods
'''Dunder methods are special methods in Python that start and end with double underscores, like __init__, __str__, __add__, etc.
They automatically get called when you perform certain actions on an object
They help you Customize behavior of your class & Make your class objects behave like built-in data types (like strings, lists, etc.'''

'''class Animal:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return f"hello how are you and your name is {self.name}"
obj=Animal("lion")
print(obj)'''

'''class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"hello how are you and your name is {self.name}"
    
    def __add__(self,other):
        return f"your sum of ages are {self.age + other.age}"
    
obj=Animal("lion",8)
obj2=Animal("Girraf",23)
print(obj+obj2)'''

#-----------------------------------------------------------------------------------#
# Decorator
"""A decorator is just a function that modifies another function without changing its actual code.F
Imagine you have a cake (your function). A decorator is like putting icing on the cake. It doesn’t change the cake itself, but makes it better, prettier, or adds some new flavor.
For creating a decorator you first have to create a decorator functions and then inside that we will create a wrapper.
Its tough to understand with text see the video."""

"""def decorate(func):
    def wrapper(a,b):
        print("the addition to your naumber are")
        func()
        print("thank you i hope you liked it")
    return wrapper

@decorate
def addition(a,b):
    print(f"your total is {a+b}")

addition(12,67)"""

# Args and Kwargs
'''1.They’re keywords in Python used in function definitions to accept a flexible number of arguments
2.Now you always don’t have to use Args and Kwargs the main thing is * , ** you can use any names in front of them.
3.so *args are used for multiple positional arguments, and **kwargs are used for multiple key word arguments.
4.And the *args becomes a tuple and **kwargs becomes a dictionary.
5.The use case is great:-
a)You don’t need to know how many inputs you'll get%
b)Helps in building flexible functions, decorators, APIs, and more.'''

'''def addition(*args):
    sum=0
    for i in args:
        sum = sum+i
    print(sum)

addition(12,67,12,43)'''

'''def addition(**kwargs):
    print(kwargs)

addition(a=12,b=67,c=12,d=43)'''

'''def information(**kwargs):
    print("your information is\n\n")
    for i in kwargs:
        print(f"{i}:{kwargs[i]}")

information(name="aatir", age=23, desigination="test engineer")'''


'''def decorate(func):
    def wrapper(*args,**kwargs):
        print("the addition to your naumber are")
        func(*args,**kwargs)
        print("thank you i hope you liked it")
    return wrapper

@decorate
def addition(a,b):
    print(f"your total is {a+b}")

addition(12,67)'''

# List, Dictionary and set comphrehension
# All of these Comprehensions are used to create List, Dictionary and set. But you don’t have to use multiple lines of code for loops and If-Else statements

'''l=[i for i in range(1,21) if i % 2==0] # For list
print(l)'''

'''l={i : i**2 for i in range(1,10)}  # For Dictonary 
print(l)'''

# Lambda Function
'''A lambda function is an anonymous, inline function defined using the lambda keyword. It's often used for short, simple functions that are used only once or temporarily.
You can have multiple arguments but there will be only one expression.'''

'''addition= lambda a,b: a+b
print(addition(12,13))'''

'''ODDOREVEN= lambda a: "even" if a%2==0 else "odd"
print(ODDOREVEN(13))'''

# Map filter and zip 
# Map is used for applying a function to multiple items.
# Takes a list (or any sequence)
# Applies the same function to every item in that list.
# Gives you back a new list (in Python 3, it gives a map object which you can convert to a list)
# Use map() when you want to transform every item in a list
# It doesn’t remove or skip items (that’s what filter() does)
# You can use it with lambda or normal functions.

'''a = [1,2,3,4,5]

result = map (lambda x: x*2,a)

print(list(result))'''

# Filter as the name suggest is used to filter out the stuff.
# Takes a list (or other sequence Checks each item using a function (a test) Keeps only the items that pass the test (i.e., return True)

'''def even(x):
    if x%2==0:
        return True
    else:
        return False
a= [1,2,3,4,5,6,7,8,9,8,7,6]
result=filter(even,a)
print(list(result))
'''

'''a= [1,2,3,4,5,6,7,8,9,8,7,6]
result=filter(lambda x: True if x%2==0 else False,a)
print(list(result))'''

# Modules and packages 






