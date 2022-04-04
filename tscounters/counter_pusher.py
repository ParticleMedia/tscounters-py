import threading
import time



def pusher_thread():
    from . import counter_instances

    while True:
        print("Push counters...")
        for counter_instance in counter_instances:
            print(counter_instance.name)

        time.sleep(1)


def init_counter_pusher():
    t = threading.Thread(target=pusher_thread)
    t.start()
