myfile = open("myfile.txt",'r')
lines =myfile.readlines()
context = [x.rstrip() for x in lines]
accounts = [x.split(':')[0] for x in context]
print('accounts----------{}'.format(accounts))
islogin = 1
oklogin = 0
while True:
    if oklogin == 0:

        if islogin == 4:
            print("密码输入三次错误，再见")
            break
        else:
            account = input("please input your Id:")
            flag = True
            while flag:
                if account not in accounts:
                    print("你输入的用户名不存在，请确认")
                    account = input("please input your Id:")
                else:
                    flag = False
            passwd = input("please input your passwd:")
            for str in myfile:
                print("===str==={}".format(str))
                file_account = str.split(":")[0]
                file_passwd = str.split(":")[1]
                print("------file_account:{}".format(file_account))
                print("------file_passwd:{}".format(file_passwd))
                file_passwd = file_passwd[:-1]
                if file_account == account and file_passwd == passwd:
                    oklogin = 1
                    break
            print("你已输错{}次，还可以再输入{}次".format(islogin, 3 - islogin))
            islogin += 1
            continue
    else:
        print("congratulations!")
        break
myfile.close()
