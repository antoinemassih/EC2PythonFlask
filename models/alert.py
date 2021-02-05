from models.modeldb import db


class Alert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    symbol = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Alert(name = {name}, symbol = {symbol}, timestamp = {timestamp})"