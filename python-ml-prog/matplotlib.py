#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


from matplotlib import pyplot as pip


# In[3]:


n1=np.arange(11)


# In[4]:


n2=n1*2


# In[5]:


n3=n1*3 


# In[ ]:





# In[6]:


student={"vikanshu":23,"ramesh":12,"suresh":1}
n1=[]
n2=[]
n1=student.keys()
n2=student.values()


# In[ ]:





# In[7]:


pip.bar(n1,n2,color='g')
pip.title("distribution of student")
pip.xlabel("name of student")
pip.ylabel("mark of student")
pip.show()
 


# for plot the scatter which draw only point

# In[20]:


n1=[1,2,3,4,5,6]
n2=[4,5,6,7,8,9]
n3=[7,6,3,2,2,1]


# In[22]:


pip.scatter(n1,n2,marker='*',color='r',s=100)
pip.scatter(n1,n3,color='g',s=200)
pip.show()


# sub plot of scater graph
# 

# In[25]:


pip.subplot(1,2,1)
pip.scatter(n1,n2,marker='*',color='r',s=100)
pip.subplot(1,2,2)
pip.scatter(n1,n3,color='g',s=200)
pip.show()


# histogram------->numerical value||||||barchart---->>categorial value
# 

# In[32]:


n1=[1,2,3,4,4,4,4,4,5,6,6,6,6,6,6,7,8,8,8,8,8,8,8,9]
pip.hist(n1,color='g',bins=10)
pip.show()


# In[33]:


import pandas as pd


# In[34]:


n1=pd.DataFrame({"length":[4,5,6,7,8,9],"volume":[5,3,3,3,3,3]})
n1


# In[35]:


n1.head()


# In[39]:


pip.hist(n1['length'],bins=4)
pip.show()


# li=[[1,2,3,4,4,3,2],[6,5,4,3,2,6,2],[1,2,3,4,5,6,7]]
# pip.boxplot(li)
# pip.show()

# In[43]:


li=[[1,2,3,4,4,3,2],[6,5,4,3,2,6,2],[1,2,3,4,5,6,7]] 
pip.boxplot(li) 
pip.show()


# In[47]:


pip.violinplot(li,showmedians=True)
pip.show()


# pie-charts

# In[68]:


name={"apple":78,"grapes":12,"bnanana":23}
n1=list(name.keys())
n2=list(name.values())


# In[73]:


pip.pie(n2,labels=n1,autopct='%.1f%%',colors=['yellow','red','green'])
pip.show()


# In[81]:


pip.pie(n2,labels=n1,radius=2,autopct="%.1f%%",colors=['r','g','b'])
pip.pie([1],colors=['y'],radius=1)
pip.show()


# In[106]:


x=[1,2,3,4,5,6]
y=[2,4,6,8,10,12]
z=[5,4,3,3,2,1]
e=[x,y]
pip.plot(x,y,color='r')
pip.plot(x,z)


# In[107]:


pip.subplot(1,2,1)
pip.plot(x,y,color='r',linestyle=':',linewidth='12')
pip.title("first graph")
pip.xlabel("x-axis")
pip.ylabel("y-axis")
pip.subplot(1,2,2)
pip.title("second graph")
pip.xlabel("x-axis")
pip.ylabel("y-axis")
pip.plot(x,color='b')
pip.show()


# In[108]:


pip.bar(x,y)


# In[109]:


pip.scatter(x,y,marker='*',color='r',s=200)
pip.scatter(x,z,color='g')


# In[110]:


pip.violinplot(x)


# In[112]:


pip.violinplot(e)


# In[117]:


a=[1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3]
pip.hist(a,bins=3)


# In[119]:


d={"men":45,"women":34,"child":90}
sex=list(d.keys())
value=list(d.values())


# In[124]:


pip.pie(value,labels=sex,autopct="%.2f%%",colors=['r','g','b'])
pip.show()


# In[129]:


pip.pie(value,labels=sex,radius=2,autopct="%.2f%%")
pip.pie([1],colors=['black'],radius=1)


# In[ ]:




