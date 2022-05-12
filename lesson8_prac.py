from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
# ヘッドレスモードでの使用 (ブラウザを立ち上げない）
# options.add_argument('--headless')

# シークレットモードでの使用
options.add_argument('--incognito')

# User-Agentの設定
# options.add_argument('--user-agent=')

# driver作成
driver = webdriver.Chrome(executable_path='/Users/ishiichiharu/Documents/try/py_udemy/tools/chromedriver2', options=options)

# 待つ
# driver.implicitly_wait(10)

# driver.get()でサイトにアクセス
driver.get('https://news.yahoo.co.jp')
sleep(3)

# inputタグに入力
search_box = driver.find_element_by_css_selector('input.sc-kgoBCf')
search_box.send_keys('ITエンジニア')
sleep(3)

search_box.submit()
sleep(3)

while True:
  # 1. スクロール
  driver.execute_script('window.scrollTo(0, document.body.scrollHeight')
  sleep(2)

  # 2. ボタンのCSSセレクタを取得する
  # elements にすると、ボタンがない場合もエラーにならずに空のリストができる
  button = driver.find_elements_by_css_selector('div.newsFeed > div > span > button')
  sleep(2)

  # 3. ボタンを押す
  if button:
    button[0].click()
  else:
    break

  sleep(3)

  driver.quit()


# ページを閉じる
# driver.close()

