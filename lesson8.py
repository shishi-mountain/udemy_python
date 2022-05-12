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
driver.implicitly_wait(10)

# driver.get()でサイトにアクセス
driver.get('https://news.yahoo.co.jp')
sleep(3)

height = 500
while height < 2000:
  # 自動スクロール x,y
  #driver.execute_script(f'window.scrollTo(0, {height})')
  height += 100
  sleep(1)

# 一番下までスクロールする
last_height = driver.execute_script('return document.body.scrollHeight')
sleep(3)

driver.execute_script(f'window.scrollTo(0, {height})')
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

print('--- css selector ---')
# css selector
a_tags = driver.find_elements_by_css_selector('.sc-jqCOkK')
for atag in a_tags:
  print(atag.text)
  print(atag.get_attribute('href'))

print('--- css selector div > ul > li 3--')
a_tag3 = driver.find_element_by_css_selector('div.sc-jBoNkH > div > ul > li:nth-of-type(3) > a')
print(a_tag3.text)

# 自動クリック もっと見るなどで使用する
# a_tag3.click()

sleep(3)

# inputタグに入力
search_box = driver.find_element_by_css_selector('input.sc-kgoBCf')
sleep(3)

search_box.send_keys('柴犬　ステッカー')
sleep(3)

# 入力した文字を消す うまく消えてくれない
# search_box.clear()
# なので以下で対応する
text = search_box.get_attribute('value')
search_box.send_keys(Keys.BACKSPACE * len(text))
sleep(3)

search_box.send_keys('黒柴')

search_box.submit()
sleep(2)

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

