import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

from selenium import webdriver
#import chromedriver_binary
from time import sleep
import datetime
from selenium.webdriver.support.select import Select

#引数：無。戻り値：browser
def new_browser():
    #ブラウザはchrome。demo用にブラウザは表示。
    browser = webdriver.Chrome()
    browser.get("https://panda.ecs.kyoto-u.ac.jp/portal/")
    return browser

#引数：browser,ユーザーID,パスワード。戻り値：loginに成功した場合True。
def login(abrowser,userid,password):
    lgin = abrowser.find_element_by_id("loginLink1")
    lgin.click()
    sleep(1)
    
    beforeUrl = abrowser.current_url
    
    useridBox = abrowser.find_element_by_id("username")
    useridBox.send_keys(userid)
    passwordBox = abrowser.find_element_by_id("password")
    passwordBox.send_keys(password)

    sleep(1)

    login = abrowser.find_element_by_name("submit")
    login.click()

    sleep(1)
    #browser.implicitly_wait(1)
    afterUrl = abrowser.current_url

    sleep(1)

    browser = abrowser

    return beforeUrl != afterUrl #loginに成功した場合URLが変わる→URLが一致しないという条件式はTrue。

#引数：browser,講義名。戻り値：成功した場合True。
#loginからにしか対応していません！！課題を提出した後に戻る関数ではありません！！
#講義名は一意に決まる名前にしてください。
#戻り値に特に意味はありません。「ドラフトを保存」ができているということは講義が必ず存在するからです。
def gotoWorksite(abrowser,worksiteName):
    try :
        dashboard = abrowser.find_element_by_link_text("サイトセットアップ")
        dashboard.click()

        sleep(1)

        iframe = abrowser.find_element_by_id(iframeId)
        #(iframeのidがuserに固有かもしれない。)
        abrowser.switch_to_frame(iframe)

        select_element = abrowser.find_element_by_id("selectPageSize")
        select_object = Select(select_element)
        select_object.select_by_visible_text("表示 1000 件ずつ")

        sleep(1)

        #講義を選択。
        worksiteButton = abrowser.find_element_by_partial_link_text(worksiteName)
        worksiteUrl = worksiteButton.get_attribute("href")
        #worksiteButton.click() #自分用なので、テスト/クイズには対応していません。
        abrowser.get(worksiteUrl)
        broser = abrowser
    
        sleep(2)

        return True

    except Exception as e: 
        print("FAILED")
        abrowser.quit()
        exit
        return False 

#引数：browser,課題提出先の名前（提出する課題ファイルの名前ではない）。戻り値：成功した場合True。
#gotoWorksiteからにしか対応していません！！課題を提出した後にAssignmentに戻る関数ではありません！！
#課題提出先の名前は一意に決まる名前にしてください。
#戻り値に特に意味はありません。「ドラフトを保存」ができているということは課題提出先が必ず存在するからです。
def gotoAssignment(abrowser,assignmentName):
    #左のバーから"課題"を選択。
    assignmentTabButton = abrowser.find_element_by_partial_link_text("課題")
    assignmentTabUrl = assignmentTabButton.get_attribute("href")
    #assignmentTabButton.click()
    abrowser.get(assignmentTabUrl)
    sleep(2)
    
    iframe = abrowser.find_element_by_class_name("portletMainIframe")
    abrowser.switch_to_frame(iframe)
    tt = abrowser.title
    assignment = abrowser.find_element_by_partial_link_text("課題")
    
    try :
        table = abrowser.find_element_by_xpath('/html/body/div/form/table')
        assignmentButton = table.find_element_by_partial_link_text(assignmentName)
        assignmentUrl = assignmentButton.get_attribute("href")
        #assignmentButton.click()
        abrowser.get(assignmentUrl)
        browser = abrowser
        sleep(10)
        print("get assignment data collectly")
        return True
    
    except Exception as e: 
        print("FAILED")
        abrowser.quit()
        exit
        return False 

def submit(browser):
	try:
		browser.find_element_by_name("post").click()
	except Exception:
		browser.back()
		return
	browser.find_element_by_link_name("eventSubmit_doConfirm_assignment_submission").click()

#===============================================================================
'''
#main
userId = "a0189727"
password = "Toriaezu1"
iframeId = "Mainf9425ba1x54e3x4846x9ae8xdc0a032aa09e"
worksiteName = "情報企業論"
assignmentName = "第5回"

browser = new_browser()

if log_in(browser,userId,password) :
    print("log-in succeeded")
else :
    browser.quit()
    exit

gotoWorksite(browser,worksiteName)
gotoAssignment(browser,assignmentName)

browser.quit()
'''
