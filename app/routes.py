from app import app
from flask import render_template
from app.forms import ImportForm
import csv

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/import', methods=['GET', 'POST'])
def importPage():
    form = ImportForm()
    if form.validate_on_submit():
        f = form.dataFile.data
        with open(f.filename, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                print(', '.join(row))
    return render_template('import.html', form=form)