import requests

from bs4 import BeautifulSoup

res=requests.get('http://www.youku.com/')

res.encoding='utf-8'

soup=BeautifulSoup(res.text,'html.parser')

alink=soup.select('.p-thumb')  
for link in alink:
              
    if len(link.select('a'))>0:
    
     a=link.select('a')[0]['title']
  
     print a
    
