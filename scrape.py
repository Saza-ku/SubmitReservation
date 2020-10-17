from selenium import webdriver
#import chromedriver_binary
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

#引数：無。戻り値：PandAの初期画面を開いたbrowser。
def new_browser():
    #ブラウザはchrome。demo用にブラウザは表示。
    browser = webdriver.Chrome()
    browser.get("https://panda.ecs.kyoto-u.ac.jp/portal/")
    return browser

#引数：browser,ユーザーID,パスワード。戻り値：loginに成功した場合True。
def log_in(abrowser,userid,password):
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
    
    afterUrl = abrowser.current_url
    browser = abrowser

    return beforeUrl != afterUrl #loginに成功した場合URLが変わる→URLが一致しないという条件式はTrue。

#引数：browser,講義名。戻り値：成功した場合True。
#loginからにしか対応していません！！課題を提出した後に戻る関数ではありません！！
#講義名は一意に決まる名前にしてください。
#戻り値に特に意味はありません。「ドラフトを保存」ができているということは講義が必ず存在するからです。
def go_to_worksite(abrowser,worksiteName):
    try :
        dashboard = abrowser.find_element_by_link_text("サイトセットアップ")
        dashboard.click()

        sleep(1)

        #iframe = abrowser.find_element_by_id(iframeId)
        #(iframeのidがuserに固有かもしれない。)
        #abrowser.switch_to_frame(iframe)
        iframe = abrowser.find_element_by_class_name("portletMainIframe")
        abrowser.switch_to_frame(iframe)
       
        select_element = abrowser.find_element_by_id("selectPageSize")
        select_object = Select(select_element)
        select_object.select_by_visible_text("表示 1000 件ずつ")

        sleep(2)

        #講義を選択。
        worksiteButton = abrowser.find_element_by_partial_link_text(worksiteName)
        worksiteUrl = worksiteButton.get_attribute("href")
        #worksiteButton.click() #自分用なので、テスト/クイズには対応していません。
        abrowser.get(worksiteUrl)
            
        sleep(1)

        broser = abrowser

        return True

    except Exception as e: 
        print("COULD NOT GO TO WORKSITE")
        abrowser.quit()
        exit
        return False 

#引数：browser,課題提出先の名前（提出する課題ファイルの名前ではない）。戻り値：成功した場合True。
#gotoWorksiteからにしか対応していません！！課題を提出した後にAssignmentに戻る関数ではありません！！
#課題提出先の名前は一意に決まる名前にしてください。
#戻り値に特に意味はありません。「ドラフトを保存」ができているということは課題提出先が必ず存在するからです。
def go_to_assignment(abrowser,assignmentName):
    #左のバーから"課題"を選択。
    assignmentTabButton = abrowser.find_element_by_partial_link_text("課題")
    assignmentTabUrl = assignmentTabButton.get_attribute("href")
    #assignmentTabButton.click()
    abrowser.get(assignmentTabUrl)
    sleep(1)
    
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

        sleep(1)

        browser = abrowser
        
        return True
    
    except Exception as e: 
        print("COULD NOT GO TO ASSIGNMENT")
        abrowser.quit()
        exit
        return False 


#引数。戻り値：成功した場合True。
def submit(abrowser):
    canSubmit = False
    count = 0
    sleepTime = 30

    while ((not canSubmit) and count < 300/sleepTime) :
        canSubmit = click_submit_button(abrowser)
        count += 1
        sleep(sleepTime)

def click_submit_button(abrowser):
    try :
        submitButton = abrowser.find_element_by_id("post")
        submitButton.click()
        return True
    except Exception as e :
        return False

#===============================================================================
'''
#main
userId = "a0189727"
password = "Toriaezu1"
worksiteName = "量子物理学２（材原宇）〈情報〉"
assignmentName = "10/20分課題"

browser = new_browser()

if log_in(browser,userId,password) :
    print("log-in succeeded")
else :
    browser.quit()
    exit

go_to_worksite(browser,worksiteName)
go_to_assignment(browser,assignmentName)
submit(browser)

browser.quit()
exit
'''
