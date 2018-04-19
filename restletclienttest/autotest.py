from selenium import webdriver
import os
import time

#若浏览器启动与python.exe在同一个目录下则可以省略其存放位置
# driver = webdriver.Chrome(r'H:\chromdownload\chromedriver_win32\chromedriver.exe')

# 加启动配置
option = webdriver.ChromeOptions()
option.add_extension("I:2.8.0.1_0.crx") #自己下载的crx路径

driver = webdriver.Chrome(chrome_options=option)

driver.implicitly_wait(10)

driver.get(r'chrome-extension://aejoelaoggembcahagimdiliamlcdmfm/restlet_client.html')

time.sleep(10)

#输入请求方式的输入框   get post
xpath = '//*[@id="request"]//div[2]//div[2]//div//div//input'
reqEle = driver.find_element_by_xpath(xpath)
#请求方式列表的下拉框内容
listxpath = '//*[@id="request"]//div[2]//div[2]//div//div//span//a[@href="javascript:;"]'
listEle = driver.find_element_by_xpath(listxpath)
listEle.click()
#选中post请求
selectEle = driver.find_element_by_link_text("GET")
selectEle.click()

#输入请求地址的输入框
addEle = driver.find_element_by_id("gwt-uid-541")
#去掉页面上原本默认的值
js='document.getElementById("gwt-uid-541").value=""'
driver.execute_script(js)

addEle.send_keys(r"http://dev-api.baibu.la/order/api/invoke?v=1.0&exec=YpbOrderInfoList&workerId=732")
addEle.click()
text = addEle.get_attribute("value")

saveButton = driver.find_element_by_link_text("Save")
saveButton.click()


#发送按钮
sendButton = driver.find_element_by_link_text("Send")
sendButton.click()








