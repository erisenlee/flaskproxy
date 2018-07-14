from webapp.extention import rest_api
from flask import Flask, redirect, url_for
from webapp.controller.rest import ProxyApi
from webapp.controller.proxy import proxy_blueprint


def create_app(object_name):
    app = Flask(__name__)
    app.config.from_object(object_name)
    rest_api.add_resource(ProxyApi, '/api/proxy', '/api/proxy/<int:count>', endpoint='api')
    rest_api.init_app(app)

    app.register_blueprint(proxy_blueprint)

    @app.route('/')
    def index():
        return redirect(url_for('proxy.index'))

    return app
