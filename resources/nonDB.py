from flask_potion import Resource, fields
from flask_potion.routes import Route


class NoDBResource(Resource):
    class Meta:
        name = 'say'

    class Schema:
        message = fields.String()

    @Route.GET
    def whos(self):
        return "hello"

    @Route.GET
    def now(self):
        return "this is another one"
