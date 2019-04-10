# -*- coding: utf-8 -*-
# @Time : 2019/4/10 16:26 
# @Author : Ymy

#用传统的方法__enter__和__exit__定义上下文管理器
# class MyResource:
# 	def  __enter__(self):
# 		print('connect to resource')
# 		return self
#
# 	def  __exit__(self, exc_type, exc_val, exc_tb):
# 		print( exc_type, exc_val, exc_tb)
# 		print('close resource connection')
#
# 	def query(self):
# 		print('query data')
#
# with MyResource() as r:
# 	r.query()

#运用python自带的上下文管理器
from contextlib import contextmanager

# class MyResource:
# 	# def  __enter__(self):
# 	# 	print('connect to resource')
# 	# 	return self
#
# 	# def  __exit__(self, exc_type, exc_val, exc_tb):
# 	# 	print( exc_type, exc_val, exc_tb)
# 	# 	print('close resource connection')
#
# 	def query(self):
# 		print('query data')
#
# @contextmanager
# def make_my_resource():
# 	print('connect to resource')
# 	yield MyResource()
# 	print('close resource connection')
#
#
# with make_my_resource() as r:
# 	r.query()

@contextmanager
def book_mark():
	print('《', end='')
	yield
	print('》', end='')

with book_mark():
	print('这是一个书名', end='')