import redis
from webapp.config import HOST, PASSWORD, PORT, KEY,MIN_SCORE,MAX_SCORE
from random import choice


class RedisClient:
    def __init__(self):
        self.db = redis.StrictRedis(host=HOST, port=PORT, password=PASSWORD)

    def is_exists(self, proxy):
        return True if self.db.zscore(KEY, proxy) else False

    @property
    def count(self):
        return self.db.zcard(KEY)

    @property
    def is_empty(self):
        return True if self.count == 0 else False

    def remove(self, proxy):
        if self.is_exists(proxy):
            self.db.zrem(KEY, proxy)

    def random(self,count=None):
        if not self.is_empty:
            if count:
                if count<=self.count:
                    proxies = self.db.zrangebyscore(KEY, MIN_SCORE, MAX_SCORE, start=0, num=count)
                    for proxy in proxies:
                        self.remove(proxy)
                    return [proxy.decode() for proxy in proxies]
                else:
                    return 'proxy is less than specified number.'
            proxies = self.db.zrangebyscore(KEY, MIN_SCORE, MAX_SCORE, start=0, num=5)
            random = choice(proxies)
            self.remove(random)
            return random.decode()
