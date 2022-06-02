from flask import *


def homepage():
    return render_template('main/index.html')
