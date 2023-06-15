#!/usr/bin/env python
# coding: utf-8

# # Python Programming Assignment_2

# Question 1. Write a Python program to convert kilometers to miles?

# #Answer  1 kilometre equals 0.62137 miles. 
# 
# Miles = kilometre * 0.62137
# 
# And,  
# Kilometre = Miles / 0.62137  

# In[1]:


#kilometer input
kilometers = float(input("Enter value in kilometers: "))

# conversion factor
conv_fac = 0.621371

# calculate miles
miles = kilometers * conv_fac
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))


# Question 2.Write a Python program to convert Celsius to Fahrenheit?

# #Answer . We can input the degree Celsius temperature and apply
# the conversation formula of degree Fahrenheit from degree Celsius and display it on screen.
# The following is the relationship of degree Celsius and degree Fahrenheit.
# 
# T(°Fahrenheit)=(T(°Celsius)*1.8)+32
# 
# OR we can write:
# 
# T(°Fahrenheit)=(T(°Celsius)*9/5)+32
# 
# 

# In[2]:


celsius = float(input("Temperature value in degree Celsius: " ))  
  
# For Converting the temperature to degree Fahrenheit by using the above  
# given formula  
Fahrenheit = (celsius * 1.8) + 32  
    
# print the result  
print('The %.2f degree Celsius is equal to: %.2f Fahrenheit'  
      %(celsius, Fahrenheit))  
  
print("----OR----")  
celsius_2 = float (input("Temperature value in degree Celsius: " ))  
Fahrenheit_2 = (celsius_2 * 9/5) + 32  
    
# print the result  
print ('The %.2f degree Celsius is equal to: %.2f Fahrenheit'  
      %(celsius_2, Fahrenheit_2))  


# Question 3.Write a Python program to display calendar?

# In[3]:


#Answer.

import calendar  
# Enter the month and year  
yy = int(input("Enter year: "))  
mm = int(input("Enter month: "))  
  
# display the calendar  
print(calendar.month(yy,mm))  


# Question 4. Write a Python program to solve quadratic equation?
# 
# Answer. The standard form of a quadratic equation is:
# 
# ax2 + bx + c = 0, where
# 
# a, b and c are real numbers and
# 
# a ≠ 0
# 
# The solutions of this quadratic equation is given by:
# 
# (-b ± (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

# In[5]:


# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module

import cmath

a = float(input('Enter a:'))  
b = float(input('Enter b:'))  
c = float(input('Enter c:'))  

# calculate the discriminant

d = (b**2) - (4*a*c)

# find two solutions

sol1 = (-b-cmath.sqrt(d))/(2*a)

sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))


# Question 5. Write a Python program to swap two variables without temp variable?
# 
# Answer.

# In[6]:



# Python code to swap two numbers
# without using another variable
 
 
x = float(input())
y = float(input())
 
print ("Before swapping: ")
print("Value of x : ", x, " and y : ", y)
 
# code to swap 'x' and 'y'
x, y = y, x
 
print ("After swapping: ")
print("Value of x : ", x, " and y : ", y)


# In[ ]:




