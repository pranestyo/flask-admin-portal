from flask import *
from modules.base.views import view

# flask setup
base_view = Blueprint('base_view', __name__,)


@base_view.route('/', methods=['GET'])
def home():
    return view.homepage()
