import collections
import time


counter_instances = []


class Counter:
    def __init__(self, name, aggregator=None):
        self.name = name
        self.data = collections.defaultdict(list)
        self.aggregator = aggregator

        counter_instances.append(self)

    def get_tags_str(self, tags):
        return ",".join(["{}:{}".format(k, v) for k, v in sorted(tags.items())])

    def set(self, value, tags=None):
        raise NotImplemented()

    def on_commit(self):
        raise NotImplemented()


class SimpleCounter(Counter):
    def set(self, value, tags=None):
        tags = tags or {}

        key = self.get_tags_str(tags)
        self.data[key].append((time.time(), value, tags))

    def on_commit(self):
        self.data.clear()
