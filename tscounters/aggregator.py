class Aggregator:
    def aggregate(self, values):
        raise NotImplemented()


class SumAggregator:
    def aggregate(self, values):
        return sum(values)


class AvgAggregator:
    def aggregate(self, values):
        if not values:
            return 0
        else:
            return sum(values) / len(values)
