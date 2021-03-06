# -*- coding: utf-8 -*-
# @Time : 2019/4/11 9:43 
# @Author : Ymy

class TradeInfo:
	def __init__(self, goods):
		self.total = 0
		self.trades = []
		self._parse(goods)

	def _parse(self,goods):
		self.total = len(goods)
		self.trades = [self._map_to_trade(single) for single in goods]

	def _map_to_trade(self, single):
		if single.create_datetime:
			time = single.create_datetime.strftime('%Y-%m-%d')
		else:
			time = '未知'
		return dict(
			user_name=single.user.nickname,
			time=time,
			id=single.id
		)