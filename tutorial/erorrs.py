from datetime import datetime

import pytz
from flask import request, jsonify, render_template

from tutorial import app


@app.errorhandler(404)
def not_found(error):
    error = {
        'timestamp': datetime.now(tz=pytz.utc).isoformat(),
        'status': 404,
        'error': 'NotFoundError',
        'message': 'Not Found',
        'path': request.path,
    }
    if request.path.startswith('/api'):
        return jsonify(error), 404
    # error['timestamp'] = datetime.now()
    return render_template('error.html', title='Error Page', **error), 404
