import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options

tornado.options.define("port",default=8001,type=int,help="run server on the given port.")#定义服务器监听端口选项
tornado.options.define("itcast",default=[],type=str,multiple=True,help="itcast subject.")#无意义，演示多值情况

class IndexHandler(tornado.web.RequestHandler):
    #主路由处理类
    def get(self):
        #对应http的get请求方式
        self.write("Hello Itcast--------------")

'''
Application:
是Tornado Web框架的核心应用类，与服务器对接的接口，里面保存了路由信息表
其初始化接收的第一个参数就是一个路由信息映射元组的列表，其listen(端口)方法用来创建一个http
服务器实例，并绑定到给定端口（此时服务器并未开启监听）

tornado.ioloop:
tornado的核心io循环模块，封装了Linux的epoll和BSD的kqueue,高性能的基石
IOLoop.current()    返回当前线程的IOLoop实例
IOLoop.start()      启动IOLoop实例的I/O循环，同时服务器监听被打开

'''
if __name__ == "__main__":
    #web应用对象
    app = tornado.web.Application([(r"/",IndexHandler),])
    #创建了一个http服务器示例并绑定到给定端口
    # app.listen(8001)

    #app.listen(端口)是一种简写
    http_server = tornado.httpserver.HTTPServer(app)
    # http_server.listen(8001)
    # http_server.bind(8001)
    http_server.listen(tornado.options.options.port)
    # http_server.start(0)  linux下才可运行
    '''
    http_server.bind(port)方法是将服务器绑定到指定端口。

    http_server.start(num_processes=1)方法指定开启几个进程，
    参数num_processes默认值为1，即默认仅开启一个进程；
    如果num_processes为None或者<=0，则自动根据机器硬件的cpu核芯数创建同等数目的子进程；
    如果num_processes>0，则创建num_processes个子进程。
    '''


    tornado.ioloop.IOLoop.current().start()