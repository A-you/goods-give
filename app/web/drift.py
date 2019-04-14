from flask import flash, redirect, url_for
from flask_login import login_required, current_user

from app.models.gift import Gift
from . import web

__author__ = '七月'


@web.route('/drift/<int:gid>', methods=['GET', 'POST'])
@login_required
def send_drift(gid):
    """
    想他人请求礼物
    :param gid:
    :return:
    """
    current_gift = Gift.query.get_or_404()
    if current_gift.is_yourself_gift(current_user.id): #判断书籍是不是登录自己的
        flash('这本书是你自己的')
        return redirect(url_for('web.book_detail', isbn = current_gift.isbn))
    pass


@web.route('/pending')
def pending():
    pass


@web.route('/drift/<int:did>/reject')
def reject_drift(did):
    pass


@web.route('/drift/<int:did>/redraw')
def redraw_drift(did):
    pass


@web.route('/drift/<int:did>/mailed')
def mailed_drift(did):
    pass
