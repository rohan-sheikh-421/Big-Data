#!/usr/bin/env python
# coding: utf-8

# **Big Data Analytics Lab - Quiz Exam - Spring 2024** <br>

# All the Questions are to be solved. <br>
# 
# 

# **Part I: Find the matching substrings (Marks=3)** <br>
# 

# Write a function get_substring_positions() that accepts two strings as arguments. Return the number of the positions where they contain the same substring of length 2. For example, **"kerase"** and **"ketasee"** should yield 3, since the "ke", "as", and "se" substrings appear in the same place in both strings.

# In[1]:


#### Write your code here ####
def get_substring_positions(str1, str2):
   
    count = 0
    for i in range(len(str1) - 1):
        if str1[i:i+2] == str2[i:i+2]:
            count += 1
    return count

# testing on given example
string1 = "kerase"
string2 = "ketasee"
result = get_substring_positions(string1, string2)
print(f"Number of matching substrings: {result}")


# **Part II: Function that divides by number (Marks=2)**

# Lambda functions offer a quicker way to write functions using fewer lines of code. They behave in a
# similar way as a regular function behaves. The lambda expression is capable of returning a function. Using a lambda expression, complete the div_by_num function. This function should take an argument and return a one argument function that divides any value passed to it by the original number.
# def div_num_by(num):
# 
# <br>
# Input: x = div_num_by(15)
# <br>
# x(3)
# <br>
# Output: 5
# <br>
# Explanation :
# "Returns a function that takes one argument and returns the divisible of that
# argument." <br>

# In[6]:


### write your code here ###

def div_num_by(num):
   
    return lambda x: x / num

# testing by given example
x = div_num_by(15)
x(3)


    


# **PART III: Matplotlib** is a library that aids in creating static, animated, and interactive visualizations in Python. We
# are already familiar with its functionalities and advantages. Solve following questions related to it. <br>
# Dataset is attached dataset. company_sales_data.csv<br>
# 
# ---
# 
# 
# 
# 

# **A: Read toothpaste sales data of each month and show it using a scatter plot (Marks=2)**

# In[10]:


import pandas as pd
import matplotlib.pyplot as plt


# In[12]:


## write your code here ##
df=pd.read_csv('company_sales_data.csv')
df.head()


# In[13]:


month_numbers = df['month_number']
toothpaste_sales = df['toothpaste']

# scatter plot
plt.figure(figsize=(8, 6)) 

# Scatter plot
plt.scatter(month_numbers, toothpaste_sales, color='b', marker='o', label='Toothpaste Sales')

# labels
plt.xlabel('Month Number')
plt.ylabel('Toothpaste Sales')
plt.title('Monthly Toothpaste Sales')
plt.grid(True, linestyle='--')  

# Show plot
plt.legend()
plt.show()


# **B:Calculate total sale data for last year for each product and show it using a Pie chart (Marks=2)**

# In[16]:



# total sales 
total_sales = df.iloc[:, 1:7].sum()

# pie chart
plt.figure(figsize=(10, 7))
plt.pie(total_sales, labels=total_sales.index, autopct='%1.1f%%', startangle=140)
plt.axis('equal')

plt.title('Total Sales Data for Each Product Last Year')
plt.show()


# **Sample matplotlib code**

# In[17]:


import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
langs = ['C', 'C++', 'Java', 'Python', 'PHP']
students = [23,17,35,29,12]
ax.bar(langs,students)
plt.show()


# In[ ]:




