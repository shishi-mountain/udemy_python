import requests
from bs4 import BeautifulSoup

url = "https://www.python.org/"
r = requests.get(url)

# soup = BeautifulSoup(html, 'lxml')
soup = BeautifulSoup(r.content, 'html.parser')
tag=soup.find(attrs={'class': 'shrubbery'})
ul = tag.find('ul', attrs= {'class': 'menu'})

date = ul.find_all('time')
titles =ul.find_all('a')
for i, title in enumerate(titles):
  print('='*30, i, '='*30)
  print(f'日付 ： {date[i].text}')
  print(f'タイトル : {title.text}')