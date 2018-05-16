from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class LocalLoadForm(FlaskForm):
    csv_path = StringField('Path', validators=[DataRequired()])
    submit = SubmitField('Submit')