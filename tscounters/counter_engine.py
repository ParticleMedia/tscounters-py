import json
import logging
import requests
import time


class CounterEngine:
    def commit_counter(self, counter):
        raise NotImplemented()


class OpenTSDBCounterEngine(CounterEngine):
    def __init__(self, hostname, port=4242):
        self.hostname = hostname
        self.port = port

    def commit_metrics(self, metrics):
        if not metrics:
            return True

        res = requests.post(
            "http://{}:{}/api/put?details=true".format(self.hostname, self.port),
            data=json.dumps(metrics),
        )
        return res.status_code == 200
