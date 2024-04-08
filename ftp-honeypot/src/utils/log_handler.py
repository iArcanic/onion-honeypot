import threading
import json
import requests

from multiprocessing import Process
from config import LOGSTASH_HOST, LOGSTASH_PORT


def send_log_to_logstash(data):
    def send_logs():
        try:
            response = requests.post(f'http://{LOGSTASH_HOST}:{LOGSTASH_PORT}', json=data)
            response.raise_for_status()  # Raise an exception for non-200 status codes
            print('Log sent to Logstash successfully!')
        except requests.exceptions.RequestException as e:
            print(f'Error sending log to Logstash: {e}')

    send_process = Process(target=send_logs)
    send_process.start()

