import requests

from bs4 import BeautifulSoup

res=requests.get('http://www.youku.com/')

res.encoding='utf-8'

soup=BeautifulSoup(res.text,'html.parser')

alink=soup.select('.p-thumb')  #��class����Ϊp-thump�Ķ���
for link in alink:
              #ѭ�� ��Ϊ�кܶ���
    if len(link.select('a'))>0:
     #���������a��ǩ
     a=link.select('a')[0]['title']
  #a��ǩ�Ǹ����� �ӵ�0����ʼ ��a�е�title
     print a
    
