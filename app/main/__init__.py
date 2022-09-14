from flask import Blueprint

from ..models import Store


main = Blueprint('main', __name__)


@main.route('/')
def index():
    return '<h1>hello main</h1>'