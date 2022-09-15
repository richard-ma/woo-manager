from flask import render_template, redirect, url_for, abort, flash, request,\
    current_app, make_response
from .. import db
from ..models import Store
from . import store as app
from .forms import StoreForm


@app.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    pagination = Store.query.order_by(Store.id.desc()).paginate(
        page, per_page=current_app.config['STORES_PER_PAGE'],
        error_out=False
    )
    stores = pagination.items

    return render_template('index.html', stores=stores, pagination=pagination)


@app.route('/create', methods=['GET', 'POST'])
def create():
    form = StoreForm()

    if form.validate_on_submit():
        store = Store(
            url=form.url.data,
            key=form.key.data,
            secret=form.secret.data,
            version=form.version.data,
            active=form.active.data
        )

        try:
            db.session.add(store)
            db.session.commit()

            flash("Your store has been updated.")
        except Exception as e:
            flash("Error: Your store hasn't been updated.")

        return redirect(url_for('store.index'))

    return render_template('modify.html', form=form)


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    store = Store.query.get_or_404(id)
    form = StoreForm()

    if form.validate_on_submit():
        store.id = id
        store.url = form.url.data
        store.key = form.key.data
        store.secret = form.secret.data
        store.version = form.version.data
        store.active = form.active.data

        try:
            db.session.commit()

            flash("Your store has been updated.")
        except Exception as e:
            flash("Error: Your store hasn't been updated.")

        return redirect(url_for('store.index'))

    form.url.data = store.url
    form.key.data = store.key
    form.secret.data = store.secret
    form.version.data = store.version
    form.active.data = store.active
    return render_template('modify.html', form=form)


@app.route('/active_store/<int:id>', methods=['GET'])
def active_store(id):
    store = Store.query.get_or_404(id)
    store.active_store()

    try:
        db.session.commit()

        flash("Your store has been updated.")
    except Exception as e:
        flash("Error: Your store hasn't been updated.")

    return redirect(url_for('store.index'))


@app.route('/deactive_store/<int:id>', methods=['GET'])
def deactive_store(id):
    store = Store.query.get_or_404(id)
    store.deactive_store()

    try:
        db.session.commit()

        flash("Your store has been updated.")
    except Exception as e:
        flash("Error: Your store hasn't been updated.")
        raise e

    return redirect(url_for('store.index'))
