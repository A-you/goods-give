# -*- coding: utf-8 -*-
# @Time : 2019/4/4 12:47 
# @Author : Ymy
from wtforms import Form,StringField,PasswordField
from wtforms.validators import length, DataRequired, Email, Length, ValidationError

from app.models.user import User


class RegisterForm(Form):
	email = StringField(validators=[DataRequired(),Length(8,64), Email(message='电子邮箱不符合规范')])
	password = PasswordField('密码', validators=[DataRequired(), Length(6, 20,message='密码长度不规范')])
	nickname = StringField('昵称', validators=[
		DataRequired(), Length(2, 10, message='昵称至少需要两个字符，最多10个字符')])

	def validate_email(self, field):
		#可以通过db.session来查询,
		if User.query.filter_by(email= field.data).first():
			raise ValidationError('电子邮件已被注册')

	def validate_password(self, field):
		#可以通过db.session来查询,
		if User.query.filter_by(email= field.data).first():
			raise ValidationError('昵称已被占用')