from flask import render_template
from tutorial import app


@app.route('/')
@app.route('/index')
def index():
    users = [
        {'id': 1, 'username': 'vova'},
        {'id': 2, 'username': 'vadim'},
        {'id': 3, 'username': 'dasha'},
    ]
    return render_template('index.html', title='Index', users=users)
