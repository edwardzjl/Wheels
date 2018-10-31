
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class ManufactorForm(FlaskForm):
    manufactor = StringField('Manufactor', validators=[DataRequired()])
    submit = SubmitField('Submit')
