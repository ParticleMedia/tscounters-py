__VERSION__ = "0.0.2"

from .counter_pusher import init_counter_pusher, add_counter_engine


def init(commit_interval=1):
    init_counter_pusher(commit_interval=commit_interval)
