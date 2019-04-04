# -*- coding: utf-8 -*-
# @Time : 2019/4/2 12:48 
# @Author : Ymy
from app.libs.http import HTTP

class YuShuBook:
    """
        鱼书API提供数据
    """
    per_page = 15
    # isbn_url = 'https://api.douban.com/v2/book/isbn/{}'
    # keyword_url = 'https://api.douban.com/v2/book/search?q={}&count={}&start={}'
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        self.total = 0
        self.books = []

    def __fill_single(self, data):
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_collection(self, data):
        self.total = data['total']
        self.books = data['books']

    def search_by_isbn(self, isbn):
        url = self.isbn_url.format(isbn)
        result = HTTP.get(url)
        self.__fill_single(result)
        # return result

    def search_by_keyword(self, key, page=1):
        url = self.keyword_url.format(key, self.per_page, self.calculate_start(page))
        result = HTTP.get(url)
        self.__fill_collection(result)
        # return result

    def calculate_start(self,page):
        return (page - 1) * self.per_page

    @property
    def first(self):
        return self.books[0] if self.total >= 1 else None