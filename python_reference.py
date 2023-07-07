#!/usr/bin/env python
# coding: utf-8

# # Python Reference Guide

# Need a quick reference guide to help you while you hack? This is no substitute for the actual course content, but here's a "cheatsheet" to help jog your memory!

# ## Handy Functions

# In[19]:


print('This will print some text')


# In[90]:


# Use string formatting ("f-strings") to insert values
name = 'Ryan'
f'My name is: {name}'


# In[31]:


# An iterable object containing sequential integers
range(0, 10)

# Iterate by steps of 2
range(0, 10, 2)


# In[28]:


# Returns the datatype of the value passed in
type(1)


# ## Math Operators

# In[2]:


# Addition
1 + 1


# In[3]:


# Subtraction
2 - 1


# In[4]:


# Multiplication
5 * 5


# In[5]:


# Division
25 / 5


# In[6]:


# Exponents 
5 ** 3


# In[7]:


# Modulus (remainder after division)
17 % 5


# ## Data Types

# In[1]:


# Integers
x = 1
type(x)


# In[2]:


# Floats
x = 1.0
type(x)


# In[3]:


# Strings
x = 'Ryan'
type(x)


# In[4]:


# Booleans
x = True
type(x)


# In[5]:


# Byte data
x = bytes(4)
type(x)


# ### Casting Datatypes

# In[85]:


# String to integer
int('1')


# In[86]:


# Float to integer
int(1.5)


# In[91]:


# Integer to float
float(1)


# In[89]:


# Integer to boolean
bool(1)


# In[88]:


# String to boolean (Anything other than an empty string is True)
bool('')


# In[92]:


# Int to string
str(1)


# In[94]:


# String to bytes, requires the encoding
bytes('🙂', 'utf-8')


# ## String Operators

# In[81]:


# String concatenation
'Ryan ' + 'Mitchell'


# In[83]:


# String multiplication
'Python'*6


# In[84]:


# Access a particular character in a string
'Python'[3]


# ## Boolean Operators

# In[62]:


# AND
print(True and True)
print(True and False)
print(False and False)


# In[64]:


# OR
print(True or True)
print(True or False)
print(False or False)


# In[65]:


# NOT 
print(not True)
print(not False)


# In[75]:


# Equality operator
5 == 5


# In[74]:


# Inequality operator
5 != 4


# In[67]:


# Less than
4 < 5


# In[71]:


# Less than or equals to 
5 <= 5


# In[68]:


# Greater than
5 > 4


# In[72]:


# Greater than or equals to
5 >= 5


# ## Control Flow

# In[ ]:





# In[24]:


if False: 
    print('This does not print')
else: 
    print('This will print')


# In[26]:


# Iterate through items in a range
for i in range(0, 5):
    print('Number: {}'.format(i))


# In[77]:


# Iterate through items in a list
for i in [1,2,3,4,5]:
    print('Number: {}'.format(i))


# In[27]:


i = 0
while i < 5:
    print('Number: {}'.format(i))
    i = i + 1


# ## Data Types

# ### Lists

# In[36]:


aList = [1,2,3,4]
type(aList)


# In[51]:


# Append item to a list
aList.append(5)
aList


# In[37]:


# List concatenation
[1,2,3] + [4,5,6]


# In[38]:


# List multiplication
[1,2] * 5


# In[43]:


# Accessing items in a list

aList = [1,2,3,4,5,6,7,8,9,10]
# Print the item at index 4
print(aList[4])

# Print the items at index 0, up to (not including) index 4
print(aList[0:4])

# If the first index is missing, it's assumed to be 0
print(aList[:4])

# If the last index is missing, it's assumed to go to the end of the list
print(aList[4:])

# Print every other item in the list
print(aList[::2])

# Print every third item in the list
print(aList[::3])


# ### Dictionaries

# In[52]:


aDict = {
    'one': 1,
    'two': 2,
    'three': 3,
}
# Add key/value pairs to dictionary
aDict['four'] = 4

# Access values by keys
print(aDict['one'])


# In[55]:


# Print all keys
print(aDict.keys())

# Print all values
print(aDict.values())

# Print all key/value pairs
print(aDict.items())


# ### Sets

# In[49]:


aSet = {1,2,3,4}

# Add an item to a set
aSet.add(5)

# Remove an item from a set
aSet.remove(2)
print(aSet)


# ### Tuples

# In[57]:


# Tuples cannot be modified
aTuple = (1,2,3,4)
aTuple


# ## Functions

# In[10]:


# Function with one argument and a return value
def aFunction(anArg):
    return anArg + 1

aFunction(5)


# In[11]:


# Different ways of calling a function with a keyword argument
def aFunction(anArg, optionalArg=1):
    return anArg + optionalArg

print(aFunction(5))
print(aFunction(5, 4))
print(aFunction(5, optionalArg=4))


# ## Classes

# In[16]:


# A simple class with one attribute and one method
class ParentClass:
    def __init__(self, val):
        self.val = val
        
    def printVal(self):
        print(self.val)
        

classInstance = ParentClass('Value for the class attribute "val"')
classInstance.printVal()


# In[17]:


# Extend the parent class to create a child class        
class ChildClass(parentClass):
    
    def printVal(self):
        print('Child class! {}'.format(self.val))
        
childInstance = ChildClass('Value for the class attribute "val"')
childInstance.printVal()   


# In[18]:


# Overriding the parent class constructor
class AnotherChildClass(parentClass):
    def __init__(self):
        super().__init__('A default value')
        
anotherChildInstance = AnotherChildClass()
anotherChildInstance.printVal()


# ## File Handling

# In[103]:


# Open a file for reading
with open('09_01_file.txt', 'r') as f:
    data = f.readlines()
print(data)


# In[ ]:


with open('test.txt', 'w') as f:
    f.write('Writing a new line\n')


# In[ ]:


with open('test.txt', 'a') as f:
    f.write('Adding a new line to the last one\n')

