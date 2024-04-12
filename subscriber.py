import json
from random import randint
import pika
from sys import path
from os import environ
import datetime
import django

#Define the connection parameters to the broker message
rabbit_host = '10.128.0.53'
rabbit_user = 'admin'
rabbit_password = 'admin'
exchange = 'BancoLosAlpes'
topics = ['solicitud']

path.append('LogsApplication/settings.py')
environ.setdefault('DJANGO_SETTINGS_MODULE', 'LogsApplication.settings')
django.setup()

from logs.models import Log
from logs.logic.logic_logs import createLog, createLogObject

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=rabbit_host, credentials=pika.PlainCredentials(rabbit_user, rabbit_password)))
channel = connection.channel()

channel.exchange_declare(exchange=exchange, exchange_type='topic')

result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

for topic in topics:
    channel.queue_bind(
        exchange=exchange, queue=queue_name, routing_key=topic)

print('> Waiting logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    payload = json.loads(body.decode('utf8').replace("'", '"'))
    print('Creation Date ' + str(payload['creationDate']) 
          + 'Status ' + str(payload['status']) + 'Documento Cliente ' + str(payload['user_id']))
    creationDate = datetime.now().isoformat()
    createdLog = datetime.fromisoformat(creationDate)
    createdSol = datetime.fromisoformat(payload['creationDate'])
    diferecia = (createdLog - createdSol)
    createLogObject(level='INFO', message= str(payload), created= creationDate, user = int(payload['user_id'], time = str(diferecia.total_segundos())))
channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()

