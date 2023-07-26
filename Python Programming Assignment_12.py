#!/usr/bin/env python
# coding: utf-8

# # Assignment 12 Solutions

# 1.Write a Python program to Extract Unique values dictionary values?

# In[1]:


in_dict = {1:'Rishikesh',2:'Badrinath',3:'Gangotri',4:'Yamunotri',5:'Kedarnath',6:'Tirupati',7:'Kedarnath'}
print(in_dict.values())
print(f'Unique Values: {list(set(in_dict.values()))}')


# 2.Write a Python program to find the sum of all items in a dictionary?

# In[2]:


in_dict = {'Apple':10,'Mango':20,'Banana':30,'Guava':40,'PineApple':200}
print('Sum of All items: ',sum(in_dict.values()))


# 3.Write a Python program to Merging two Dictionaries?

# In[3]:


course_details = {
    'cousre_name':'Ineuron'
}
instructors = {
    'course_instructors':['Sudhanshu Kumar','Krish Naik']
}
course_details.update(instructors)
print(course_details)


# 4.Write a Python program to convert key-values list to flat dictionary?

# In[4]:


in_list = [('A',10),('B',20),('C',30),('D',40),('E',50),('F',60),('G',70),('H',80),('I',90),('J',100)]

# Method #1
dict(in_list)

# Method #2
out_dict = {}
for ele in in_list:
    out_dict[ele[0]] = ele[1]
print(out_dict)


# 5.Write a Python program to insertion at the beginning in OrderedDict?

# In[6]:


from collections import OrderedDict
dict_one = OrderedDict({'Apple':'Iphone','Microsoft':'Windows','Google':'chrome'})
print('dict_one',dict_one)
dict_two = {'Tesla':'SpaceX'}
dict_one.update(dict_two)
print('dict_one',dict_one)
dict_one.move_to_end('Tesla',last=False)
print('dict_one',dict_one)


# 6.Write a Python program to check order of character in string using OrderedDict()?

# In[7]:


from collections import OrderedDict

initial_list = {'a': 1000, 'f': 200, 'd': 300, 'c': 400, 'b': 500, 'e': 600}
print(initial_list)

final_list = OrderedDict(dict(sorted(initial_list.items())))
print(final_list)


# 7.Write a Python program to sort Python Dictionaries by Key or Value?

# In[8]:


d_items = {'Mango':100,'PineApple':22,'Banana':60,'Grape':13}

def sort_dict(in_dict,sort_type):
    if sort_type == 'key':
        print(dict(sorted(in_dict.items(), key=lambda x:x[0], reverse=False)))
    else:
        print(dict(sorted(in_dict.items(), key=lambda x:x[1], reverse=False)))
        
sort_dict(d_items,'key')        
sort_dict(d_items,'value')

