# Importing external package dependency:
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, FileField, SelectField, SubmitField
from wtforms import ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, Length


# Form to manually upload new dataset:
class DatasetUploadForm(FlaskForm):
    new_dataset = FileField(validators=[DataRequired()])
    submit = SubmitField("Upload")
