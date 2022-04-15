from time import sleep

import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = 'https://doda.jp/DodaFront/View/JobSearchList.action?pic=1&ds=0&oc=0313M%2C0317M%2C0321M&so=50&ci=401307&pf=0&tp=1&page={}'

d_list = []

for i in range(1, 50):
  url = base_url.format(i)
  sleep(2)

  r = requests.get(url, timeout=3)
  r.raise_for_status()
  if r.status_code != 200:
    break

  soup = BeautifulSoup(r.content, 'html.parser')

  companies = soup.find_all('div', class_= 'layoutList02')
  print(len(companies))

  for i,company in enumerate(companies):
    company_url = ''
    print('='*30, i, '='*30)
    company_name = company.find('span', class_='company').text
    page_url = company.find('a', class_='btnJob03').get('href')

    page_url = page_url.replace('-tab__pr', '-tab__jd')
    print(company_name, '::', page_url)

    sleep(1)

    page_r = requests.get(page_url, timeout=3)
    page_r.raise_for_status()

    page_soup = BeautifulSoup(page_r.content, 'html.parser')
    table = page_soup.find('table', id='company_profile_table')
    if table:
      company_url = table.find('a')
      if company_url:
        company_url = company_url.get('href')
    else:
      # 違うところにないか探す
      tab = page_soup.find('div', id='shtTabContent3')
      if tab:
        dt = tab.find_all('dt')
        dd = tab.find_all('dd')
        for i in range(len(dt)):
          if '企業URL' in dt[i].text:
            company_url = dd[i].find('a').attrs['href']

    d_list.append({
      'company_name': company_name,
      'company_url': company_url,
    })

  print(d_list[-1])

  df = pd.DataFrame(d_list)
  df.to_csv('company_list.csv', index=None, encoding='utf-8-sig')
