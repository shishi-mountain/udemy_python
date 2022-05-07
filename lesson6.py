from bs4 import BeautifulSoup

html = """
  <body>
    <h1>タイトル</h1>
    <h2>演習内容</h2>
    <p>パラグラフ</p>
    <ol id="step1" class="study-list">
      <li class="python-list">Python basic</li>
      <li class="html-list" value="22">HTML basic</li>
      <li class="opython-list2">JS basic</li>
      <li class="html-js-list" value="34">python library basic</li>
    </ol>
  </body>
"""

soup = BeautifulSoup(html, 'html.parser')
#print(soup.find_all(['h1', 'h2']))
print(soup.select('li:-soup-contains("Python")'))
#print(soup.select('#step2 > li'))
