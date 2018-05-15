import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr,formataddr

def _format_addr(s):
    name,addr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

from_addr = "944974531@qq.com"
password = "jmcumoxpqbnxbbga"
# to_addr = "fanglijuan@baibu.la,376699155@qq.com"
to_addr = "fanglijuan@baibu.la"
smtp_server = "smtp.qq.com"

msg = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>大吉大利，今晚吃鸡 <a href="http://www.sohu.com/a/208713682_755197">吃鸡</a>...</p>' +
    '</body></html>', 'html', 'utf-8')
msg['From'] = _format_addr('吃鸡邀请者 <%s>' % from_addr)
msg['To'] = _format_addr('鸡 <%s>' % to_addr)
msg['Subject'] = Header('吃鸡帖', 'utf-8').encode()
server = smtplib.SMTP_SSL(smtp_server,465)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()