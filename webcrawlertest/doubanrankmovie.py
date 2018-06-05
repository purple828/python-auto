import requests
from bs4 import BeautifulSoup

#要爬取的网页地址
pageurl="https://movie.douban.com/chart"


#根据给定的地址url来获取页面内容
def get_page_content(url):

    headers={
        'User - Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    content = requests.get(url,headers=headers).content
    print(content)
    return content

#从整个页面内容中筛选出需要的数据
def get_select_data(doc):
    soup = BeautifulSoup(doc,'html.parser')
    div = soup.find('div',attrs={'class',''})


if __name__ == '__main__':
    get_page_content(pageurl)


