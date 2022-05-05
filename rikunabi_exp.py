import pandas as pd
import requests
from bs4 import BeautifulSoup
from time import sleep
import re

# 企業詳細ページURLリストを取得
base_url = 'https://next.rikunabi.com'
company_list = []
i = 0
while True:
  # test
  if i>1:
   break

  url='https://next.rikunabi.com/rnc/docs/cp_s00700.jsp?jb_type_long_cd=0500000000&wrk_plc_long_cd=0840000000&wrk_plc_long_cd=0840300000&curnum=' + str(1+50*i)
  print(url)
  i += 1

  res = requests.get(url, timeout=3)
  res.raise_for_status()
  if res.status_code != 200:
    break

  soup = BeautifulSoup(res.content, 'html.parser')
  post = soup.select('a:-soup-contains(企業ページ)')
  for page_url in post:
    page_url = base_url + page_url.get('href')

    sleep(0.1)

    page_r = requests.get(page_url, timeout=3)
    page_r.raise_for_status()

    page_soup = BeautifulSoup(page_r.content, 'html.parser')

    company_name = page_soup.select_one('.rnn-breadcrumb > li:last-of-type')
    print('='*50)
    print(company_name.text)
    # aがrnn-col-11 の直下ではないから、>はつけない
    url_in_tag = page_soup.select_one('.rnn-col-11:last-of-type a')
    # 三項演算子
    company_url = url_in_tag.get('href') if url_in_tag else None
    print(company_url)

    c_info = {
      'company': company_name.text,
      'url': company_url,
    }
    company_list.append(c_info)

# CSV出力
df=pd.DataFrame(company_list)

print(df)

df.to_csv('rikunabi.csv', index=None, encoding='utf-8-sig')