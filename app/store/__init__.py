from flask import Blueprint

store = Blueprint('store', __name__, template_folder='templates', static_folder='static')

from .views import *
