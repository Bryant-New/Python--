# 导入模块
import smtplib  # smtplib 用于邮件的发信动作
from email.mime.text import MIMEText  # email 用于构建邮件内容
from email.header import Header  # 用于构建邮件头
import csv
# 引用csv模块，用于读取邮箱信息

# 定义变量

# 发信方的信息：发信邮箱，QQ邮箱授权码
from_addr = input('请输入登录邮箱：')
password = input('请输入邮箱授权码：')

# 发信服务器
smtp_server = 'smtp.qq.com'
text = '''亲爱的学员你好！
        我是研究生，希望你以后能越来越好'''

# 待写入csv文件的收件人数据：人名+邮箱
# 记得替换成你要发送的名字和邮箱
data = [['杨光', '18811316839@163.com'], ['杨光容', 'yangguang197@mails.ucas.edu.cn']]

# 写入收件人数据
with open('to_addrs.csv', 'w', newline='') as f:  # 使用with open语句新建一个to_addrs.csv文件
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)  # 将存在data变量中的数据一行行的写到to_addrs.csv中

# 读取收件人数据，并启动写信和发信流程
with open('to_addrs.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        to_addrs = row[1]
        msg = MIMEText(text, 'plain', 'utf-8')

    # 邮件头信息
        msg['From'] = Header(from_addr)
        msg['To'] = Header(",".join(to_addrs))
        msg['Subject'] = Header('python test')
    # 使用方法

    #  开启发信服务，这里使用的是加密传输
        server = smtplib.SMTP_SSL(smtp_server)
        server.connect(smtp_server, 465)
    # 登录发信邮箱
        server.login(from_addr, password)
    # 发送邮件
    try:
        server.sendmail(from_addr, to_addrs, msg.as_string())
        print('恭喜,发送成功')
    except:
        print('发送失败，请重试')

# 异常处理代码


# 关闭服务器
server.quit()

