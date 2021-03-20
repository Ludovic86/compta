from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import FileField, SubmitField

class ImportForm(FlaskForm):
    dataFile = FileField('Data File', validators=[
        FileRequired(), 
        FileAllowed(['csv'], 'csv only !')
        ])
    submit = SubmitField('Import')