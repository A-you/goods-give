# -*- coding: utf-8 -*-
# @Time : 2019/4/2 10:23 
# @Author : Ymy
"""
  工具类函数
"""
def is_isbn_or_key(q):
	isbn_or_key = 'key'
	if len(q) == 13 and q.isdigit():
		isbn_or_key = 'isbn'
	if '-' in q and len(q.replace('-', '')) == 10 and q.replace('-', '').isdigit():
		isbn_or_key = 'isbn'
	return isbn_or_key

def get_isbn(data_dict):
    isbn = data_dict.get('isbn')
    if not isbn:
        isbn = data_dict.get('isbn13')
        if not isbn:
            isbn = data_dict.get('isbn10')
    return isbn