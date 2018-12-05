import os
from datetime import datetime

import pytz
from flask import Flask, send_from_directory, request, jsonify, render_template

from .config import Config
from . import views, utils

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


@app.route('/node_modules/<path:filename>')
def node_modules(filename):
    return send_from_directory(Config.NODE_MODULES_DIR, filename)


@app.errorhandler(404)
def not_found_error(error):
    error = {
        'timestamp': datetime.now(tz=pytz.utc).isoformat(),
        'status': 404,
        'error': 'NotFoundError',
        'message': 'Not Found',
        'path': request.path,
    }
    if request.path.startswith('/api'):
        return jsonify(error), 404
    title = 'Error Page 404'
    return render_template('error.html', title=title, **error), 404


# @app.errorhandler(500)
# def internal_error(error):
#     db.session.rollback()
#     return render_template('errors/500.html'), 500


# routes
views.init(app)

# print(app.url_map)
utils.print_routes(app)
