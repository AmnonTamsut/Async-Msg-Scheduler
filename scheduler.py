import time
from threading import Thread

def start_scheduler():
    def scheduler():
        while True:
            time.sleep(1)

    thread = Thread(target=scheduler)
    thread.start()
