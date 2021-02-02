from flask_potion import Resource, fields
from flask_potion.routes import Route


class trades(db.model):
    __tablename__ = 'trades'
    schema = 'public'
    id = db.Column(db.Integer, primary_key=True)
    trade_symbol = db.Column(db.String(), nullable=False)
    symbol= db.Column(db.String(), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    open_date = db.Column(db.Integer, nullable=False)


class TradesResource(Resource):
    class Meta:
        model = trades

    class Schema:
        message = fields.String()

    @Route.GET
    def whos(self):
        return "hello"
