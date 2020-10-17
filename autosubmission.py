from selenium import webdriver
import chromedriver_binary
from time import sleep
import datetime
from selenium.webdriver.support.select import Select

def dating(hoge):
    k = hoge.split('/')
    return datetime.date(int(k[0]),int(k[1]),int(k[2]))

def make_datetime(hoge,fuga):
    k = fuga.split(':')
    l = hoge.split('/')
    return datetime.datetime(int(l[0]),int(l[1]),int(l[2]),int(k[0]),int(k[1]))


#ブラウザはchrome,あえてブラウザは表示させました。

browser = webdriver.Chrome()
browser.get("https://panda.ecs.kyoto-u.ac.jp/portal/")

lgin = browser.find_element_by_id("loginLink1")
lgin.click()

#usernameとpasswordは自分がいつも使ってる奴にしてください。

userid = browser.find_element_by_id("username")
userid.send_keys("a0189727")

password = browser.find_element_by_id("password")
password.send_keys("Toriaezu1")

sleep(1)

login = browser.find_element_by_name("submit")
login.click()
#ここまででログインをします
browser.implicitly_wait(3)
dashboard = browser.find_element_by_link_text("サイトセットアップ")
dashboard.click()

print("login ok")

sleep(2)

nameOfWorksite = "情報企業論"
nameOfAssignment = ""

iframe = browser.find_element_by_id("Mainf9425ba1x54e3x4846x9ae8xdc0a032aa09e")
# 上について:ここのiframeのidが人によって異なるかもしれないので変えておきました。
browser.switch_to_frame(iframe)

select_element = browser.find_element_by_id("selectPageSize")
select_object = Select(select_element)
select_object.select_by_visible_text("表示 1000 件ずつ")

sleep(2)

assignment = browser.find_element_by_partial_link_text(nameOfWorksite)
assignment.click() #自分用なので、テスト/クイズには対応していません。

'''
cources = browser.find_elements_by_tag_name("tr")

url_list = []
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

        if url == "https://panda.ecs.kyoto-u.ac.jp/portal/tool/f9425ba1-54e3-4846-9ae8-dc0a032aa09e?panel=Main#": #urlsには講義のURLともう一つ別のURLが入っています。後者を避けるためのif文です。
            continue
        url_list.append(url)
'''

"""
この下、urls_2020の所は自分専用の形になってます。公開するとは思っていなかったので。
上のforループでpandaにある全ての講義のurlを取得しました。
しかし私のpandaには2019年の講義のURLやら教職関連のURLやらがあったので除去しなくてはいけません。
その作業を下で行っています。
もしこれを利用するのであれば、どうかご自分に合った形に変形してください。
よろしくお願い致します。
"""

'''
urls = url_list[6:] #2019年度の除去
address = urls[:-2] #教職関連の除去
urls_2020 = address[7:] #ここゴチャっとしてるんですけど、2020前期の講義だけ集めてます

today = datetime.date.today()
assignment_lists = []
for c in urls_2020:
    print(c)
    browser.get(c)
    sleep(2)
    assignment = browser.find_element_by_partial_link_text("課題")
    # 上について:課題/assignment　っていう形をした講義があったので。partialにしました。
    assignment.click() #自分用なので、テスト/クイズには対応していません。
    sleep(2)
    iframe = browser.find_element_by_class_name("portletMainIframe")
    # 多分こっちのiframeのclass_nameはみんな同じだと思います。

    browser.switch_to_frame(iframe)
    tt = browser.title
    assignment = browser.find_element_by_partial_link_text("課題")
    
    try:
        table = browser.find_element_by_xpath('/html/body/div/form/table')
        ass = table.find_elements_by_tag_name("tr")
        li = []
        for i in ass:
            li.append(i.text)
        n = len(li)

    except Exception as e:
        continue #そもそもテーブルが用意されていない講義もあります。（民俗学とか）

'''
print("get assignment data collectly")
browser.quit()
