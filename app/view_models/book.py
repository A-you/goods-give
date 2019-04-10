# -*- coding: utf-8 -*-
# @Time : 2019/4/3 11:26 
# @Author : Ymy
from app.libs.helper import get_isbn


class BookViewModel:

	def __init__(self,data):
		self.title = data['title']
		self.author = '、'.join(data['author'])
		self.binding = data['binding']
		self.publisher = data['publisher']
		self.image = data['image']
		self.price = '￥' + data['price'] if data['price'] else data['price']
		self.isbn = get_isbn(data)
		self.pubdate = data['pubdate']
		self.summary = data['summary']
		self.pages = data['pages']

	@property
	def intro(self):
		#如果某项的值为空，则过滤掉该项。
		intros = filter(lambda x: True if x else False,
		                [self.author, self.publisher, self.price])
		return ' / '.join(intros)

class BookCollection:
	def __init__(self):
		self.total = 0
		self.books = []
		self.keyword = None

	def fill(self, yushu_book, keyword):
		self.total = yushu_book.total
		self.books = [BookViewModel(book) for book in yushu_book.books]
		self.keyword = keyword

class BookViewModelOld:
	#类应该特征（类变量，实例变量）。这个类就是一个伪面向对象。只具有行为（方法）

	"""
	package_single处理isbn搜索，单个
	package_collection处理关键字搜索，多个数据，多本数据
	"""
	@classmethod
	def package_single(cls, data, keyword):
		returned = {
			'book': [],
			'total': 0,
			'keyword': keyword
		}
		if data:
			returned['total'] = 1
			returned['book'] = [cls.__cut_book_data(data)]
		return  returned

	@classmethod
	def package_collection(cls, data, keyword):
		returned = {
			'books': [],
			'total': 0,
			'keyword': keyword
		}
		if data:
				returned['total'] = data['total']
				returned['books'] = [cls.__cut_book_data(book) for book in data['books']]
		return returned

	@classmethod
	def __cut_book_data(cls,data):
		book = {
			'title': data['title'],
			'author': '、'.join(data['author']),
			'publisher': data['publisher'],
			'image': data['images'],
			'price': data['price'],
			'summary': data['summary'] or '',
			'pages': data['pages'] or ''
		}
		return book