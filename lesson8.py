from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
# ヘッドレスモードでの使用 (ブラウザを立ち上げない）
options.add_argument('--headless')

# シークレットモードでの使用
options.add_argument('--incognito')

# User-Agentの設定
# options.add_argument('--user-agent=')

# driver作成
driver = webdriver.Chrome(executable_path='/Users/ishiichiharu/Documents/try/py_udemy/tools/chromedriver2', options=options)

# 待つ
driver.implicitly_wait(10)

# driver.get()でサイトにアクセス
driver.get('https://news.yahoo.co.jp')
sleep(3)

# ひとつだけ取得
# e = driver.find_element_by_tag_name('h2')
e = driver.find_element(by=By.TAG_NAME, value='h2')
print(e.text)
print(e.get_attribute('outerHTML'))  # BeautifulSoupのfind()とおなじ

print('#### ')

# 複数取得
h2_tags = driver.find_elements(by=By.TAG_NAME, value='h2')

for h2_tag in h2_tags:
  print(h2_tag.text)
  print(h2_tag.get_attribute('outerHTML'))

print(driver.title)
print(driver.current_url)

# idで取得
e = driver.find_element(by=By.ID, value="uamods-topics")
print(e.text)

print('----')
# classで取得
e = driver.find_element(by=By.CLASS_NAME, value="sc-jqCOkK")
print(e.text)
print(e.get_attribute('href'))


# driver.get('https://google.com')


# 戻る
# driver.back()

# # 進む
# driver.forward()

# # リフレッシュ
# driver.refresh()

# スクショ
driver.save_screenshot('test.png')

# ブラウザを終了
driver.quit()

# ページを閉じる
# driver.close()

