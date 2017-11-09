import requests

from bs4 import BeautifulSoup

res=requests.get('http://www.youku.com/')

res.encoding='utf-8'

soup=BeautifulSoup(res.text,'html.parser')

alink=soup.select('.p-thumb')  #找class名字为p-thump的东西
for link in alink:
              #循环 因为有很多类
    if len(link.select('a'))>0:
     #如果类中有a标签
     a=link.select('a')[0]['title']
  #a标签是个数组 从第0个开始 找a中的title
     print a
    
