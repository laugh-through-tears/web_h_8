import json
from datetime import datetime

import pika

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='Web8 exchange', exchange_type='direct')
channel.queue_declare(queue='web_8_queue', durable=True)
channel.queue_bind(exchange='Web_8 exchange', queue='web_8_queue')


def create_tasks(nums: int):
    for i in range(nums):
        message = {
            'id': i,
            'payload': f"Date: {datetime.now().isoformat()}"
        }

        channel.basic_publish(exchange='Web16 exchange', routing_key='web_8_queue', body=json.dumps(message).encode())

    connection.close()


if __name__ == '__main__':
    create_tasks(100)
