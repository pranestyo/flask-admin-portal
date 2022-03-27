#!/usr/bin/env python3
import os
from datetime import timedelta
import logging as lg

from flask import *

from core import config

from modules.base.base import base_view

# flask setup
app = Flask(__name__)
app.config['SECRET_KEY'] = config.SECRET_KEY

# logging
handler = lg.FileHandler(config.PATH_LOG)
logger = lg.getLogger('werkzeug')
logger.addHandler(handler)
app.logger.addHandler(handler)
app.logger.setLevel(lg.DEBUG)


# register routes from urls
app.register_blueprint(base_view)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=60781)
