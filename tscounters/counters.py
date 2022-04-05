import collections
import time


counter_instances = []


class Counter:
    def __init__(self, name):
        self.name = name
        self.data = []

        counter_instances.append(self)

    def get_tags_str(self, tags):
        return ",".join(["{}:{}".format(k, v) for k, v in sorted(tags.values())])

    def set(self, value, tags=None):
        raise NotImplemented()

    def on_commit(self):
        raise NotImplemented()


class SimpleCounter(Counter):
    def set(self, value, tags=None):
        self.data.append((time.time(), value, tags))

    def on_commit(self):
        self.data.clear()
