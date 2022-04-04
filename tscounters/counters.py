class Counter:
    def __init__(self, name):
        self.name = name
        self.value = 0

        from . import counter_instances
        counter_instances.append(self)

    def on_commit(self):
        pass


class SimpleCounter(Counter):
    def set(value):
        self.value = value


class RateCounter(Counter):
    def set(value):
        self.value += value

    def on_commit(self):
        self.value = 0
