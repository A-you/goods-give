from app import db
from . import web
from flask import render_template, request
from app.forms.auth import RegisterForm
from app.models.user import User

__author__ = '七月'


@web.route('/register', methods=['GET','POST'])
def register():
    print (request)
    form = RegisterForm(request.form)
    user = User()
    if request.method == 'POST' and form.validate():
        user.set_attr(form.data)
        # user.password = generate_password_hash(form.password.data)  #机械式加密，
    # user.email='ddsdd'  #这种方式有点笨，如果传入多个值
    # user.password = '123456'
    # user.nickname = 'wwww'
        db.session.add(user)
        db.session.commit()
    form =form
    return render_template('auth/register.html', form=form)


@web.route('/login', methods=['GET', 'POST'])
def login():
    pass


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    pass


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    pass


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    pass
