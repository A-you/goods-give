# -*- coding: utf-8 -*-
# @Time : 2019/4/12 21:32 
# @Author : Ymy
from flask import current_app, render_template
# from werkzeug.contrib import
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from app import mail
from flask_mail import Message
def send_mail(to=None, subject=None, template=None, **kwargs):
	# msg= Message('测试邮件',sender='582838918@qq.com',body='邮件测试', recipients=['767024056@qq.com'])
	msg = Message('[物品网]'+' ' + subject, sender= current_app.config['MAIL_USERNAME'], recipients=[to])
	msg.html = render_template(template, **kwargs)
	mail.send(msg)
