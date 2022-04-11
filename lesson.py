import pandas as pd
import requests
from bs4 import BeautifulSoup
from time import sleep

url='https://www.python.org/'
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')
post = soup.find('div', class_='blog-widget')

d_list = []
for li in post.find_all('li'):
  post_url = li.find('a').get('href')

  sleep(2)
  post_r = requests.get(post_url)
  post_soup = BeautifulSoup(post_r.content, 'html.parser')
  post_h3 = [h3.text for h3 in post_soup.find_all('h3')]
  d = {
    'title': li.find('a').text,
    'date': li.find('time').text,
    'url': post_url,
    'post_h3': post_h3,
  }
  d_list.append(d)

df=pd.DataFrame(d_list)

print(df)

df.to_csv('python_web_posts.csv', index=None, encoding='utf-8-sig')