from models.modeldb import db


class Alert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    alertMessage = db.Column(db.String(100), nullable=False)
    timeFrame = db.Column(db.String(100), nullable=False)
    symbol = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.TIMESTAMP, nullable=False)
    alertType = db.Column(db.String(100), nullable=False)
    bearBull = db.Column(db.String(100), nullable=False)
    alertValue = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f"Alert(name = {name}, symbol = {symbol})"