# -*- coding: utf-8 -*-
# @Time : 2019/4/10 15:39 
# @Author : Ymy
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base
class Wish(Base):
	"""
	心愿
	"""
	id = Column(Integer, primary_key=True)
	user = relationship('User')
	uid = Column(Integer, ForeignKey('user.id'))
	isbn = Column(String(15), nullable=False)
	launched = Column(Boolean, default=False)