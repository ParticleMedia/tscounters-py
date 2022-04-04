__VERSION__ = "0.0.2"

from .counter_pusher import init_counter_pusher


counter_instances = []


def init():
    init_counter_pusher()
