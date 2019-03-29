#-*- coding : utf-8 -*-
from selenium import webdriver
import datetime
import time
import os

ROOT,FILENAME=os.path.split(os.path.abspath(__file__))
def login(browser):
    browser.get("https://www.taobao.com")
    handle=browser.current_window_handle
    if browser.find_element_by_link_text("登录"):
        browser.find_element_by_link_text("登录").click()
        print("请在15秒内完成扫码,扫码成功请按回车")
        input()
    now = datetime.datetime.now()
    print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))
    handles=browser.window_handles
    for newhandle in handles:
        if newhandle!=handle:
            browser.switch_to_window(newhandle)
            browser.close()
            browser.switch_to_window(handles[0])
    browser.get("https://cart.taobao.com")


def buy(times,browser):
    choose = input("到时间自动勾选购物车请输入“a”，否则输入“b”：")
    if choose == 'b':
        print("请手动勾选需要购买的商品")
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        if now > times:
            if choose == 'a':
                while True:
                    try:
                        if browser.find_element_by_id("J_SelectAll1"):
                            browser.find_element_by_id("J_SelectAll1").click()
                            break
                    except:
                        print("找不到全选按钮")
            try:
                browser.switch_to
                if browser.find_element_by_id("J_Go"):
                    handle=browser.current_window_handle
                    browser.switch_to_window(handle)
                    browser.find_element_by_id("J_Go").click()
                    js='document.getElementById("J_Go").click()'
                    browser.execute_script(js)
                    print("结算成功")
            except:
                print("结算失败")
            while True:
                try:
                    if browser.find_element_by_link_text('提交订单'):
                        browser.find_element_by_link_text('提交订单').click()
                        now1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                        print("抢购成功时间：%s" % now1)
                except:
                    print("再次尝试提交订单")
                    time.sleep(0.01)
 
if __name__ == "__main__":
    
    print("___________            __________                 __________        __   ")
    print("\__    ___/____    ____\______   \_____    ____   \______   \ _____/  |_ ")
    print("  |    |  \__  \  /  _ \|    |  _/\__  \  /  _ \   |    |  _//  _ \   __\ ")
    print("  |    |   / __ \(  <_> )    |   \ / __ \(  <_> )  |    |   (  <_> )  |  ")
    print("  |____|  (____  /\____/|______  /(____  /\____/   |______  /\____/|__|  ")
    print("               \/              \/      \/                 \/            ")
    print("                                                               code by Horizon")
    times = input("请输入抢购时间，格式如(2018-09-06 11:20:00.000000):")
    options=webdriver.ChromeOptions()
    options.add_argument('--log-level=3')
    options.binary_location=ROOT+"/Application/chrome.exe"
    browser = webdriver.Chrome(chrome_options=options,executable_path=ROOT+"/chromedriver.exe")
    browser.maximize_window()
    login(browser)
    buy(times,browser)
    browser.close()

