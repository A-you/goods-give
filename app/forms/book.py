# -*- coding: utf-8 -*-
# @Time : 2019/4/2 11:45 
# @Author : Ymy
from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired, Regexp


class SearchForm(Form):
	q = StringField(validators=[Length(min=1, max=30)])
	page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)

class DriftForm(Form):
	recipient_name = StringField('收件人姓名', validators=[DataRequired(),Length(min=2, max=20,message='收件人姓名长度必须在2到20个长度')])
	# mobile = StringField('手机号', validators=[DataRequired(), Regexp('^1(0-9){10}$', 0, '请输入正确的手机号码')])
	mobile = StringField('手机号', validators=[DataRequired()])
	message = StringField('留言')
	address = StringField('邮寄地址',validators=[DataRequired(),Length(min=10,max=70,
	                                                               message='留言需要在10到70字之间')])
