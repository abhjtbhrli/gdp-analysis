#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np


# In[14]:


distance = [12, 445, 50, 100]
time = [3, 24, 7, 10]


# In[15]:


dist1 = np.array(distance)


# In[6]:


time1 = np.array(time)


# In[18]:


speed = dist1/time1
print(speed)


# In[19]:


type(speed)


# In[21]:


np.zeros(10)


# In[23]:


np.ones(5)


# In[28]:


np.ones((2,2))


# In[30]:


np.array(([1,1,1],
        [1,1,1]))


# In[31]:


np.array([1,1,1])


# In[32]:


dist = [[1,1,1],
       [1,1,1]]


# In[34]:


np.array(dist) == np.array([[1,1,1],
                           [1,1,1]])


# In[39]:


np.empty((1,100))


# In[40]:


np.arange(10)


# In[42]:


np.arange(12).reshape(2,6)


# In[46]:


ax = np.arange(125).reshape(5,5,5)


# In[48]:


ax[0,4,4]


# In[50]:


ax.ndim


# In[51]:


ax.shape


# In[52]:


ax.size


# In[53]:


ax.dtype


# In[54]:


type(ax)


# In[56]:


np.array([1,2,3])+np.array([1,2,3,4])


# In[62]:


np.add(2,np.add(3,4))


# In[68]:


np.array([1,1,1,1,6]).sum() == sum(np.array([1,1,1,1,6]))


# In[87]:


new = np.array([1,1,1,3,4])
#new[new in [[1,3]]]
np.logical_and(new>0.5 & new<3)
#np.array([1,1,1,3,4])[np.array([1,1,1,3,4])>0.5 & np.array([1,1,1,3,4])<3]


# In[89]:


wwe = np.array(["Undertaker","Stone Cold","Brock Lesnar","Triple H"])


# In[91]:


print (wwe)


# In[92]:


wwe.view()


# In[95]:


wwe.copy().tolist() == wwe.tolist()


# In[96]:


wwe1 = np.array([1,2,3,4,5])


# In[100]:


np.sqrt(wwe1)


# In[101]:


np.cos(wwe1)


# In[102]:


np.floor(wwe1)


# In[106]:


np.sin(wwe1)*np.sin(wwe1) + np.cos(wwe1)*np.cos(wwe1)


# In[112]:


np.sin(wwe1).reshape(5,1).flatten()


# In[113]:


np.sin(wwe1).reshape(5,1).transpose()


# In[114]:


1+1


# In[116]:


import pandas as pd


# In[166]:


df = pd.read_csv("Countries with GDP.txt")


# In[169]:


df.columns


# In[164]:


df.iloc[0]


# In[140]:


cou = np.array([df.iloc[0,],df.iloc[2,]])


# In[141]:


cou


# In[ ]:


np.array(read)


# In[143]:


fileObject = open("Countries with GDP.txt", "r")
data = fileObject.read()


# In[144]:


data


# In[ ]:





# In[281]:


df = pd.read_csv('Countries with GDP.txt', sep="\t", header=None)


# In[282]:


df


# In[181]:


type(df)


# In[182]:


df.shape


# In[183]:


df.size


# In[191]:


df.iloc[1][0]


# In[185]:


df.iloc[3]


# In[192]:


gdp = pd.DataFrame(list([df.iloc[1],
    df.iloc[3]]))


# In[229]:


gdp["Item"].apply(lambda x: pd.Series(x.split(","))).index = ["Country","GDP"]


# In[230]:


gdp_new = gdp["Item"].apply(lambda x: pd.Series(x.split(",")))


# In[232]:


gdp_new.index = ["Country","GDP"]


# In[236]:


gdp_final = gdp_new.transpose()


# In[245]:


gdp_final["GDP"] = pd.to_numeric(gdp_final["GDP"])


# In[249]:


type(gdp_final["Country"][1])


# In[250]:


gdp_final["GDP"].argmax()


# In[255]:


print(gdp_final.loc[gdp_final["GDP"].argmax()]["Country"])


# In[257]:


print(gdp_final.loc[gdp_final["GDP"].argmin()]["Country"])


# In[269]:


for i in gdp_final.index:
    #print(i)
    print(gdp_final["Country"][i] + " - " + str(gdp_final["GDP"][i]))


# In[272]:


print("Highest GDP value is: " +str(gdp_final.loc[gdp_final["GDP"].argmax()]["GDP"]))


# In[273]:


print("Lowest GDP value is: " +str(gdp_final.loc[gdp_final["GDP"].argmin()]["GDP"]))


# In[275]:


print("Mean GDP value is: " +str(gdp_final["GDP"].mean()))


# In[277]:


print("Standard deviation of GDP values is: " +str(gdp_final["GDP"].std()))


# In[279]:


print("Sum of all GDP values is: " +str(sum(gdp_final["GDP"])))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




