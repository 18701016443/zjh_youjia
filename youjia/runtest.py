#!/usr/bin/env python
# encoding: gbk

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/25 15:25
"""
from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import unittest
import os,time

#���巢���ʼ�

def send_mail(file_new):
    f = open(file_new,"rb")
    mail_body = f.read()
    f.close()

    #�Ը�������ʽ�����ʼ�
    att = MIMEText(mail_body, "base64", "gbk")
    att["Content-Type"] = "application/octet-stream"
    file_name = file_new.split("./report/")[1]
    print(file_name)
    att["Content-Disposition"] = "attachment;filename="+file_name
    msgRoot = MIMEMultipart("related")
    msgRoot["Subject"] = "�Զ������Ա���"
    #�ʼ�����
    # msgRoot.attach(MIMEText("����PC�Զ������Ա��棬�����~~","plain","utf-8"))
    msgRoot.attach(MIMEText(mail_body,"html","gbk"))
    msgRoot.attach(att)

    msgRoot["From"] = "18701016443@163.com"
    msgRoot["To"] = "zhangjiaheng_dz@mayi.com"
    # msgRoot["From"] = "bxj3416162@163.com"
    # msgRoot["To"] = "buxiangjie@huirendai.net"


    smtp = smtplib.SMTP()
    smtp.connect("smtp.163.com")
    smtp.login("18701016443", "zjh18701016443")
    smtp.sendmail("18701016443@163.com", "zhangjiaheng_dz@mayi.com", msgRoot.as_string())
    smtp.quit()
    print("email has send out")


    #��������htmlģʽ���͵��ʼ�
    # msg = MIMEText(mail_body,"html","utf-8")
    # msg["Subject"] = Header("�Զ������Ա���","utf-8")
    #
    # msg["From"] = "18701016443@163.com"
    # msg["To"] = "zhangjiaheng_dz@mayi.com"
    #
    # smtp = smtplib.SMTP()
    # smtp.connect("smtp.163.com")
    # smtp.login("18701016443","zjh18701016443")
    # smtp.sendmail("18701016443@163.com","zhangjiaheng_dz@mayi.com",msg.as_string())
    # smtp.quit()
    # print("email has send out")

#���Ҳ��Ա���Ŀ¼���ҵ��������ɵĲ��Ա����ļ�

def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn:os.path.getmtime(testreport + "\\" + fn))
    file_new = os.path.join(testreport,lists[-1])
    print(file_new)
    return file_new

if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = "./report/"+ now +"result.html"

    fp = open(filename,"w")
    runner = HTMLTestRunner(stream=fp,
                            title="PC�Զ������Ա���",
                            description="���� win10  ��������ȸ�/65��")

    discover = unittest.defaultTestLoader.discover("./test_cases/",
                                                   pattern="test_*.py")

    runner.run(discover)
    fp.close()
    file_path = new_report("./report/")
    send_mail(file_path)
