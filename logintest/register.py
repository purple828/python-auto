#简单的去除重复用户名的注册案例
myfile = open("myfile.txt","a+")
lines =open("myfile.txt","r").readlines()
context = [x.rstrip() for x in lines]
print('context----------{}'.format(context))
accounts = [x.split(':')[0] for x in context]
print('accounts----------{}'.format(accounts))

while True:
    account = input("please input your Id :")
    flag = True
    while flag:
        if account in accounts:
            print("your id is exist ,please check!")
            account = input("====>please input your Id again:")
        else:
            flag = False
    if account == '':
        print("please input your id again!")
        continue
    passwd = input("please input your passwd:")
    if passwd == '':
        print("please input your passwd again!")
        continue
    str1 = "%s:%s\n"%(account,passwd)
    myfile.write(str1)
    myfile.flush()
    print("congratulations!")
    break

myfile.close()