from flask import render_template, redirect, url_for, abort, flash, request,\
    current_app, make_response
from woocommerce import API as WCAPI
from .. import db
from ..models import Store
from . import main as app


def create_api(id=None):
    store = Store.query.get_or_404(id)

    api = WCAPI(
        url=store.url,
        consumer_key=store.key,
        consumer_secret=store.secret,
        version=store.version
    )

    return api


@app.route('/')
def index():
    wc_api = create_api(2)

    r = wc_api.get("products")
    print(r.status_code)
    print(r.encoding)
    print(r.text)
    print(r.json())

    return render_template('index.html')


# @app.route('/create', methods=['GET', 'POST'])
# def create():
#     form = StoreForm()
#
#     if form.validate_on_submit():
#         store = Store(
#             url=form.url.data,
#             key=form.key.data,
#             secret=form.secret.data,
#             version=form.version.data,
#             active=form.active.data
#         )
#
#         try:
#             db.session.add(store)
#             db.session.commit()
#
#             flash("Your store has been updated.")
#         except Exception as e:
#             flash("Error: Your store hasn't been updated.")
#
#         return redirect(url_for('store.index'))
#
#     return render_template('modify.html', form=form)
#
#
# @app.route('/update/<int:id>', methods=['GET', 'POST'])
# def update(id):
#     store = Store.query.get_or_404(id)
#     form = StoreForm()
#
#     if form.validate_on_submit():
#         store.id = id
#         store.url = form.url.data
#         store.key = form.key.data
#         store.secret = form.secret.data
#         store.version = form.version.data
#         store.active = form.active.data
#
#         try:
#             db.session.commit()
#
#             flash("Your store has been updated.")
#         except Exception as e:
#             flash("Error: Your store hasn't been updated.")
#
#         return redirect(url_for('store.index'))
#
#     form.url.data = store.url
#     form.key.data = store.key
#     form.secret.data = store.secret
#     form.version.data = store.version
#     form.active.data = store.active
#     return render_template('modify.html', form=form)
#
#
# @app.route('/active_store/<int:id>', methods=['GET'])
# def active_store(id):
#     store = Store.query.get_or_404(id)
#     store.active_store()
#
#     try:
#         db.session.commit()
#
#         flash("Your store has been updated.")
#     except Exception as e:
#         flash("Error: Your store hasn't been updated.")
#
#     return redirect(url_for('store.index'))
#
#
# @app.route('/deactive_store/<int:id>', methods=['GET'])
# def deactive_store(id):
#     store = Store.query.get_or_404(id)
#     store.deactive_store()
#
#     try:
#         db.session.commit()
#
#         flash("Your store has been updated.")
#     except Exception as e:
#         flash("Error: Your store hasn't been updated.")
#         raise e
#
#     return redirect(url_for('store.index'))
