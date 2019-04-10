from flask import current_app, flash

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
    if current_user.can_save_to_list(isbn):
        try:
            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id
            # current_user.beans += 0.5 #写死的办法
            current_user.beans = current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gift)
            db.session.commit()  # 这句其实已经有了事物的方法
            return '添加成功'
        except Exception as e:
            db.session.rollback()
            raise e
    else:
        flash('这本书已经存在心愿清单或礼物清单，请不要重复添加')

@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass



