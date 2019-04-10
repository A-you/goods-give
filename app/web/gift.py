from flask import current_app

from app import db
from app.models.gift import Gift
from . import web
from flask_login import login_required, current_user
__author__ = '七月'


@web.route('/my/gifts')
@login_required
def my_gifts():
    return 'hello,gifts'


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    gift = Gift()
    gift.isbn = isbn
    gift.uid = current_user.id
    current_user.beans = current_app.config['BEANS_UPLOAD_ONE_BOOK']
    db.session.add(gift)
    db.session.commit()
    return '添加成功'

@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass



