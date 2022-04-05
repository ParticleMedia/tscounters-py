import json
import requests


class CounterEngine:
    def commit_counter(self, counter):
        raise NotImplemented()


class OpenTSDBCounterEngine(CounterEngine):
    def __init__(self, hostname, port=4242):
        self.hostname = hostname
        self.port = port

    def commit_counter(self, counter):
        metrics = []
        for ts, value, tags in counter.data:
            metrics.append({
                "metric": counter.name,
                "timestamp": int(ts * 1000),
                "value": value,
                "tags": tags or {},
            })

        res = requests.post(
            "http://{}:{}/api/put?details=true".format(self.hostname, self.port),
            data=json.dumps(metrics),
        )
        return res.status_code == 200
