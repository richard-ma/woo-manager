from flask import render_template, redirect, url_for, abort, flash, request,\
    current_app, make_response
from ..models import Store
from . import store
from .forms import StoreForm


@store.route('/', methods=['GET', 'POST'])
def index():
    form = StoreForm()
    return render_template('index.html', form=form)
