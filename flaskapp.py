from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with

from models.alert import Alert
from models.modeldb import db
from resources.alertResource import AlertResource
from resources.alertsResource import AlertListResource

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Monkeyhero69@trendchart.cu0jwgiytj6k.us-east-1.rds.amazonaws.com:5432/postgres'
app.config['SQLALCHEMY_ENABLE_POOL_PRE_PING'] = True
db.init_app(app)


api.add_resource(AlertListResource, "/alerts/")
api.add_resource(AlertResource, "/alert/<int:alert_id>")


@app.route('/')
def hello():
    return 'I made a pipeline ammendment!'


if __name__ == "__main__":
    app.run(debug=True)
