from flask_restful import Resource
from flask import jsonify
from webapp.db import RedisClient


class ProxyApi(Resource):
    def __init__(self):
        self.db = RedisClient()

    def get(self, count=None):
        if count:
            proxies = self.db.random(count=count)
            return jsonify(proxies=proxies, count=count)
        return jsonify(count=1, proxy=self.db.random())
