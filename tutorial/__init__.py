import os
from datetime import datetime

import pytz
from flask import Flask, render_template, request, jsonify

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
RESOURCES_DIR = os.path.join(BASE_DIR, 'resources')

app = Flask(__name__, root_path=RESOURCES_DIR)


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

if __name__ == '__main__':
    app.run()
