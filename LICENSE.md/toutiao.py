import requests

from bs4 import BeautifulSoup

res=requests.get('http://www.sina.com.cn/')

res.encoding='utf-8'

soup=BeautifulSoup(res.text,'html.parser')

alink=soup.select('.top_newslist')  
for link in alink:
             
    if len(link.select('a'))>0:
     
     a=link.select('a')[0].text
     b=link.select('a')[1].text
     c=link.select('a')[2].text
     d=link.select('a')[3].text
     e=link.select('a')[4].text
     f=link.select('a')[5].text
     print a
   
     print b   
     print c
  
     print d
  
     print e
   
     print f  
	