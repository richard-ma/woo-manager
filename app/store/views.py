from flask import render_template, redirect, url_for, abort, flash, request,\
    current_app, make_response
from .. import db
from ..models import Store
from . import store as app
from .forms import StoreForm


@app.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    pagination = Store.query.order_by(Store.url.asc()).paginate(
        page, per_page=current_app.config['STORES_PER_PAGE'],
        error_out=False
    )
    stores = pagination.items

    return render_template('index.html', stores=stores)


@app.route('/modify', methods=['GET', 'POST'])
def modify():
    form = StoreForm()

    if form.validate_on_submit():
        store = Store()
        store.url = form.url.data
        store.key = form.key.data
        store.secret = form.secret.data
        store.version = form.version.data
        store.active = form.active.data

        try:
            db.session.add(store)
            db.session.commit()

            flash("Your store has been updated.")
        except Exception as e:
            flash("Error: Your store hasn't been updated.")

        return redirect(url_for('store.index'))

    return render_template('modify.html', form=form)
