from app import db
from app.libs.mail import send_mail
from . import web
from flask import render_template, request, redirect, url_for, make_response, flash
from app.forms.auth import RegisterForm, LoginForm, EmailForm, ResetPasswordForm
from app.models.user import User
from flask_login import login_user

__author__ = '小尤'

# @web.route('/set/cookie')
# def set_cookie():
#     response = make_response("你好啊，小尤")
#     response.set_cookie('name','xiaoyou',100)
#     return response


@web.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm(request.form)
    user = User()
    if request.method == 'POST' and form.validate():
        with db.auto_commit():
            user.set_attr(form.data)
            # user.password = generate_password_hash(form.password.data)  #机械式加密，
        # user.email='ddsdd'  #这种方式有点笨，如果传入多个值
        # user.password = '123456'
        # user.nickname = 'wwww'
            db.session.add(user)
        return redirect(url_for('web.login'))
    form =form
    return render_template('auth/register.html', form=form)


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user,remember=True)
            next = request.args.get('next')
            if not next or next.startswith('/'):
                next = url_for('web.index')
            return redirect(next)
        else:
            flash('账号不存在')
    return render_template('auth/login.html', form=form)

@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    form = EmailForm(request.form)
    if request.method == 'POST':
        if form.validate():
            account_email = form.email.data
            user = User.query.filter_by(email=account_email).first_or_404()
            token = user.generate_password()
            send_mail(account_email,'请重置您的密码', 'email/reset_password.html', user=user,token=token)
            pass
        pass
    return render_template('auth/forget_password_request.html',form=form)


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    form = ResetPasswordForm(request.form)
    if request.method =='POST' and form.validate():
        success=User.reset_password(token,form.password1.data)
        if success:
            flash('你的密码已更新，请使用新密码登录')
            return redirect(url_for('web.login'))
        else:
            flash('重置失败，请重新输入邮箱')
            return redirect(url_for('web.forget_password_request'))
    return render_template('auth/forget_password.html')


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    pass
