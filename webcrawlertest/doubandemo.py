# import urllib
from urllib import request
from bs4 import BeautifulSoup
import re

from selenium import webdriver

url = r"https://movie.douban.com/"

driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(10)
targe = driver.page_source
print('====================targe===========',targe)



html = request.urlopen(url,data=None,cafile=None,capath=None,cadefault=False,context=None)
obj = html.read().decode()
# print('obj------------',obj)
soup = BeautifulSoup(obj,'html.parser')
# print('soup------+++++++++++++++++-------',soup,end='')

# bcSouplist = soup.find_all(name="h1", attrs={"class":re.compile(r"abc(\s\w+)?")})
#正在热映中的影片
list1 = soup.find_all(name='a',attrs={"href":re.compile("https://movie.douban.com.*from=showing")})
#热门推荐
list2 = soup.find_all(name='a',attrs={"href":re.compile("https://movie.douban.com.*from=gallery")})
list3 = soup.find_all(name='a',attrs={"href":re.compile("https://movie.douban.com.*from=reviews")})
list4 = soup.find_all(name='a',attrs={"href":re.compile("https://movie.douban.com.*from=gaia")})
list5 = soup.find_all(name='a',attrs={"href":re.compile("https://movie.douban.com.*from=gaia_video")})

# print('list1--------------',list1)
# print('******************************************************************************************************')
# print('list2--------',list2)
# print('*********************************************************************************************************')
# print('list3---',list3)
# print('*********************************************************************************************************')
# print('list4---',list4)
#
# print('*********************************************************************************************************')
# print('list5---',list5)


