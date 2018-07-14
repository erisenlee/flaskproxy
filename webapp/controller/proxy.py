from flask import render_template, Blueprint
from os import path
from webapp.db import RedisClient

proxy_blueprint = Blueprint('proxy', __name__,
                            template_folder=path.join(path.pardir, 'templates', 'proxy'),
                            url_prefix='/proxy')


@proxy_blueprint.route('/')
def index():
    redis=RedisClient()
    proxies=redis.random(count=10)

    return render_template('index.html',proxies=proxies)