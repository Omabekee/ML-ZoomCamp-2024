#!/usr/bin/env python
# coding: utf-8

# In[1]:


wget https://raw.githubusercontent.com/alexeygrigorev/datasets/master/laptops.csv


# In[3]:


url = 'https://raw.githubusercontent.com/alexeygrigorev/datasets/master/laptops.csv'


# In[4]:


import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('laptops.csv')

# Display the first few rows of the DataFrame
print(df.head())


# In[5]:


import os
print(os.getcwd())


# In[9]:


os.chdir('C:/Users/PC/Documents/ML-ZoomCamp')


# In[10]:


os.chdir('C:/Users/PC/Documents/ML-ZoomCamp2024')


# In[11]:


import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('laptops.csv')

# Display the first few rows of the DataFrame
print(df.head())


# In[12]:


__version__


# In[13]:


pd.__version__


# In[14]:


df.head()


# In[15]:


# Get the number of rows
num_rows = df.shape[0]
print(f"Number of records: {num_rows}")


# In[17]:


# Count the number of unique laptop brands
num_brands = df['Brand'].nunique()
print(f"Number of unique laptop brands: {num_brands}")


# In[18]:


# Check for missing values in each column
missing_values = df.isnull().sum()
print(missing_values)


# In[19]:


# Total count of missing values in the dataset
total_missing = df.isnull().sum().sum()
print(f"Total missing values: {total_missing}")


# In[21]:


# Find the maximum final price
max_final_price = df['Final Price'].max()
print(f"Maximum final price: {max_final_price}")


# In[23]:


# Get the row with the maximum final price
max_price_row = df[df['Final Price'] == max_final_price]
print(max_price_row)


# In[25]:


# Find the median screen size
median_screen = df['Screen'].median()
print(f"Median screen: {median_screen}")

