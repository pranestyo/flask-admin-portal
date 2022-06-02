from flask import *


def login():
    return render_template('auth/login.html')
