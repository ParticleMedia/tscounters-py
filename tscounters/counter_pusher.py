import threading
import time
import logging

from .counters import counter_instances


counter_engines = []


def pusher_thread():
    while True:
        if counter_instances:
            logging.info("Committing {} counters...".format(len(counter_instances)))

            for counter_engine in counter_engines:
                for counter_instance in counter_instances:
                    counter_engine.commit_counter(counter_instance)
                    counter_instance.on_commit()

        time.sleep(1)


def init_counter_pusher():
    t = threading.Thread(target=pusher_thread)
    t.start()


def add_counter_engine(counter_engine):
    counter_engines.append(counter_engine)
