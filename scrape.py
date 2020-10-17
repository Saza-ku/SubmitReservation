import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

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
