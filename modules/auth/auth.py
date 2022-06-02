from flask import *
from modules.auth.views import auth

# flask setup
auth_view = Blueprint('auth_view', __name__,)


@auth_view.route('/login', methods=['GET'])
def login():
    return auth.login()
