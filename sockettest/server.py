import socket

# #使用ipv4 和TCP协议
# sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #第一个参数为空代表绑定所有主机
# sock.bind(('',8000))
# print('this is socket_server:127.0.0.1:8000')
# sock.listen(5)
# con,add = sock.accept()
# print('%s is connected'%add[0])
# print(con.recv(512))
# con.send(b'hello I am your server')
# sock.close()

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('127.0.0.1',8000))
sock.listen(5)
con,add = sock.accept()
while True:
    recvs = con.recv(512)
    print(recvs)
    if recvs =='break':
        break
    sends = b'input(">>>")'
    sends = b'sends'
    con.send(bytes(sends))
    if sends=='break':
        break
sock.close()
