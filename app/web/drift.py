from flask import flash, redirect, url_for, render_template, request
from flask_login import login_required, current_user
from sqlalchemy import desc, or_

from app import db
from app.forms.book import DriftForm
from app.libs.mail import send_mail
from app.models.drift import Drift
from app.models.gift import Gift
from app.view_models.book import BookViewModel
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
    current_gift = Gift.query.get_or_404(gid)
    if current_gift.is_yourself_gift(current_user.id): #判断书籍是不是登录自己的
        flash('这本书是你自己的')
        return redirect(url_for('web.book_detail', isbn = current_gift.isbn))
    can = current_user.can_send_drift()
    if not can:
        return render_template('not_enough_beans.html', beans = current_user.beans)
    gifter = current_gift.user.summary
    form = DriftForm(request.form)
    if request.method == 'POST' and form.validate():
        save_drift(form, current_gift)
        send_mail(current_gift.user.email, '有人想要一本书', 'email/get_gift.html',
                   wisher=current_user,
                   gift=current_gift)
        return redirect('web.pending')
    return render_template('drift.html', gifter = gifter, user_beans = current_user.beans, form=form)

@web.route('/pending')
def pending():
    drifts = Drift.query.filter(or_(Drift.requester_id==current_user.id, Drift.gifter_id==current_user.id)).order_by(desc(Drift.create_time))


@web.route('/drift/<int:did>/reject')
def reject_drift(did):
    pass


@web.route('/drift/<int:did>/redraw')
def redraw_drift(did):
    pass


@web.route('/drift/<int:did>/mailed')
def mailed_drift(did):
    pass


def save_drift(drift_form, current_gift):
    with db.auto_commit():
        drift = Drift()
        drift_form.populate_obj(drift) #使用tform带的拷贝方法

        drift.gift_id = current_gift.id
        drift.requester_id = current_user.id
        drift.requester_nickname = current_user.nickname
        drift.gifter_nickname = current_gift.user.nickname
        drift.gifter_id = current_gift.user.id

        book = BookViewModel(current_gift.book)
        drift.book_title = book.title
        drift.book_author = book.author
        drift.book_img = book.image
        drift.isbn = book.isbn
        try:
            current_user.beans -= 1
        except Exception as e:
            print(e)
        db.session.add(drift)