from app import db

class Debit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, index=True)
    amount = db.Column(db.Integer, index=True)

    