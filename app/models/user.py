# -*- coding: utf-8 -*-
# @Time : 2019/4/3 22:07 
# @Author : Ymy
from sqlalchemy import Column, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship
from app.models.base import Base
from werkzeug.security import generate_password_hash

class User(Base):
	#__tablename__ = 'user1'#更改表名
	id = Column(Integer, primary_key=True)
	_password = Column('password',String(128))
	nickname = Column(String(24), nullable=False)
	phone_number = Column(String(18), unique=True)
	email = Column(String(50), unique=True, nullable=False)
	confirmed = Column(Boolean, default=False)
	beans = Column(Float, default=0)
	send_counter = Column(Integer, default=0)
	receive_counter = Column(Integer, default=0)

	@property
	def password(self):   #属性读取
		return self._password

	@password.setter   #属性的写入
	def password(self, raw):
		self._password = generate_password_hash(raw)