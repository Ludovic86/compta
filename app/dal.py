from app import db
from app.models import Debit
import csv
import datetime

def write_debits(filepath):
    with open(filepath, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            i = 0
            for row in spamreader:
                if (i > 0):
                    if (row[2] != ''):
                        datearray = row[1].split('/')
                        dateobject = datetime.datetime(
                            int(datearray[2]), 
                            int(datearray[1].lstrip('0')), 
                            int(datearray[0].lstrip('0')))
                        d = Debit(date=dateobject, amount=float(row[2]), label=row[4])
                        db.session.add(d)
                i = i + 1
    db.session.commit()

def get_all_debits():
    return Debit.query.all()
                    