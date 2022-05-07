import pandas as pd
import requests
from bs4 import BeautifulSoup
from time import sleep
import re

# 企業詳細ページURLリストを取得
base_url = 'https://next.rikunabi.com'
d_list = []
i = 0
while True:
  # test
  if i>3:
   break

  url='https://next.rikunabi.com/rnc/docs/cp_s00700.jsp?jb_type_long_cd=0500000000&wrk_plc_long_cd=0840000000&wrk_plc_long_cd=0840300000&curnum=' + str(1+50*i)
  print(url)
  i += 1

  res = requests.get(url, timeout=3)
  print(res.status_code)
  res.raise_for_status()
  if res.status_code != 200:
    break

  soup = BeautifulSoup(res.content, 'html.parser')
  post = soup.select('.rnn-linkText--black')
  for pp in post:
    detail_url = base_url + pp.get('href')
    sleep(1)
    d_list.append(detail_url)
    # print(detail_url)

# 詳細ページを読んで、求人詳細ページにとぶ
company_list = []
for d_url in d_list:
  r = requests.get(d_url, timeout=3)
  soup = BeautifulSoup(r.content, 'html.parser')

  # 求人情報URL取得
  if (soup.select_one('.rn3-companyOfferTabMenu__navItemLink') == None):
    # 求人詳細ページがない場合は読み飛ばす
    continue

  info_url = base_url + soup.select_one('.rn3-companyOfferTabMenu__navItemLink').get('href')
  info_r = requests.get(info_url, timeout=3)
  soup = BeautifulSoup(info_r.content, 'html.parser')
  if (soup.select_one('.rn3-companyOfferCompany__link') == None):
    # 社名なし
    continue

  # 会社名
  company_name = soup.select_one('.rn3-companyOfferCompany__link').text

  if (soup.select_one('.js-companyOfferEntry__link') == None):
    # 会社URLなし
    continue

  # 会社URLに飛ぶ前のアクセスURL
  tmp_url = soup.select_one('.js-companyOfferEntry__link').get('href')

  tmp_r = requests.get(base_url + tmp_url)
  soup = BeautifulSoup(tmp_r.content, 'html.parser')
  # company_url = soup.find('a', text=re.compile("こちら"))
  company_url = soup.select_one('a:-soup-contains("こちら")')
  if company_url is None:
    # URLなし
    company_url = ''
  else:
    company_url = company_url.get('href')

  c_info = {
    'company': company_name.replace('\r\n','').replace('\n','').replace(' ', ''),
    'url': company_url,
  }
  company_list.append(c_info)
  #print(c_info)



# CSV出力
df=pd.DataFrame(company_list)

print(df)

df.to_csv('rikunabi.csv', index=None, encoding='utf-8-sig')