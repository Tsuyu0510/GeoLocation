#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import requests
from bs4 import BeautifulStoneSoup 
df = pd.read_csv('store_list_1.csv',encoding='utf-8')
df_1=df.iloc[0:10,1:2]
#df_2 = df.iloc[0:10,:]
df_1
locations = df_1['地址'].tolist()
locations


# In[2]:


URL = []
for i in locations:
    URL.append("https://www.google.com/maps/place?q="+i)
    


# In[3]:


## for testing 
'''import requests
from bs4 import BeautifulSoup
response = requests.get(URL[0])
soup = BeautifulSoup(response.text, "html.parser")
text = soup.prettify()
text'''


# In[5]:


# for testing 
'''initial_pos = text.find(";window.APP_INITIALIZATION_STATE")
data = text[initial_pos+30:initial_pos+85]
num_data = STR_to_NUM(data)
num_data'''


# In[6]:


##excel package didn't use
'''from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws['A1'] = 'longtitude'
ws['A2'] = 'latitide'''


# In[ ]:





# In[7]:


def STR_to_NUM(data):
    line = tuple(data.split(','))
    num1 = float(line[1])
    num2 = float(line[2])
    line = [num1,num2]
    return line


# In[8]:


def coordinations(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")
    text = soup.prettify()
    initial_pos = text.find(";window.APP_INITIALIZATION_STATE")
    data = text[initial_pos+36:initial_pos+82]## 取得經緯度後面小數點位數（尚未確認具體區別）
    num_data = STR_to_NUM(data)
    df_lat = pd.DataFrame([num_data])
    df_lat.to_csv('latlon.csv',mode='a',header=False ,index = None)
    print(num_data)


# In[9]:


## call function 
import requests
from bs4 import BeautifulSoup
for i in URL:
    coordinations(i)

    


# In[10]:


df_lat = pd.read_csv('latlon.csv',header = None)
df_lat
#df_final = pd.concat([df_2,df_lat],axis =1 ,ignore_index=True)
#df_final.dropna()


# In[ ]:





# In[ ]:




