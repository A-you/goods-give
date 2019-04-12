# -*- coding: utf-8 -*-
# @Time : 2019/4/11 15:43 
# @Author : Ymy


from app.view_models.book import BookViewModel

# MyGift = namedtuple('MyGift',['id','book', 'wishes_count'])

class MyWishes:
	def __init__(self, gifts_of_my, wish_count_list):
		self.gifts = []
		self.__gifts_of_my = gifts_of_my
		self.__wish_count_list = wish_count_list
		self.gifts = self.__parse()

	def __parse(self):
		tem_gifts = []
		for gift in self.__gifts_of_my:
			tem_gifts.append(self.__marching(gift))
		return tem_gifts

	def __marching(self,gift):
		count = 0
		for wish_count in self.__wish_count_list:
			if wish_count['isbn'] == gift.isbn:
				count = wish_count['count']
		r = {
			'wishes_count': count,
			'book': BookViewModel(gift.book),
			'id': gift.id
		}
		# my_gift = MyGift(gift.id, BookViewModel(gift.book), count)   #为了方便使用rest api   还是不使用对象
		return r