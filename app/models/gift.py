# -*- coding: utf-8 -*-
# @Time : 2019/4/3 22:07 
# @Author : Ymy
from flask import current_app
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, desc,distinct,func
from sqlalchemy.orm import relationship

from app.models.base import Base, db
from app.spider.yushu_book import YuShuBook
from collections import namedtuple #用于快速定义对象

EachGiftWishCount = namedtuple('EachGiftWishCount',['count','isbn'])


class Gift(Base):
	"""
	礼物模型
	"""
	id = Column(Integer, primary_key=True)
	user = relationship('User')
	uid = Column(Integer, ForeignKey('user.id'))
	isbn = Column(String(15), nullable=False)
	launched = Column(Boolean, default=False)
	# recipient_name = Column(String(20), nullable=False)
	# address = Column(String(100), nullable=False)
	# message = Column(String(200))
	# mobile = Column(String(20), nullable=False)
	# book_title = Column(String(50))
	# book_author = Column(String(30))
	# book_img = Column(String(50))
	# requester_id = Column(Integer, ForeignKey('user.id'))
	# requester = relationship('User')
	# requester_id = Column(Integer)
	# requester_nickname = Column(String(20))
	# gifter_id = Column(Integer)
	# gift_id = Column(Integer)
	# gifter_nickname = Column(String(20))

	def is_yourself_gift(self,uid):
		return True if self.uid == uid   else False


	#查询用户的礼物清单
	@classmethod
	def get_user_gifts(cls, uid):
		gifts = Gift.query.filter_by(uid=uid, launched=False).order_by(desc(Gift.create_time)).all()
		return gifts

	#根据isbn列表查询相关送的人和想要的人
	@classmethod
	def get_wish_counts(cls, isbn_list):
		from app.models.wish import Wish
		#filter和filter_by不同，filter需要接收表达式，filter_by接收关键字参数
		#需要用到mysql 的in查询来处理isbn_list
		#query中传入的数据机构能等查询出来的数据结构,func.count可以统计个数
		# 加上group_by就是分组统计，结构为[(个数,isbn),(个数,isbn).......]
		count_list = db.session.query(func.count(Wish.id),Wish.isbn).filter(Wish.launched == False,
		                              Wish.isbn.in_(isbn_list),
		                              Wish.status ==1).group_by(Wish.isbn).all()
		# count_list = [EachGiftWishCount(w[0],w[1]) for w in count_list]
		count_list = [{'count': w[0],'isbn': w[1]} for w in count_list]
		return count_list

	@property
	def book(self):
		yushu_book = YuShuBook()
		yushu_book.search_by_isbn(self.isbn)
		return yushu_book.first

	#对象代表一个礼物，具体
	#类是一个事物，是抽象的
	@classmethod
	def recent(self):
		#链式调用，主体是query
		recent_gift = Gift.query.filter_by(
			launched=False).order_by(
			desc(Gift.create_time)).limit(
			current_app.config['RECENT_BOOK_COUNT']).all()
		return recent_gift