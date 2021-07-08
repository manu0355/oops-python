#!/usr/bin/env python
# coding: utf-8

# In[14]:


class Human:           #single person details class 
    name = "manoj"
    age  = 25                             #attributes
    gender = "male"
    
    def Run(self):             #function
        print("manoj is running.....")
object = Human()             #object
print(object.name, object.age, object.gender)
object.Run()   


# In[16]:


class Person:
    def __init__(self, name , age , gender):      # by init constructor we can create multiple objects with class attributes
        self.name = name
        self.age = age
        self.gender = gender
        
object = Person("manoj",25,"male")                #object is used to access of class variables
print(object.name, object.age, object.gender)
object2 = Person("yoga", 26, "male")
print(object2.name, object2.age, object2.gender)


# In[15]:


# inheritance is just like family relation
# 1 single inheritance
# by using inheritance we can access parent class through child class, but parent class cant access child class
class Parent:
    pname = "manohar"
    def Driving(self):
        print("I am driving a car")
class Child(Parent):
    name = "manoj"
    def Learning(self):
        print("I was learning a car from my father")
    
object2 = Child()
print(object2.name)
object2.Learning()
object2.pname


# In[21]:


#multi level inheritance

class Grandfather:
    def g_landproperties(self):
        print("I  have some land")
class Father(Grandfather):
    def f_landproperties(self):
        print("I belongs to my father properties")
class Child(Father,Grandfather):
    def c_landproperties(self):
        print("I belongs to my father and my grandfather properties")
        
object1 = Child()
object1.c_landproperties()
object1.f_landproperties()
object1.g_landproperties()


# In[3]:


# Hierarchical inheritance it means single base class and multiple derived class
class Father:
    def Captain(self):
        print("I am the captain of this house")
class Son(Father):
    def Player1(self):
        print("I am main player of this house")
class Daughter(Father):
    def Player2(self):
        print("I am key player of this house")

object1 = Son()
object2 = Daughter()
object1.Player1()
object2.Player2()
object2.Captain()


# In[4]:


# Multiple inheritance
class Father:
    def Captain(self):
        print("I am father of my son")
class Mother:
    def Vicecaptain(self):
        print("I am mother of my son")
class Son(Mother, Father):
    def Player(self):
        print("I am son of my father and my mother")
        
obj = Son()
obj.Vicecaptain()
obj.Captain()
obj.Player()


# In[10]:


#polymorphism means many forms
# it divides into two types compile time and Run time
"""compile time means method overloading almost as same as default parameter in functions
   Run time means method override"""
class Base:
    def add(self,a,b,c=100):
        print(a+b+c)
obj = Base()
obj.add(100,200)

class Derivedclass:
    def add(self,a,b=100):
        print(a+b)
obj = Derivedclass()
obj.add(100,200)
obj.add(100)          #here b value takes default given value 100


# In[11]:


# runtime :method override

class Base:
    def Vehicleloan(self):
        print("some due for vehicleloan")
class Derived(Base):
    def Vehicleloan(self):
        print("no due for vechicleloan")
        
obj = Derived()
obj.Vehicleloan()


# In[3]:


#abstraction method
# first we have to import ABC, abstraction method
# In this we have to put decorator abstraction method

from abc import ABC,abstractmethod

class Abstractionmethod(ABC):
    @abstractmethod
    def Running(self):
        print("yes i am running")

class Constructormethod(Abstractionmethod):
    def Running(self):
        print("changed into constructormethod")

obj = Constructormethod()
obj.Running()


# In[4]:


"""Encapsulation means wrapping of data and methods"""


# In[12]:


#Data hiding means we having public and private data to access 
# whenever we start with __(double underscore) it means hiding we cant access out of class. we can access inside a class

class Base:
    __a = 10
    b = 30
    def __Display(self):
        print(self.__a)
        print("a and b values display")
    def Show(self):
        self.__Display()

obj = Base()
print(obj.b)
obj.Show()


# In[1]:


os.getdir()


# In[3]:


import os
os.getcwd()


# In[4]:


os.path


# In[ ]:




