# 导入模块
import smtplib
from email.mime.text import MIMEText
from email.header import Header
# 定义变量

# 发信方的信息：发信邮箱，QQ邮箱授权码
from_addr = input('请输入登录邮箱：')
password = input('请输入邮箱授权码：')
# 收信方邮箱
to_addrs = []
while True:
    a = input('请输入收件人邮箱：')
    to_addrs.append(a)
    b = input('是否继续输入，n退出，任意键继续：')
    if b == 'n':
        break
# 发信服务器
smtp_server = 'smtp.qq.com'
text = '''亲爱的学员你好！
        我是研究生，希望你以后能越来越好'''
msg = MIMEText(text, 'plain', 'utf-8')
# 邮件头信息
msg['From'] = Header(from_addr)
msg['To'] = Header(",".join(to_addrs))
msg['Subject'] = Header('python test')
# 使用方法


# 开启发信服务，这里使用的是加密传输
server = smtplib.SMTP_SSL(smtp_server)
server.connect(smtp_server, 465)
# 登录发信邮箱
server.login(from_addr, password)
# 发送邮件
server.sendmail(from_addr, to_addrs, msg.as_string())
# 关闭服务器
server.quit()

