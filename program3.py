#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import numpy as np


# In[16]:


books_df = pd.read_csv("BL-Flickr-Images-Book.csv")


# In[17]:


print("Original DataFrame:")


# In[18]:


irrelevant_columns = ['Edition Statement', 'Corporate Author', 'Corporate Contributors', 'Former owner',
'Engraver', 'Contributors', 'Issuance type', 'Shelfmarks']


# In[19]:


books_df.drop(columns=irrelevant_columns, inplace=True)


# In[20]:


books_df.set_index('Identifier', inplace=True)


# In[21]:


books_df['Date of Publication'] = books_df['Date of Publication'].str.extract(r'^(\d{4})', expand=False)
books_df['Date of Publication'] = pd.to_numeric(books_df['Date of Publication'], errors='coerce')


# In[22]:


print("\nCleaned DataFrame:")
print(books_df.head())


# In[ ]:





# In[ ]:




