# -*- coding: utf-8 -*-
# @Time : 2019/4/3 22:07 
# @Author : Ymy
from app import login_manager
from sqlalchemy import Column, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship

from app.libs.helper import is_isbn_or_key
from app.models.base import Base
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app.models.gift import Gift
from app.models.wish import Wish
from app.spider.yushu_book import YuShuBook


class User(UserMixin,Base):
	"""
	继承usermixin，其中cookie是用get_id来取，如果另需，可以重写这个方法
	"""
	#__tablename__ = 'user1'#更改表名
	id = Column(Integer, primary_key=True)
	_password = Column('password',String(128), nullable=False)
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

	def check_password(self,raw):
		return check_password_hash(self._password,raw)

	#检查加入礼物清单中的isbn是否合法
	def can_save_to_list(self,isbn):
		if is_isbn_or_key(isbn) != 'isbn':
			return False
		yushu_book = YuShuBook()
		yushu_book.search_by_isbn(isbn)
		if not yushu_book.first:
			return False
		#不允许一个用户同时赠送多本相同的图书
		#一个用户不可能同时成为赠送者和索要者
		gifting = Gift.query.filter_by(uid =self.id, isbn=isbn, launched =False).first()
		wishing= Wish.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()
		if not gifting and not wishing:
			return True
		else:
			return False

#该方法在类的外面
@login_manager.user_loader
def get_user(uid):
	return User.query.get(int(uid))