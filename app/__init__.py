# -*- coding: utf-8 -*-
# @Time : 2019/4/2 10:00 
# @Author : Ymy
import os
from flask import Flask, request, current_app
from flask_login import LoginManager
from app.models.base import db

login_manager = LoginManager()
def register_web_blueprint(app):
     from app.web import web
     app.register_blueprint(web)

def create_app(config=None):
	app = Flask(__name__)
	register_web_blueprint(app)
	app.config.from_object('app.secure')
	app.config.from_object('app.settings')
	app.app_context()
	db.init_app(app)
	login_manager.init_app(app)
	login_manager.login_view = 'web.login'
	login_manager.login_message = '请重新登录'
	# db.create_all(app=app)
	with app.app_context():
		db.create_all()
	return app