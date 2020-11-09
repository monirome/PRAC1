#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
import requests
import os
from bs4 import BeautifulSoup
import urllib.request
import requests
import pandas as pd


# In[2]:


#leemos el codigo robot.txt creamos una funcion 
def robot_txt(url):
    if url.endswith('/'):
        path = url
    else: 
        path = url + '/'
    req = requests.get(path + "robots.txt", data=None)
    return req.text


# In[3]:


print(robot_txt("https://es.wikipedia.org"))


# In[4]:


#elegimos la opcion del webdriver como abrirlo en modo incognito y usar el academic crawler
opcion = webdriver.ChromeOptions()
opcion.add_argument(" — incognito")
opcion.add_argument("user-agent=AcademicCrawler")


# In[5]:


#archivo path
My_path = os.path.dirname(os.path.abspath("__file__"))


# In[6]:


browser = webdriver.Chrome(executable_path=My_path +'/chromedriver')


# In[7]:


url = "https://es.wikipedia.org/wiki/Anexo:Tenistas_n%C3%BAmero_1_de_la_WTA"
browser.get(url)


# In[8]:


#revisamos el user agent
agent = browser.execute_script("return navigator.userAgent")
print(agent)


# In[9]:


#buscamos dentro del enlace las tablas que queremos descargarnos
page = requests.get(url)

soup = BeautifulSoup(page.content, "lxml")

table = soup.find('table',{'class':'wikitable'})
links = table.findAll('a')
links


# In[10]:


table1 = pd.read_html(url,header=0)[0]
table1.head()


# In[13]:


table2 = pd.read_html(url,header=0)[2]
table2.head()


# In[14]:


table3 = pd.read_html(url,header=0)[4]
table3.head()


# In[15]:


table4 = pd.read_html(url,header=0)[6]
table4.head()


# In[16]:


table5 = pd.read_html(url,header=0)[7]
table5.head()


# In[17]:


table6 = pd.read_html(url,header=0)[8]
table6.head()


# In[18]:


table7 = pd.read_html(url,header=0)[9]
table7.head()


# In[19]:


table8 = pd.read_html(url,header=0)[10]
table8.head()


# In[20]:


#guardamos cada tabla en un csv distinto 
table1.to_csv('table_1.csv', index=False)
table2.to_csv('table_2.csv', index=False)
table3.to_csv('table_3.csv', index=False)
table4.to_csv('table_4.csv', index=False)
table5.to_csv('table_5.csv', index=False)
table6.to_csv('table_6.csv', index=False)
table7.to_csv('table_7.csv', index=False)
table8.to_csv('table_8.csv', index=False)

