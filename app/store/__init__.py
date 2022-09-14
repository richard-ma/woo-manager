from flask import Blueprint

from ..models import Store


store = Blueprint('store', __name__)


@store.route('/')
def index():
    return '<h1>store index</h1>'
