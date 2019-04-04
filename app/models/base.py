# -*- coding: utf-8 -*-
# @Time : 2019/4/3 22:07 
# @Author : Ymy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, SmallInteger, Integer

db = SQLAlchemy()

class Base(db.Model):
	__abstract__ = True   #添加了这个属性,，就不用添加主键，否则sqlalchemy会以为我们要创建表，必须有主键
	create_time = Column('create_time', Integer)
	status = Column(SmallInteger, default=1)

	def set_attr(self,attr):
		for k ,v in attr.items():
			if hasattr(self,k) and k != 'id':
				setattr(self, k, v)
