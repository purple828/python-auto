import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

#要爬取的网页地址
pageurl="https://movie.douban.com/chart"

wb = Workbook()
w = wb.active
w.title = '豆瓣电影排行榜'
dest_filename = '豆瓣电影.xlsx'


#根据给定的地址url来获取页面内容
def get_page_content(url):

    headers={
        'User - Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    content = requests.get(url,headers=headers).content
    # print(content)
    return content

#从整个页面内容中筛选出需要的数据
def get_select_data(doc):
    movie_name = []  #电影名
    movie_score = [] #电影评分
    movie_star_con = [] #电影评价人数
    movie_time = [] #电影上线年份
    movie_url = [] #电影链接
    soup = BeautifulSoup(doc,'html.parser')
    #找到最外层的div对象
    main_div = soup.find('div',attrs={'class','indent'})
    # print(main_div)
    tables = main_div.find_all('table')
    # print(tables)
    for table in tables:
        # print(table)
        info_div = table.find('div',attrs={'class','pl2'})
        # print(info_div,end='')
        # print('\n')

        #获取电影名称
        a_tag = info_div.find('a')
        name = a_tag.get_text()
        n = name.split('/')[0]
        movie_name.append(n)

        #获取电影链接
        url = a_tag['href']
        movie_url.append(url)

        #获取电影评分
        rating_nums = info_div.find('span',attrs={'class','rating_nums'}).get_text()
        # print('rating_nums',rating_nums,end='')
        movie_score.append(rating_nums)

        # 获取电影评价人数
        star_con = info_div.find('span', attrs={'class', 'pl'}).get_text()
        # print('star_con', star_con, end='')
        movie_star_con.append(star_con)


        #获取电影上线年份
        p_tag = info_div.find('p')
        time = p_tag.get_text()
        t = time.split('/')[0]
        # print(t)
        movie_time.append(t)

    return movie_name,movie_score,movie_star_con,movie_time,movie_url



if __name__ == '__main__':
    name = []
    score = []
    star = []
    time = []
    url = []
    page_content = get_page_content(pageurl)
    movie_name, movie_score, movie_star_con, movie_time, movie_url = get_select_data(page_content)
    name = name + movie_name
    score = score + movie_score
    star = star + movie_star_con
    time = time + movie_time
    url = url + movie_url

    w['A1'] = '电影名'
    w['B1'] = '电影评分'
    w['C1'] = '电影评价人数'
    w['D1'] = '上线时间'
    w['E1'] = '观看地址'

    for(n,sc,st,t,u) in zip(name,score,star,time,url):
        print(n,sc,st,t,u)
        col_A = 'A{}'.format(name.index(n)+2)
        col_B = 'B{}'.format(name.index(n) + 2)
        col_C = 'C{}'.format(name.index(n) + 2)
        col_D = 'D{}'.format(name.index(n) + 2)
        col_E = 'E{}'.format(name.index(n) + 2)
        w[col_A] = n.strip()
        w[col_B] = sc
        w[col_C] = st
        w[col_D] = t
        w[col_E] = u
        wb.save(filename=dest_filename)




