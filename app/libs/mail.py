# -*- coding: utf-8 -*-
# @Time : 2019/4/12 21:32 
# @Author : Ymy
from threading import Thread

from flask import current_app, render_template
# from werkzeug.contrib import
# import logging
from app import mail
from flask_mail import Message

def send_async_email(app,mes):
	with app.app_context():
		try:
			mail.send(mes)
		except Exception as e:
			print(e)
def send_mail(to=None, subject=None, template=None, **kwargs):
	# msg= Message('测试邮件',sender='582838918@qq.com',body='邮件测试', recipients=['767024056@qq.com'])
	msg = Message('[物品网]'+' ' + subject, sender= current_app.config['MAIL_USERNAME'], recipients=[to])
	msg.html = render_template(template, **kwargs)
	# app = current_app.
	#直接传入current_app到send_async_email无效，因为curren_app是在栈顶获取到的。现在又线程隔离
	#获取真实flask对象，不在使用代理模式，它默认是使用代理模式
	app  = current_app._get_current_object()
	thr = Thread(target=send_async_email, args=[app,msg])
	thr.start()
	# mail.send(msg)
