# -*- coding: utf-8 -*-
# @Time : 2019/4/2 10:22 
# @Author : Ymy
import json
from flask import request, jsonify, make_response, render_template,flash
from flask_login import current_user

from app.models.gift import Gift
from app.models.wish import Wish
from app.view_models.book import BookViewModel, BookCollection
from app.view_models.trade import TradeInfo
from . import web
from app.forms.book import SearchForm
from app.spider.yushu_book import YuShuBook
from app.libs.helper import is_isbn_or_key

@web.route('/book/search',)
def search():
	# q = request.args['q']   #获取参数
	# page = request.args['page']
	form = SearchForm(request.args)
	books = BookCollection()  #处理多数据
	if form.validate():
		q = form.q.data.strip() #获取form验证通过的参数
		isbn_or_key = is_isbn_or_key(q)
		page = form.page.data
		yushu_book = YuShuBook()
		if isbn_or_key == 'isbn':
			yushu_book.search_by_isbn(q)
			# result = YuShuBook.search_by_isbn(q)  if YuShuBook.search_by_isbn(q) else ''
			# result =BookViewModel.package_single(result, q)
		else:
			yushu_book.search_by_keyword(q, page)
			#老方法对应view_model中的伪类
			# result = YuShuBook.search_by_keyword(q)
			# result = BookViewModel.package_collection(result, q)
		# return json.dumps(result),200,{'content-type': 'application/json'}
		books.fill(yushu_book, q) #这是一个对象，且不是普通的对象，所以不能用__dict__。它是的属性同样是一个对象。
		# return json.dumps(books, default=lambda o: o.__dict__)  #后面函数采用了递归的思想，如果属性为一个对象，则继续调用__dict__方法
		# return jsonify(books)
	else:
		flash('搜索的关键字不符合要求，请重新输入关键字')
	return render_template('search_result.html', books=books)


@web.route('/book/<isbn>/detail')
# @cache.cached(timeout=1800)
def book_detail(isbn):
	#默认情况下用户既不是赠送者，也不是索要者
	has_in_gifts = False
	has_in_wishes = False

	if current_user.is_authenticated:
		if Gift.query.filter_by(uid=current_user.id, isbn=isbn, launched=False).first():
			has_in_gifts = True
		if Wish.query.filter_by(uid=current_user.id, isbn=isbn, launched=False).first():
			has_in_wishes = True

	#取数据的详情数据
	yushu_book = YuShuBook()
	yushu_book.search_by_isbn(isbn)
	book = BookViewModel(yushu_book.first)

	trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
	trade_wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()

	trade_gifts_model = TradeInfo(trade_gifts)
	trade_wishes_model = TradeInfo(trade_wishes)

	return render_template('book_detail.html', book=book,
	                       wishes = trade_wishes_model  , gifts = trade_gifts_model,
	                       has_in_gifts = has_in_gifts, has_in_wishes=has_in_wishes)