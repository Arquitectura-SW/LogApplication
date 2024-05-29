import json
from random import randint
import pika
from sys import path
from os import environ
from datetime import datetime, timezone
import django
from uuid import uuid4


#Define the connection parameters to the broker message
rabbit_host = '10.128.0.14'
rabbit_user = 'admin'
rabbit_password = 'admin'
exchange = 'BancoLosAlpes'
topics = ['solicitud']

path.append('LogsApplication/settings.py')
environ.setdefault('DJANGO_SETTINGS_MODULE', 'LogsApplication.settings')
django.setup()

from logs.logic.logic_logs import createLogObject

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
    logId = uuid4()
    creationDate = datetime.now(timezone.utc).isoformat()
    createdLog = datetime.fromisoformat(creationDate)
    print(createdLog)
    createdSol = datetime.fromisoformat(payload['creationDate'])
    print(createdSol)
    diferencia = createdLog - createdSol
    print(diferencia)
    print('Creation Date ' + str(payload['creationDate']) 
          + ' ' + ' Status ' + str(payload['status']) + ' ' + ' Documento Cliente ' + ' ' +  str(payload['user_id']) + ' ' + str(creationDate) + ' ' + " Creacion Log " + ' ' + 
          str((createdLog - createdSol)) + ' ' + " Tiempo de diferencia")
    createLogObject(uid=logId, level='INFO', message=str(payload), created=creationDate, user=int(payload['user_id']), time=str((createdLog - createdSol)))
channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()

