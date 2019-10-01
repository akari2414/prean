from urllib import parse
from urllib import request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import urllib, time, ssl, os, sys
context = ssl._create_unverified_context()

id = ''
pw = ''

local_path = 'images'
login_page = 'https://www.instagram.com/accounts/login/?source=auth_switcher'
tag = '롤드컵'

if not os.path.exists(local_path):
    os.makedirs(local_path)

ch = webdriver.Chrome(executable_path='./chromedriver')

# 로그인 패이지 접속
ch.get(login_page)

# 로그인 페이지 대기
try:
    element = WebDriverWait(ch, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
except Exception as e:
        print(e)


# 로그인 정보 입력
ch.find_element_by_name('username').send_keys(id)
ch.find_element_by_name('password').send_keys(pw)

# 로그인 버튼 클릭
ch.find_element_by_css_selector('button.L3NKy').click()

# 로그인 대기
try:
    element = WebDriverWait(ch, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.wUAXj"))
    )
except Exception as e:
        print(e)

# 알림설정 나중에 버튼 선택
ch.find_element_by_css_selector('button.HoLwm').click()

# 테그입력
ch.find_element_by_css_selector('input.x3qfX').send_keys(tag)

# 연관 검색어 로딩 대기
try:
    element = WebDriverWait(ch, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.drKGC"))
    )
except Exception as e:
        print(e)

# 첫번째 연관 검색어 클릭
ch.find_elements_by_css_selector('div.fuqBx a')[0].click()

# 페이지 로딩 대기
try:
    element = WebDriverWait(ch, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.weEfm"))
    )
except Exception as e:
        print(e)

urls = {}
stop = False
idx = 0

while(True) :
    for image in ch.find_elements_by_css_selector('img.FFVAD') :
        temp_url = image.get_attribute('srcset')
        tp = temp_url.split(' 150w,')
        url = tp[0]
        url_info = parse.urlparse(url)
        fname, ext = os.path.splitext(url_info.path)

        local_file = local_path + '/download_image' + str(len(urls)+1) + ext
        urls[url] = url

        req = urllib.request.urlopen(url, context=context).read()
        fid = open(local_file, "wb")
        fid.write(req)
        fid.close()

        if(len(urls) == 100) :
            stop = True
            break

    ch.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    if(stop == True):
        break

ch.close()
ch.quit()
sys.exit()
