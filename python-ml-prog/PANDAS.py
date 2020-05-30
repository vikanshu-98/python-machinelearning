#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd


# In[21]:


p1=pd.Series({'r':67,'u':90})


# In[22]:


p1


# In[23]:


p1=pd.Series({'r':67,'u':90},index=['u','r'])


# In[24]:


p1


# In[25]:


p1=pd.Series({'r':67,'u':90},index=['a','b'])


# In[26]:


p1


# In[27]:


l1=[9,8,7,6,5,3]


# In[28]:


s2=pd.Series(l1)


# In[29]:


s2


# In[30]:


s2[3]


# In[31]:


s2[:5]


# In[32]:


s2[-3:]


# In[33]:


s2+5


# In[34]:


p3=pd.DataFrame({'name':['n','k','l'],'value':[9,8,7]})


# In[35]:


p3


# In[ ]:



   


# In[ ]:





# In[36]:


p3.head


# In[37]:


p3.describe()


# In[38]:


p3.tail()


# In[39]:


p3.tail()


# In[40]:


p3.head()


# In[41]:


import pandas as pd1


# In[42]:


l1=[2,3,4]


# In[43]:


pd1.Series(l1)


# In[ ]:





# In[ ]:





# In[ ]:




