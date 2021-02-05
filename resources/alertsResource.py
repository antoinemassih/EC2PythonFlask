from flask_restful import reqparse, fields, marshal_with, abort, Resource

from models.alert import Alert
from models.modeldb import db


class AlertListResource(Resource):

    alert_post_args = reqparse.RequestParser()
    alert_post_args.add_argument("name", type=str, help="Alert Name", required=True)
    alert_post_args.add_argument("symbol", type=str, help="Alert Symbol", required=True)

    resource_fields = {
        'id': fields.Integer,
        'name': fields.String,
        'symbol': fields.String,
        'timestamp': fields.Integer
    }

    @marshal_with(resource_fields)
    def get(self):
        result = Alert.query.all()
        if not result:
            abort(404, message="Could not find alert with that id")
        return result

    @marshal_with(resource_fields)
    def post(self):
        args = self.alert_post_args.parse_args()

        alertitem = Alert(name=args['name'], symbol='AAPL', timestamp=2)
        db.session.add(alertitem)
        db.session.commit()
        return alertitem, 201
