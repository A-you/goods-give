from flask import current_app, flash, redirect, url_for, render_template
from flask_login import login_required, current_user

from app import db
from app.models.wish import Wish
from app.view_models.wish import MyWishes
from . import web

__author__ = '七月'


@web.route('/my/wish')
@login_required
def my_wish():
    uid = current_user.id
    wishes_of_my  = Wish.get_user_wishes(uid)
    isbn_list = [wish.isbn for wish in wishes_of_my]
    gift_count_list = Wish.get_gift_counts(isbn_list)
    view_model = MyWishes(wishes_of_my, gift_count_list)
    return render_template('my_wish.html', wishes = view_model.gifts)


@web.route('/wish/book/<isbn>')
@login_required
def save_to_wish(isbn):
    if current_user.can_save_to_list(isbn):
        # try:
        with db.auto_commit():
            wish = Wish()
            wish.isbn = isbn
            wish.uid = current_user.id
            # current_user.beans += 0.5 #写死的办法
            # current_user.beans = current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(wish)
            # db.session.commit()  # 这句其实已经有了事物的方法
        # except Exception as e:
        #     db.session.rollback()
        #     raise e
        return '成功'
    else:
        flash('这本书已经存在心愿清单或礼物清单，请不要重复添加')
    return  redirect(url_for('web.book_detail',isbn=isbn))


@web.route('/satisfy/wish/<int:wid>')
def satisfy_wish(wid):
    pass


@web.route('/wish/book/<isbn>/redraw')
def redraw_from_wish(isbn):
    pass
