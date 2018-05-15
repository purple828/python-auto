import smtplib
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr,formataddr
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from_addr = "944974531@qq.com"
password = "jmcumoxpqbnxbbga"
to_addr = "fanglijuan@baibu.la"
smtp_server = "smtp.qq.com"

def _format_addr(s):
    print('----------------s',s)
    name,addr = parseaddr(s)
    print('******************name',name)
    print('----------------addr',addr)
    return formataddr((Header(name,'utf-8').encode(),addr))

#邮件对象
msg = MIMEMultipart()
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

#邮件正文是MIMEText
# msg.attach(MIMEText('send with file','plain','utf-8'))

msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p><img src="cid:0"></p>' +
    '</body></html>', 'html', 'utf-8'))

#添加附件就是加上一个MiMEBase，从本地读取一张图片
with open(r'C:\Users\fff\Desktop\picture\cat3.jpg','rb') as f:
    #设置附件的MIME和文件名，这里是jpg类型
    mime = MIMEBase('image','jpg',filename='cat3.jpg')
    #加上必要的头信息
    mime.add_header('Content-Disposition','attachment',filename='cat3.jpg')
    mime.add_header('Content-ID','<0>')
    mime.add_header('X-Attachment-Id','0')
    #把附件的内容读进来
    mime.set_payload(f.read())
    #用Base64编码
    encoders.encode_base64(mime)
    msg.attach(mime)

server = smtplib.SMTP_SSL(smtp_server,465)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()

