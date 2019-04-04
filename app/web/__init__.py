# -*- coding: utf-8 -*-
# @Time : 2019/4/2 10:01 
# @Author : Ymy
from flask import  Blueprint, url_for

web = Blueprint('web',__name__)
from . import book
from . import auth
from . import drift
from . import gift
from . import main
from . import wish