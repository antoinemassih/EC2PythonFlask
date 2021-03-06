from flask_restful import reqparse, fields, marshal_with, abort, Resource
from models.alert import Alert


class AlertResource(Resource):
    alert_post_args = reqparse.RequestParser()
    alert_post_args.add_argument("symbol", type=str, help="Alert Symbol", required=True)

    resource_fields = {
        'id': fields.Integer,
        'alertMessage': fields.String,
        'alertType': fields.String,
        'bearBull': fields.String,
        'alertValue': fields.Integer,
        'symbol': fields.String,
        'timestamp': fields.DateTime
    }

    @marshal_with(resource_fields)
    def get(self, alert_id):
        result = Alert.query.filter_by(id=alert_id).first()
        if not result:
            abort(404, message="Could not find alert with that id")
        return result
