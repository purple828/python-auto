
from urllib.request import *
import re
import logging


url ='https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1521526930790_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E8%90%8C%E5%A8%83'
# url = 'http://qa-mall-www.baibu.la/'


html = urlopen(url)


obj = html.read().decode()
# print(obj)
matchstr = r'"objURL":"(http:.*?\.jp[e]?g)"'

#百度图片中，只能爬出objURL地址，其他的爬不到
# "objURL":"http://v1.qzone.cc/pic/201611/19/17/40/58301e1f5ce67927.JPG%21600x600.jpg"                                ok
# https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=3415758294,1581442723&fm=27&gp=0.jpg                      no
# urls = re.findall(r'src="(http:.*?\.png)"',obj)
urls = re.findall(matchstr,obj)
print('urls---------------',urls)
index = 0
for url in urls:
	try:
		print('downloading%d'%index)
		urlretrieve(url,'pic'+ str(index)+'.jpg')
		index += 1
	except Exception:
        # logging.info(Exception)
		print('download error.....%d'%index)
	else:
		print('download complete...')
