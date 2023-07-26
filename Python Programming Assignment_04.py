#!/usr/bin/env python
# coding: utf-8

# # Assignment 4 Solutions

# 1.Write a Python Program to find the factorial of a number ?

# In[2]:


def factorial(num):
    if (num < 1):
        return 1
    else:
        return num*factorial(num-1)
num = int(input('Enter a number: '))
value = factorial(num)
print(f'The Factorial of {num} is {value}')


# 2.Write a Python Program to display the multiplication table ?

# In[3]:


def generateTable(base,entries):
    for x in range(1,entries+1):
        print(f'{base} X {x} = {base*x}')

num = int(input('Enter a number: '))
values = int(input('Enter no of entries: '))
generateTable(num,values)


# 3.Write a Python Program to print the fibonacci sequence ?

# In[10]:


n = int(input("Enter length of Fibonacci series: "))
num1 = 0
num2 = 1
next_number = 0
count = 1
  
while(count <= n):
    print(next_number, end=" ")
    count += 1
    num1 = num2
    num2 = next_number
    next_number = num1 + num2
    t_number = num1 + num2


# 4.Write a Python Program to check Armstrong number ?

# In[11]:


def checkArmstrongNumber():
    in_num = input('Enter a number: ')
    sum = 0
    for char in range(len(in_num)):
        sum = sum + pow(int(in_num[char]),3)
    if sum == int(in_num):
        print(f'{in_num} is a Armstrong Number')
    else:
        print(f'{in_num} is a Not Armstrong Number')

for x in range(2):
    checkArmstrongNumber()


# 5.Write a Python Program to Find Armstrong number in an interval ?

# In[13]:


def checkArmstrongNumber(in_num, storage):
    sum = 0
    for char in range(len(in_num)):
        sum = sum + pow(int(in_num[char]),3)
    if sum == int(in_num):
        storage.append(int(in_num))

start_interval = int(input('Enter the Start of the Interval: '))
end_interval = int(input('Enter the End of the Interval: '))
list_of_armstrong = []

if start_interval > end_interval:
    print("Start Interval Cannot be Greater than End Interval")
else:
    for number in range(start_interval,end_interval+1):
        checkArmstrongNumber(str(number),list_of_armstrong)
    print(f'The Armstrong numbers between {start_interval} and {end_interval} are {list_of_armstrong}')


# 6.Write a Python Program to sum of natural numbers ?

# In[14]:


def sumOfNaturalNumbers(num):
    sum = num*((num+1)/2)
    print(f'Sum of {num} natural numbers is {sum}')
    
num = int(input('Enter a number: '))
sumOfNaturalNumbers(num)

