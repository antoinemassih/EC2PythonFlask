from flask_potion import Resource, fields
from flask_potion.routes import Route, ItemRoute

from flaskapp import HookAlert


class TvHooksResource(Resource):
    class Meta:
        model = HookAlert

    @Route.GET
    def base(self):
        return "base API is working"

    @ItemRoute.GET("/title")
    def title(self):
        return "this is another one"

    @title.POST
    def posttitle(self, title, value: fields.String) -> fields.String():
        self.manager.update(title, {"title": value})
        return value
