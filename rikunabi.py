import pandas as pd
import requests
from bs4 import BeautifulSoup
from time import sleep

# 企業詳細ページURLリストを取得
d_list = []
# i = 0
# while True:
#   i += 1
  # test
  #if i>2:
  #  break

url='https://next.rikunabi.com/rnc/docs/cp_s00700.jsp?jb_type_long_cd=0500000000&wrk_plc_long_cd=0840000000&wrk_plc_long_cd=0840300000&curnum=1'

res = requests.get(url, timeout=3)
#res = requests.get(url, timeout=3, allow_redirects=False)
print(res.status_code)
#print(res.history)
res.raise_for_status()
# if res.status_code != 200:
#   break

soup = BeautifulSoup(res.content, 'html.parser')
post = soup.select('.rnn-linkText--black')
# post = soup.select('li')
print(post)
for pp in post:
  print(pp.get('href'))