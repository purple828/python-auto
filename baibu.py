from selenium import webdriver
import time

driver = webdriver.Chrome(r'H:\chromdownload\chromedriver_win32\chromedriver.exe')

driver.get('https://qa-bps.hengdafangzhi.com/static/index.html#/login')

account = driver.find_element_by_class_name('el-input__inner')
account.send_keys('方丽娟')

password = driver.find_element_by_class_name('base-input')
password.send_keys('123456')

submit = driver.find_element_by_tag_name('button')

submit.click()
time.sleep(3)

orderxpath = '//a[@href="#/orderList"]'

manxpath = '/html/body/div[1]/div/div/div[1]/ul/li[2]/div'

orderEle = driver.find_element_by_xpath(manxpath)

# orderEle = driver.find_element_by_css_selector('/html/body/div[1]/div/div/div[1]/ul/li[2]/div')

orderEle.click()
# orderListEle = driver.find_element_by_link_text('订单列表')

orderListEle = driver.find_element_by_xpath(orderxpath)
print(orderListEle)
orderListEle.click()



