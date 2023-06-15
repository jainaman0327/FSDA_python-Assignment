#!/usr/bin/env python
# coding: utf-8

# # Python Programming Assignment_1

# Question 1. Write a Python program to print "Hello Python"?

# In[2]:


#Answer 1. The python programming screen is by using the print() function.

print("Hello python")


# Qustion 2. Write a Python program to do arithmetical operations addition and division.?

# In[4]:


# Answer 2. Python program to do arithmetical operation addition and division.

#This example shows the basic arithmetic operations i.e

# Store input numbers:  
num1 = input('Enter first number:')  
num2 = input('Enter second number:')

# For addition 
sum = float(num1)+float(num2)

# Display the addition  
print('The addition of {0} and {1} is {2}'.format(num1, num2, sum)) 


# For division
#Divide two numbers  
div = float(num1) / float(num2)

# Display the division  
print('The division of {0} and {1} is {2}'.format(num1, num2, div)) 



# Question 3 Write a Python program to find the area of a triangle?

# # Answer 3 . Mathematical formula:
# 
# Area of a triangle = (s*(s-a)*(s-b)*(s-c))-1/2

# In[5]:


# The semi-perimeter and a, b and c are three sides of the triangle
a = float(input('Enter first side: '))  
b = float(input('Enter second side: '))  
c = float(input('Enter third side: '))  
  
# calculate the semi-perimeter  
s = (a + b + c) / 2  

# calculate the area  
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5  
print('The area of the triangle is %0.2f' %area)   


# Question 4.Write a Python program to swap two variables?

# In[6]:


# Answer 4. # Python program to swap two variables

x = int( input("Please enter value for x:"))  
y = int( input("Please enter value for y:"))  

# create a temporary variable and swap the values
temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))


# Question 5. Write a Python program to generate a random number?

# In[10]:


#Answer 5.To generate random number in Python, randint() function is used. This function is defined in random module.

# Program to generate a random number between 

# importing the random module

import random

n = random.random()  
print(n)  


# # Note: If we run the code again, we will get the different output as follows.

# In[ ]:




