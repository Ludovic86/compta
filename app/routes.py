import os
from app import app
from app import dal
from flask import render_template
from app.forms import ImportForm
from werkzeug.utils import secure_filename

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/import', methods=['GET', 'POST'])
def importPage():
    form = ImportForm()
    if form.validate_on_submit():
        f = form.dataFile.data
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['IMPORT_BUFFER'], filename))
        filepath = app.config['IMPORT_BUFFER'] + '/' + filename
        dal.write_debits(filepath)
        os.remove(filepath)
        return render_template('index.html')
    return render_template('import.html', form=form)

@app.route('/data')
def data():
    debits = dal.get_all_debits()
    return render_template('data.html', debits=debits)