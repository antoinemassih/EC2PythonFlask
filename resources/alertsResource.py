from flask_restful import reqparse, fields, marshal_with, abort, Resource

from models.alert import Alert
from models.modeldb import db
from datetime import datetime
import json


class AlertListResource(Resource):

    alert_post_args = reqparse.RequestParser()
    alert_post_args.add_argument("symbol", type=str, help="Alert Symbol", required=False)
    alert_post_args.add_argument("alertMessage", type=str, help="Alert Symbol", required=False)
    alert_post_args.add_argument("alertValue", type=str, help="Alert Symbol", required=False)
    alert_post_args.add_argument("timeFrame", type=str, help="Alert Symbol", required=False)
    alert_post_args.add_argument("alertType", type=str, help="Alert Symbol", required=False)
    alert_post_args.add_argument("bearBull", type=str, help="Alert Symbol", required=False)

    resource_fields = {
        'id': fields.Integer,
        'alertMessage': fields.String,
        'alertType': fields.String,
        'bearBull': fields.String,
        'alertValue': fields.Integer,
        'symbol': fields.String,
        'timeFrame': fields.String,
        'timestamp': fields.DateTime
    }

    @marshal_with(resource_fields)
    def get(self):
        result = Alert.query.all()
        if not result:
            abort(404, message="Could not find alert with that id")
        return result

    @marshal_with(resource_fields)
    def post(self):
        jsonString = self.alert_post_args.parse_args()
        alertDict = {}
        #jsonString = json.loads(args['text'])
        #alertDict = json.load(jsonString)
        print(jsonString['alertType'])
        alertitem = Alert(alertMessage=jsonString['alertMessage'],alertValue=jsonString['alertValue'], symbol=jsonString['symbol'], timestamp=datetime.now(),timeFrame=jsonString['timeFrame'],alertType=jsonString['alertType'],bearBull=jsonString['bearBull'])
        db.session.add(alertitem)
        db.session.commit()
        return alertitem, 201
