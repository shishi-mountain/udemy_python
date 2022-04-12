import pandas as pd
import requests
from bs4 import BeautifulSoup
from time import sleep

d_list = []
i = 1
while True:
  url='https://doda.jp/DodaFront/View/JobSearchList.action?pic=1&ds=0&oc=0313M%2C0317M%2C0321M&so=50&ci=401307&pf=0&tp=1&page=' + str(i)
  print(url)

  r = requests.get(url)

  soup = BeautifulSoup(r.content, 'html.parser')
  post = soup.find('section', id='shStart')

  for h2 in post.find_all('h2'):
    detail_url = h2.find('a').get('href')
    sleep(0.5)
    # post_r = requests.get(post_url)
    # post_soup = BeautifulSoup(post_r.content, 'html.parser')
    # post_h3 = [h3.text for h3 in post_soup.find_all('h3')]
    d = {
      'url': detail_url,
    }
    d_list.append(d)

  print('====='+str(i)+'======')
  i += 1

  if i>10:
    break

print(len(d_list))

df=pd.DataFrame(d_list)

print(df)

df.to_csv('duda.csv', index=None, encoding='utf-8-sig')