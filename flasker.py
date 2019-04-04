# -*- coding: utf-8 -*-
# @Time : 2019/3/31 22:36 
# @Author : Ymy
from app import create_app
app = create_app()
#
#
# #搬迁到app文件夹下
# # app = Flask(__name__)
# # @app.route('/hello')
# # def hello():
# # 	return 'hello,word'
# # app.run()
# if __name__ == '__main__':
# 	app.run(host='0.0.0.0', debug=True)


# from flask import Flask
# app = Flask(__name__)
#
# @app.route('/index')
# def index():
# 	return 'hello'

if __name__ == '__main__':
	app.run()