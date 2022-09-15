from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import Length, DataRequired, InputRequired


class StoreForm(FlaskForm):
    url = StringField('Store Url', validators=[DataRequired(), Length(0, 128)])
    key = StringField('Consumer Key', validators=[DataRequired(), Length(0, 128)])
    secret = StringField('Consumer Secret', validators=[DataRequired(), Length(0, 128)])
    version = StringField('API Version', default='wc/v3', validators=[DataRequired(), Length(0, 128)])
    active = BooleanField('Active?', default=True)
    submit = SubmitField('Submit')
