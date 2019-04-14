# -*- coding: utf-8 -*-
# @Time : 2019/4/14 19:54 
# @Author : Ymy
from enum import Enum
class PendingStatus(Enum):
	"""
	交易状态
	"""
	waiting = 1
	success = 2
	reject = 3
	redraw = 4