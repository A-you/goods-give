# -*- coding: utf-8 -*-
# @Time : 2019/4/2 10:00 
# @Author : Ymy
import os
from flask import Flask, request, current_app
from app.models.base import db

def register_web_blueprint(app):
     from app.web import web
     app.register_blueprint(web)

def create_app(config=None):
	app = Flask(__name__)
	register_web_blueprint(app)
	app.config.from_object('app.secure')
	app.app_context()
	db.init_app(app)
	db.create_all(app=app)
	return app