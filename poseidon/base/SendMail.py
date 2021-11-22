# coding=utf-8

__author__ = 'songmengyun'

import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.header import Header
from pytest_testconfig import config as pyconfig


class SendMail():

    def __init__(self, sender, receiver, mail_title, smtp_server='xxx@xxx.com', smtp_port=25,
                 mail_user=None, mail_pwd=None, message=None):
        self.sender = sender
        self.receiver = receiver
        self.mail_title = mail_title
        self.message = message

        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.mail_user = mail_user
        self.mail_pwd = mail_pwd

    def _get_html_report_path(self):
        html_path = pyconfig['logfile'].get('html')
        return html_path

    def _read_html_report(self):
        path = self._get_html_report_path()
        with open(path, 'rb') as f:
            mail_body = f.read()
        return mail_body

    def html_report(self, name, json_report_dict, url):
        summary = json_report_dict['report']['summary']
        mail_msg = """
                <p>Hi, All:</p>
                <p>以下是：%s(%s)：</p>
                <p>总用例数:%s</p>
                <p><font style='color:green;'>成功:%s</font> &nbsp; <font style='color:red;'>失败:%s</font> &nbsp; <font style='color:gray;'>跳过:%s</font></p>
                <p>执行时长: %s</p>
                <p><a href="%s">点击查看报告详情</a></p>
                """%(name, pyconfig['env'], summary.get('num_tests'),
                     summary.get('passed', 0),summary.get('failed', 0),
                     summary.get('skipped', 0),summary.get('duration', 0),  url)
        return mail_msg

    def send_mail(self):
        '''发送普通邮件'''
        message = MIMEText(self.message, 'plain', _charset="utf-8")
        message['Subject'] = Header(self.mail_title, 'utf-8')   # 标题
        message['From'] = Header("%s" % (self.sender), 'utf-8')  # 发送人，没有实际作用，
        message['To'] = Header(','.join(self.receiver), 'utf-8')  # 收件人
        self._send(message)

    def send_mail_html(self):
        '''发送html邮件'''
        receivers = self.receiver  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
        mail_body = self._read_html_report()

        # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
        message = MIMEText(mail_body , 'html' , 'utf-8')
        message['Subject'] = Header(self.mail_title, 'utf-8')   # 标题
        message['From'] = Header("%s" % (self.sender), 'utf-8')
        message['To'] = Header(','.join(self.receiver), 'utf-8')  # 收件人

        try:
            smtpObj = smtplib.SMTP(self.smtp_server, self.smtp_port)
            # smtpObj.starttls()
            smtpObj.set_debuglevel(1)   # 打印出和SMTP服务器交互的所有信息
            smtpObj.sendmail(self.sender , receivers , message.as_string())
            logging.info("邮件发送成功")
        except smtplib.SMTPException as e:
            logging.error("Error: 邮件发送失败")
            raise e
        finally:
            smtpObj.quit()

    def send_mail_html_ssl(self):
        '''发送html邮件'''
        mail_body = self._read_html_report()

        # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
        message = MIMEText(mail_body , 'html' , 'utf-8')
        message['Subject'] = Header(self.mail_title, 'utf-8')   # 标题
        message['From'] = Header("%s" % (self.sender), 'utf-8')
        message['To'] = Header(','.join(self.receiver), 'utf-8')  # 收件人
        self._send(message)

    def send_mail_multipart(self, file_path):
        '''发送带附件邮件'''

        message = MIMEMultipart()
        message.attach(MIMEText(self.message, 'html', _charset="utf-8"))
        att = MIMEText(open(file_path, 'rb').read(), 'base64', 'utf-8') # 构造附件1
        att["Content-Type"] = 'application/octet-stream'
        att.add_header("Content-Disposition", "attachment", filename=("gbk", "", self.mail_title))  # 附件名称非中文时的写法
        message.attach(att)
        message['Subject'] = Header(self.mail_title, 'utf-8')   # 标题
        message['From'] = Header("%s" % (self.sender), 'utf-8')
        message['To'] = Header(','.join(self.receiver), 'utf-8')  # 收件人
        self._send(message)

    def send_mail_pic_multipart(self, pic_path):
        '''发送带图片邮件'''
        message = MIMEMultipart()
        message.attach(MIMEText(self.message, 'html', _charset="utf-8"))
        message['Subject'] = Header(self.mail_title, 'utf-8')   # 标题
        message['From'] = Header("%s" % (self.sender), 'utf-8')
        message['To'] = Header(','.join(self.receiver), 'utf-8')  # 收件人
        with open(pic_path, 'rb') as fp:
            msgImage = MIMEImage(fp.read())
        msgImage.add_header('Content-ID', '<image>')   # # 定义图片 ID，在 HTML 文本中引用
        message.attach(msgImage)
        self._send(message)

    def _send(self, message):
        '''
        发送邮件
        :param message:
        :return:
        '''
        with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as smtp:
            # 登录发邮件服务器
            smtp.login(user = self.mail_user, password = self.mail_pwd)
            # 实际发送、接收邮件配置
            smtp.sendmail(from_addr = self.sender, to_addrs=self.receiver, msg=message.as_string())


