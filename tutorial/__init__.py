import os
from datetime import datetime

import pytz
from flask import Flask, render_template, request, jsonify

from config import Config

app = Flask(__name__, root_path=Config.RESOURCES_DIR)

app.config.from_object(Config)

# @app.before_request
# def before_request():
#     g.user = current_user
#     locale = get_locale()
#     if not locale:
#         g.locale = app.config['DEFAULT_LOCALE']
#     else:
#         g.locale = locale


@app.context_processor
def inject_dict_for_all_templates():
    app_vars = {
        'name': os.environ.get('APP_NAME', 'App'),
        'locale': os.environ.get('APP_LOCALE', 'en'),
        'env': os.environ.get('FLASK_ENV', 'production'),
        'tutorial': os.environ.get('FLASK_APP', 'tutorial'),
    }
    return dict(app=app_vars)


# routes
from tutorial import erorrs
from tutorial import routes
