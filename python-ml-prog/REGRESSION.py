#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[69]:


li={"crim":[0.00632,0.02731,0.02729,0.03237,0.06905],"zn":[18.0,0.0,0.0,0.0,0.0],"indus":[2.31,7.07,7.67,2.18,2.16],"max":[0.0538,0.469,0.0469,0.0459,0.456],"mode":[24.0,21.6,34.7,33.4,36.2]}
data=pd.DataFrame(li)


# In[70]:


y=data[["mode"]]


# In[71]:


x=data[["crim"]]


# In[72]:


from sklearn.linear_model import LinearRegression


# In[73]:


from sklearn.model_selection import train_test_split


# In[75]:


lr=LinearRegression()


# In[76]:


lr.fit(x_train,y_train)


# In[77]:


y_predict=lr.predict(x_test)


# In[78]:


y_test.head()


# In[79]:


y_predict[0:5]


# In[80]:


from sklearn.metrics import mean_squared_error


# In[81]:


mean_squared_error(y_test,y_predict)


# x=data[["indus"]]

# In[82]:


x=data[["indus"]]


# In[83]:


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)


# In[84]:


lr2=LinearRegression()


# In[85]:


lr2.fit(x_train,y_train)


# lr

# In[86]:


y_pred2=lr2.predict(x_test)


# In[90]:


from sklearn.metrics import mean_squared_error


# In[92]:


li2={"crim":[0.00632,0.02731,0.02729,0.03237,0.06905],"zn":[18.0,0.0,0.0,0.0,0.0],"indus":[2.31,7.07,7.67,2.18,2.16],"max":[0.0538,0.469,0.0469,0.0459,0.456],"mode":[24.0,21.6,34.7,33.4,36.2]}
li2


# In[93]:


data1=pd.DataFrame(li2)
data1


# In[94]:


y=data1[["mode"]]


# In[95]:


x=data1[["crim"]]


# In[96]:


from sklearn.linear_model import LinearRegression


# In[99]:


from sklearn.model_selection import train_test_split


# In[103]:


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)


# In[107]:


lr=LinearRegression()


# In[108]:


lr.fit(x_train,y_train)

y_predict=lr.predict(x_test)
# In[109]:


y_test


# In[110]:


x_test


# In[111]:


x_train


# In[112]:


y_test.head()


# In[113]:


y_predict


# In[117]:


from sklearn.metrics import mean_squared_error


# In[119]:


mean_squared_error(y_test,y_predict)


# In[120]:


x=data1[["zn"]]


# In[123]:


from sklearn.linear_model import LinearRegression


# In[124]:


from sklearn.model_selection import train_test_split


# In[126]:


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.4)


# In[127]:


x_train


# In[128]:


x_test


# In[129]:


y_test


# In[130]:


li2=LinearRegression()


# In[132]:


li2.fit(x_train,y_train)


# In[133]:


y_train


# In[134]:


y_predict=li2.predict(x_test)


# In[135]:


y_predict


# In[136]:


y_test


# In[137]:


from sklearn.metrics import mean_squared_error


# In[138]:


mean_squared_error(y_test,y_predict)


# In[140]:


li={"crim":[0.00632,0.02731,0.02729,0.03237,0.06905],"zn":[18.0,0.0,0.0,0.0,0.0],"indus":[2.31,7.07,7.67,2.18,2.16],"max":[0.0538,0.469,0.0469,0.0459,0.456],"mode":[24.0,21.6,34.7,33.4,36.2]}
data3=pd.DataFrame(li)


# In[141]:


li


# In[142]:


data3


# In[143]:


y=data3[["mode"]]


# In[144]:


x=data3[["max"]]


# In[145]:


from sklearn.linear_model import LinearRegression


# In[147]:


from sklearn.model_selection import train_test_split


# In[149]:


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)


# In[150]:


l2=LinearRegression()


# In[152]:


l2.fit(x_train,y_train)


# In[153]:


y_predict=l2.predict(x_test)


# In[154]:


y_test


# In[155]:


y_predict


# In[156]:


from sklearn.metrics import mean_squared_error


# In[157]:


mean_squared_error(y_test,y_predict)


# In[1]:


import pandas as pd


# In[2]:


d={"cr":[0.009,9.9,3.3,0.444,0.5],"mean":[12,32,44,55,44],"rs":[0.04,0.09,.4,0.5,0.99]}


# In[23]:


dataframe=pd.DataFrame(d)


# In[24]:


dataframe


# In[26]:


from sklearn.linear_model import LinearRegression


# In[27]:


y=dataframe[['mean']]


# In[28]:


x=dataframe[['cr']]


# In[29]:


from sklearn.model_selection import train_test_split


# In[31]:


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)


# li1.fit(x_train,y_train)

# In[32]:


linear=LinearRegression()


# In[33]:


linear.fit(x_train,y_train)


# In[37]:


y_predict=linear.predict(x_test)


# In[38]:


y_test


# In[39]:


y_predict


# In[41]:


from sklearn.metrics import mean_squared_error


# In[42]:


mean_squared_error(y_test,y_predict)


# 
