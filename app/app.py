# -*- coding: utf-8 -*-
from flask import Flask, render_template
from query.views import query_app

class HttpsForcedApp(Flask):
    def wsgi_app(self, environ, start_response):
        environ['wsgi.url_scheme'] = 'https'
        return super(HttpsForcedApp, self).wsgi_app(environ, start_response)


# application factory, see: http://flask.pocoo.org/docs/patterns/appfactories/
def _register_blueprints(app):
    app.register_blueprint(query_app)

def create_app():
    #app = Flask(__name__)
    app = HttpsForcedApp(__name__)

    # # import blueprints
    # from accounts.views import accounts_app
    # from pages.views import pages_app

    # register blueprints
    _register_blueprints(app)
    # app.register_blueprint(pages_app)

    return app
