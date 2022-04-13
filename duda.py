import pandas as pd
import requests
from bs4 import BeautifulSoup
from time import sleep

# 企業詳細ページURLリストを取得
d_list = []
i = 0
while True:
  i += 1
  # test
  #if i>2:
  #  break

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
    d_list.append(detail_url)

# 詳細ページを読んで、会社名、会社URLを取得
company_list = []
for d_url in d_list:
  r = requests.get(d_url)
  soup = BeautifulSoup(r.content, 'html.parser')

  # 会社名
  company = soup.find('div', class_='head_detail').find('h1')
  # spanは除く
  for explain in company.find_all("span", {'class': 'explain'}):
    explain.extract()

  # 会社URL
  if (soup.find('table', id='company_profile_table') == None):
    # 開いたページが求人詳細ページではない場合、求人詳細ページURLを探す
    if (soup.find('a', class_='_canonicalUrl') == None):
      # それでも見つからない場合は、会社URLは空白にする
      company_url = ''
      break
    else:
      detail_url = soup.find('a', class_='_canonicalUrl').get('href')
      detail_r = requests.get(detail_url)
      soup = BeautifulSoup(detail_r.content, 'html.parser')

  c_profile = soup.find('table', id='company_profile_table')
  if c_profile == None:
    company_url = ''
    break
  else:
    if c_profile.find('a') == None:
      company_url = ''
      break

    company_url = c_profile.find('a').get('href')

  c_info = {
    'company': company.get_text().replace('\r\n','').replace('\n','').replace(' ', ''),
    'url': company_url,
  }
  company_list.append(c_info)

# CSV出力
df=pd.DataFrame(company_list)

#print(df)

df.to_csv('duda.csv', index=None, encoding='utf-8-sig')