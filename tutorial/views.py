from flask import Flask, render_template, flash, redirect, url_for

from .forms import LoginForm


def init(app: Flask):
    @app.route('/')
    def index():
        users = [
            {'id': 1, 'username': 'vova'},
            {'id': 2, 'username': 'vadim'},
            {'id': 3, 'username': 'dasha'},
        ]
        return render_template('index.html', users=users)

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            flash('Login requested for user {}, remember_me={}'.format(
                form.username.data, form.remember_me.data))
            return redirect(url_for('index'))
        return render_template('login.html', title='Login', form=form)
