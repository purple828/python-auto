import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr,formataddr
from email import encoders

#案例一
# _user = "944974531@qq.com"
# _pwd  = "jmcumoxpqbnxbbga"
# _to   = "fanglijuan@baibu.la"
#
# msg = MIMEText("Test")
# msg["Subject"] = "don't panic"
# msg["From"]    = _user
# msg["To"]      = _to
#
# try:
#     s = smtplib.SMTP_SSL("smtp.qq.com", 465)
#     s.login(_user, _pwd)
#     s.sendmail(_user, _to, msg.as_string())
#     s.quit()
#     print("Success!")
# except :
#     print ("Falied")
#

#********************案例2
# 输入Email地址和口令:
# from_addr = input('From: ')
# password = input('Password: ')
# # 输入收件人地址:
# to_addr = input('To: ')
# # 输入SMTP服务器地址:
# smtp_server = input('SMTP server: ')
#
# msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
#
# server = smtplib.SMTP_SSL(smtp_server, 465) # SMTP协议默认端口是25
# server.set_debuglevel(1)
# server.login(from_addr, password)
# server.sendmail(from_addr, [to_addr], msg.as_string())
# server.quit()

def _format_addr(s):
    name,addr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

# from_addr = input('From: ')
# password = input('Password: ')
# to_addr = input('To: ')
# smtp_server = input('SMTP server: ')

from_addr = "944974531@qq.com"
password = "jmcumoxpqbnxbbga"
to_addr = "fanglijuan@baibu.la,376699155@qq.com"
smtp_server = "smtp.qq.com"

msg = MIMEText('杀鸡，哼哼哼。。。','plain','utf-8')
msg['From'] = _format_addr('杀鸡者 <%s>' % from_addr)
msg['To'] = _format_addr('鸡 <%s>' % to_addr)
msg['Subject'] = Header('杀鸡帖', 'utf-8').encode()
server = smtplib.SMTP_SSL(smtp_server,465)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()