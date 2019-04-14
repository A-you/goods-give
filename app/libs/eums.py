# -*- coding: utf-8 -*-
# @Time : 2019/4/14 19:54 
# @Author : Ymy
from enum import Enum
class PendingStatus(Enum):
	"""
	交易状态
	"""
	Waiting = 1
	Success = 2
	Reject = 3
	Redraw = 4