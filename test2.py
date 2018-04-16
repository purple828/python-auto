from selenium import webdriver
#指定的是chrome的驱动
#执行到这里的时候Selenium会去到指定的路径将chrome driver程序运行起来
#调用该方法会返回一个WebDriver实例对象，控制该对象就可以控制浏览器
driver = webdriver.Chrome(r'H:\chromdownload\chromedriver_win32\chromedriver.exe')
#get 方法  打开指定网址
driver.get('http://www.baidu.com')
print(driver.get_cookies())

#查找到那个搜索输入栏网页元素，返回一个表示该元素的WebElement对象
element_keyword = driver.find_element_by_id('kw')
#输入字符
element_keyword.send_keys('松勤')
#找到搜索按钮
element_search_button = driver.find_element_by_id('su')
#点击该元素
element_search_button.click()

#===========================
import time
time.sleep(2)
ret = driver.find_element_by_id('1')
print(ret.text)
if ret.text.startswith('松勤网'):
    print('测试通过')
else:
    print('测试不通过')


#===========================



#最后  driver.quit 让浏览器和驱动进程一起退出，不然会有好几个实例一起运行
# driver.quit()

