# -*- coding: utf-8 -*-
# @Time : 2019/4/10 15:39 
# @Author : Ymy
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, desc, func
from sqlalchemy.orm import relationship

from app.models.base import Base, db

from app.spider.yushu_book import YuShuBook


class Wish(Base):
	"""
	心愿
	"""
	id = Column(Integer, primary_key=True)
	user = relationship('User')
	uid = Column(Integer, ForeignKey('user.id'))
	isbn = Column(String(15), nullable=False)
	launched = Column(Boolean, default=False)

	# 查询用户的礼物清单
	@classmethod
	def get_user_wishes(cls, uid):
		wishes = Wish.query.filter_by(uid=uid, launched=False).order_by(desc(Wish.create_time)).all()
		return wishes

	#获取数组中每本书的想要赠送的人数。对于单本书来说就是有意向赠送这本书的人数
	@classmethod
	def get_gift_counts(cls, isbn_list):
		from app.models.gift import Gift
		count_list = db.session.query(func.count(Gift.id), Gift.isbn).filter(Gift.launched == False,
		                                                                     Gift.isbn.in_(isbn_list),
		                                                                     Gift.status == 1).group_by(Gift.isbn).all()
		# count_list = [EachGiftWishCount(w[0],w[1]) for w in count_list]
		count_list = [{'count': w[0], 'isbn': w[1]} for w in count_list]
		return count_list

	@property
	def book(self):
		yushu_book = YuShuBook()
		yushu_book.search_by_isbn(self.isbn)
		return yushu_book.first

