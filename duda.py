import pandas as pd
import requests
from bs4 import BeautifulSoup
from time import sleep

# 企業詳細ページURLリストを取得
d_list = []
i = 0
while True:
  i += 1
  url='https://doda.jp/DodaFront/View/JobSearchList.action?pic=1&ds=0&oc=0313M%2C0317M%2C0321M&so=50&ci=401307&pf=0&tp=1&page=' + str(i)
  print(url)
  res = requests.get(url, timeout=3, allow_redirects=False)
  print(res.status_code)
  #print(res.history)
  #res.raise_for_status()
  if res.status_code != 200:
    break

  soup = BeautifulSoup(res.content, 'html.parser')
  post = soup.find('section', id='shStart')

  for h2 in post.find_all('h2'):
    detail_url = h2.find('a').get('href')
    sleep(0.01)
    # post_r = requests.get(post_url)
    # post_soup = BeautifulSoup(post_r.content, 'html.parser')
    # post_h3 = [h3.text for h3 in post_soup.find_all('h3')]
    d = {
      'url': detail_url,
    }
    d_list.append(d)

print(len(d_list))

# 詳細ページを読んで、会社名、会社URLを取得



# CSV出力
df=pd.DataFrame(d_list)

print(df)

df.to_csv('duda.csv', index=None, encoding='utf-8-sig')