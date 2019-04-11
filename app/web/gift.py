from flask import current_app, flash

from app import db
from app.models.gift import Gift
from . import web
from flask_login import login_required, current_user
__author__ = '七月'


@web.route('/my/gifts')
@login_required
def my_gifts():
    uid = current_user.id
    gifts_of_my = Gift.get_user_gifts(uid)
    isbn_list = [gift.isbn for gift in gifts_of_my]
    Gift.get_wish_counts(isbn_list)

    return 'hello,gifts'


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    if current_user.can_save_to_list(isbn):
        # try:
        with db.auto_commit():
            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id
            # current_user.beans += 0.5 #写死的办法
            current_user.beans = current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gift)
            db.session.commit()  # 这句其实已经有了事物的方法
        # except Exception as e:
        #     db.session.rollback()
        #     raise e
        return '成功'
    else:
        flash('这本书已经存在心愿清单或礼物清单，请不要重复添加')

@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass



