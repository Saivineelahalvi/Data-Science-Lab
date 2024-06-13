#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt


# In[4]:


hours_studied=[10,9,2,15,10,16,11,16]
exam_scores=[95,80,10,50,45,98,38,93]
plt.plot(hours_studied,exam_scores,marker='*',color='red',linestyle='-')
plt.xlabel('hours Studied')
plt.ylabel('Score in Final Exam')
plt.title('Effect of hours Studied on Exam Score')

