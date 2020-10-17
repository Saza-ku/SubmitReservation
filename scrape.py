import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from selenium import webdriver
from time import sleep
import datetime

def login(user, pwd):
	# セッションを開始
	session = requests.session()

	# ログイン情報の取得
	login_page = session.get("https://cas.ecs.kyoto-u.ac.jp/cas/login?service=https%3A%2F%2Fpanda.ecs.kyoto-u.ac.jp%2Fsakai-login-tool%2Fcontainer").text
	soup = BeautifulSoup(login_page, "html.parser")
	values = soup.findAll("input", type="hidden")
	lt = values[0].attrs["value"]
	execution = values[1].attrs["value"]
	event_id = values[2].attrs["value"]
  

	# ログイン情報の準備

	login_info = {
		"usrname":user,
		"password":pwd,
    	"warn":"true",
    	"lt":lt,
		"execution":execution,
		"_eventId":event_id
	}
	url_login = "https://cas.ecs.kyoto-u.ac.jp/cas/login?service=https%3A%2F%2Fpanda.ecs.kyoto-u.ac.jp%2Fsakai-login-tool%2Fcontainer"

   
	res = session.post(url_login, data=login_info)
	res.raise_for_status() # エラーならここで例外を発生させる

	print(res.text)
	print(lt)
	print(execution)
	print(event_id)

def get_cources(browser):
	dashboard = browser.find_element_by_link_text("サイトセットアップ")
  	dashboard.click()
  	sleep(2)
  	cources = browser.find_elements_by_tag_name("tr")

  	urls = []
  	for cource in cources:
		urls = cource.find_elements_by_tag_name('a')
      	for a in urls:
          	url = a.get_attribute("href")

          	"""
          	下のif文の意図を書きます。
          	urlsに入っているaタグのhrefは二つあります。
          	1つは講義のURLでもう1つはhref="#"です。
          	href="#"が講義のURLリストに入るのは避けたいので下のif文を書きました。
          	"""


# "#_URL"にすると手元の環境だと動かない。サイトセットアップのページに戻るURLを除去したいので、そのURLをそのまま書く方が確実かと？
          if url == "#_URL": #urlsには講義のURLともう一つ別のURLが入っています。後者を避けるためのif文です。
              continue
          urls.append(url)
  return cources

