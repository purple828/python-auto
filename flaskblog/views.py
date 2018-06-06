from flask import Flask
from flask import render_template
from flask import request
from models import Article

#创建flask应用
app = Flask(__name__)

#指定路由
@app.route("/index/")
#视图函数，用来处理请求
def index():
    return "hello world"

@app.route('/articles/')
def article():
    articles = Article.select()
    return  render_template("newslistpic.html",articles=articles)

@app.route('/register/',methods=["GET","POST"])
def register():
    if request.method == "POST":
        requestData = request.form
        try:
            title = requestData["title"]
            time = requestData["time"]
            author = requestData["author"]
            description = requestData["description"]
            content = requestData["content"]

            article = Article()
            article.title = title
            article.time = time
            article.author = author
            article.description = description
            article.content = content
            print('新增数据成功')
            article.save()
        except:
            print("出现错误--------------------")


    return  render_template("register.html")

#启动应用
if __name__ == "__main__":
    app.run(
        #定义应用的端口
        port = 8002,
        #定义开启调试模式
        debug = True
    )