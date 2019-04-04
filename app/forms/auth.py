# -*- coding: utf-8 -*-
# @Time : 2019/4/4 12:47 
# @Author : Ymy
from wtforms import Form,StringField,PasswordField
from wtforms.validators import length, DataRequired, Email, Length


class RegisterForm(Form):
	email = StringField(validators=[DataRequired(),Length(8,64), Email(message='电子邮箱不符合规范')])
	password = PasswordField('密码', validators=[DataRequired(), Length(6, 20)])
	nickname = StringField('昵称', validators=[
		DataRequired(), Length(2, 10, message='昵称至少需要两个字符，最多10个字符')])