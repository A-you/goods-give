# -*- coding: utf-8 -*-
# @Time : 2019/4/14 19:30 
# @Author : Ymy
from app.models.base import Base
from sqlalchemy import Column, Integer, String, SmallInteger


class Drift(Base):
	"""
	一次交易的具体信息
	"""

	id = Column(Integer, primary_key=True)

		#邮寄地址
	recipient_name = Column(String(20), nullable=False)
	address = Column(String(20), nullable=False)
	message = Column(String(200))
	mobile = Column(String(20), nullable=False)

	#书籍信息
	isbn = Column(String(13))
	book_title = Column(String(50))
	book_author = Column(String(30))
	book_ima = Column(String(50))

	#请求者信息
	requester_id = Column(Integer)
	requester_nickname = Column(String(20))

	#赠送者信息
	gifter_id = Column(Integer)
	gift_id = Column(Integer)
	gifter_nickname = Column(String(20))

	pending = Column('pending', SmallInteger, default=1)