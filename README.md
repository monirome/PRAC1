from selenium import webdriver
import requests
import os
from bs4 import BeautifulSoup
import urllib.request
import requests
import pandas as pd

#leemos el codigo robot.txt creamos una funcion 
def robot_txt(url):
    if url.endswith('/'):
        path = url
    else: 
        path = url + '/'
    req = requests.get(path + "robots.txt", data=None)
    return req.text
    
print(robot_txt("https://es.wikipedia.org"))
    
#elegimos la opcion del webdriver como abrirlo en modo incognito y usar el academic crawler
opcion = webdriver.ChromeOptions()
opcion.add_argument(" — incognito")
opcion.add_argument("user-agent=AcademicCrawler")

#archivo path
My_path = os.path.dirname(os.path.abspath("__file__"))

browser = webdriver.Chrome(executable_path=My_path +'/chromedriver')

url = "https://es.wikipedia.org/wiki/Anexo:Tenistas_n%C3%BAmero_1_de_la_WTA"
browser.get(url)

#revisamos el user agent
agent = browser.execute_script("return navigator.userAgent")
print(agent)

#buscamos dentro del enlace las tablas que queremos descargarnos
page = requests.get(url)

soup = BeautifulSoup(page.content, "lxml")

table = soup.find('table',{'class':'wikitable'})
links = table.findAll('a')
links

#vamos a obtener todas las tablas que hemos visto que existen en la web que tienen informacion util 
table1 = pd.read_html(url,header=0)[0]
table1.head()
table2 = pd.read_html(url,header=0)[2]
table2.head()
table3 = pd.read_html(url,header=0)[4]
table3.head()
table4 = pd.read_html(url,header=0)[6]
table4
table5 = pd.read_html(url,header=0)[7]
table5.head()
table6 = pd.read_html(url,header=0)[8]
table6.head()
table7 = pd.read_html(url,header=0)[9]
table7.head()
table8 = pd.read_html(url,header=0)[10]
table8

#guardamos cada tabla en un csv distinto 
table1.to_csv('table_1.csv', index=False)
table2.to_csv('table_2.csv', index=False)
table3.to_csv('table_3.csv', index=False)
table4.to_csv('table_4.csv', index=False)
table5.to_csv('table_5.csv', index=False)
table6.to_csv('table_6.csv', index=False)
table7.to_csv('table_7.csv', index=False)
table8.to_csv('table_8.csv', index=False)
