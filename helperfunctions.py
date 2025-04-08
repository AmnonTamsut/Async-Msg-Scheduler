import json
import threading
import time

from redis_client import ma_redis_client

SCHEDULED_MESSAGES = 'scheduled messages'


def print_message_at_time():


    while True:
        now = time.time()
        messages = ma_redis_client.zrangebyscore(SCHEDULED_MESSAGES, 0, now)
        for message in messages:
            message_data = message.decode("utf-8")
            message_data = json.loads(message_data)
            message_text = message_data['message']
            print(message_text)
            ma_redis_client.zrem(SCHEDULED_MESSAGES, message)


def start_message_scheduler():
    # would be better with sempahore or some kind of thread pool to handle load
    # due to time constraints and wanting to test multiple scenarios, kept it at 1 thread.
    thread = threading.Thread(target=print_message_at_time)
    thread.start()
