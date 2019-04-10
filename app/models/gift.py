# -*- coding: utf-8 -*-
# @Time : 2019/4/3 22:07 
# @Author : Ymy
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base
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