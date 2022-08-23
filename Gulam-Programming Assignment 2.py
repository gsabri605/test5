#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('1. Write a Python program to convert kilometers to miles');get_ipython().run_line_magic('pinfo', 'miles')


# In[1]:



kilometers = float(input("Enter value in kilometers: "))

conv_fac = 0.621371

miles = kilometers * conv_fac

print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))


# In[ ]:


get_ipython().set_next_input('2. Write a Python program to convert Celsius to Fahrenheit');get_ipython().run_line_magic('pinfo', 'Fahrenheit')


# In[6]:


celsius = float (input("Enter value in celsius"))

fahrenheit = (celsius * 1.8) + 32

print('% 0.1f degree Celsius is equal to % 0.1f degree Fahrenheit' %(celsius,fahrenheit))


# In[ ]:


get_ipython().set_next_input('3. Write a Python program to display calendar');get_ipython().run_line_magic('pinfo', 'calendar')


# In[7]:


import calendar

year = int(input("Enter Year: "))

month = int(input("Enter Month: "))

print(calendar.month(year, month))


# In[ ]:


get_ipython().set_next_input('4. Write a Python program to solve quadratic equation');get_ipython().run_line_magic('pinfo', 'equation')


# In[16]:



import cmath
a=int(input("Enter a coefficents"))
b=int(input("Enter b coefficents"))
c=int(input("Enter b coefficents"))


d = (b**2) - (4*a*c)

sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))


# In[ ]:


get_ipython().set_next_input('5. Write a Python program to swap two variables without temp variable');get_ipython().run_line_magic('pinfo', 'variable')


# In[19]:



x = 7
y = 8

x = x + y
y = x - y
x = x - y


print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))


# In[ ]:




