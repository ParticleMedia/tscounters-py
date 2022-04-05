__VERSION__ = "0.0.2"

from .counter_pusher import init_counter_pusher, add_counter_engine


def init():
    init_counter_pusher()
