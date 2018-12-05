from flask import render_template, send_from_directory, flash, redirect, url_for

from forms import LoginForm
from tutorial import app, config


@app.route('/node_modules/<path:path>')
def send_node_modules(path):
    return send_from_directory(config.Config.NODE_MODULES_DIR, path)


@app.route('/')
def index():
    users = [
        {'id': 1, 'username': 'vova'},
        {'id': 2, 'username': 'vadim'},
        {'id': 3, 'username': 'dasha'},
    ]
    return render_template('index.html', title='Index', users=users)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
