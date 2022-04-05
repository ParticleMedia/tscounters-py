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

    def commit_counter(self, counter):
        metrics = []
        for tag_str, tag_data in counter.data.items():
            if counter.aggregator is None:
                for ts, value, tags in tag_data:
                    metrics.append({
                        "metric": counter.name,
                        "timestamp": int(ts * 1000),
                        "value": value,
                        "tags": tags,
                    })
            else:
                agg_value = counter.aggregator.aggregate([
                    value for _, value, tags in tag_data
                ])

                metrics.append({
                    "metric": counter.name,
                    "timestamp": int(time.time() * 1000),
                    "value": agg_value,
                    "tags": tag_data[0][2],
                })

        res = requests.post(
            "http://{}:{}/api/put?details=true".format(self.hostname, self.port),
            data=json.dumps(metrics),
        )
        return res.status_code == 200
