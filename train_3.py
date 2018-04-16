#导入selenium库里面的webdriver模块
from selenium import webdriver
from selenium.webdriver.support.ui import Select

from winsound import Beep
import time,sys

#下面的代码指定是chrome的驱动，注意这个driver对象是后面自动化的入口，
# 成功后返回一个WebDriver实例对象，通过它的方法，可以控制浏览器

driver = webdriver.Chrome(r'H:\chromdownload\chromedriver_win32\chromedriver.exe')

driver.implicitly_wait(10)

#get 方法 打开指定网页   12306登陆网页
driver.get('https://kyfw.12306.cn/otn/login/init')
driver.find_element_by_id('username').send_keys('juan520ni')
input('登陆界面，请输入密码登录  后按回车')

#=========================================================
#get 方法 打开指定网页
driver.get('https://kyfw.12306.cn/otn/leftTicket/init')

#找到出发地的输入框
fromEle = driver.find_element_by_id('fromStationText')
#先点击一下它，这是12306的限制，不点击不行
fromEle.click()
fromEle.clear()
fromEle.send_keys('阳新\n')




#找到目的地的输入框
finalEle = driver.find_element_by_id('toStationText')
finalEle.click()
finalEle.clear()
finalEle.send_keys('惠州\n')

#选择开始时间 选择时间的框是Select   cc_start_time
# timeSelect = Select(driver.find_element_by_id('cc_start_time'))
# timeSelect.select_by_visible_text('06:00--12:00')

#第三个tab就是第三天   选日期
tommorrow = driver.find_element_by_css_selector('#date_range li:nth-child(6)')

i=0
#循环不断的搜索
while True:
    i+=1
    isGet = False   #设置为没有找到
    # 点击这个，就会搜索车次
    tommorrow.click()
    # 选择2等座有票的车次  @代表属性   //任意位置的所有子节点，/直接子节点
    # xpath = '//*[@id="queryLeftTable"]//td[4][@class]/../td[1]//a'
    xpath = '//*[@id="queryLeftTable"]//td[8][@class]/../td[1]//a'

    # interseted = ['G1379','g1377','D3295','G7393']
    interseted = ['K1655']
    theTrains = driver.find_elements_by_xpath(xpath)
    print('thetrains------',theTrains)
    #将所有有票的车次遍历出来，看是否有我们感兴趣的票
    for one in theTrains:
        name = one.text
        if name in interseted:
            isGet = True
            print('********有剩余车票*******',name)
            #找到当前元素的上层节点
            targe = one.find_element_by_xpath('../../../../../td[last()]')

            targe.click()
            time.sleep(4)
            driver.find_element_by_id('normalPassenger_0').click()
            driver.find_element_by_id('submitOrder_id').click()
            #蜂鸣器通知
            Beep(1500,2000)
            sys.exit()

#==========================================================








