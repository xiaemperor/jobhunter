import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

class SendMail:
    # 参数：jobsize:职位数量，keywords：查询的关键字，jobPlist:邮件中的职位列表
    def send(jobsize,keywords,jobPlist):
        # 第三方 SMTP 服务
        mail_host = "smtp.163.com"  # 设置服务器
        mail_user = "maven163@163.com"  # 用户名
        mail_pass = "mawenxia163"  # 口令 这边请使用自己的邮箱服务商的smtp服务口令

        # 邮件发送人
        sender = 'maven163@163.com'
        # 接收邮件的地址
        receivers = ['267007900@qq.com', 'xiaohan0930@126.com']
        # receivers = ['267007900@qq.com']
        msg = '<p>沈肖含，已为您查到'+str(jobsize)+'  条信息，关键字：'+str(keywords)+\
              jobPlist+\
              '</p><p><a href="http://www.cxhr.com/search/jobList.jsp">请点击查询</a></p>'
        # msg='邮件测试'
        print(msg)
        # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
        message = MIMEText(msg, 'html', 'utf-8')
        message['From'] = formataddr(["maven163@163.com", sender])
        message['To'] = formataddr(["267007900@qq.com", receivers[0]])

        subject = '职位订阅'
        message['Subject'] = subject



        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
            smtpObj.login(mail_user, mail_pass)
            smtpObj.sendmail(sender, receivers, message.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("Error: 无法发送邮件"+smtplib.SMTPException)
