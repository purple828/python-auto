#导入selenium库
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(r'H:\chromdownload\chromedriver_win32\chromedriver.exe')

driver.implicitly_wait(10)

#get 方法 打开指定网页
driver.get('https://kyfw.12306.cn/otn/leftTicket/init')

#找到出发地的输入框
fromEle = driver.find_element_by_id('fromStationText')
#先点击一下它，这是12306的限制，不点击不行
fromEle.click()
fromEle.clear()
fromEle.send_keys('南京南\n')




#找到目的地的输入框
finalEle = driver.find_element_by_id('toStationText')
finalEle.click()
finalEle.clear()
finalEle.send_keys('杭州东\n')

#选择开始时间 选择时间的框是Select   cc_start_time
timeSelect = Select(driver.find_element_by_id('cc_start_time'))
timeSelect.select_by_visible_text('06:00--12:00')

#第三个tab就是第三天   选日期
tommorrow = driver.find_element_by_css_selector('#date_range li:nth-child(3)')
#点击这个，就会搜索车次
tommorrow.click()
#选择2等座有票的车次  @代表属性   //任意位置的所有子节点，/直接子节点
xpath = '//*[@id="queryLeftTable"]//td[4][@class]/../td[1]//a'

theTrains = driver.find_element_by_xpath(xpath)
for one in theTrains:
    print(one.text)

#最后，driver.quit 让浏览器和驱动进程一起退出
driver.quit()







