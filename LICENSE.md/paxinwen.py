import requests

from bs4 import BeautifulSoup

res=requests.get('http://news.sina.com.cn/china/')

res.encoding='utf-8'

soup=BeautifulSoup(res.text,'html.parser')

alink=soup.select('.news-item')

for link in alink:
  
  if len(link.select('h2'))>0:
     
   h2=link.select('h2')[0].text
       
   time=link.select('.time')[0].text
        
   a=link.select('a')[0]['href']
      
   print time,h2
        
   print a