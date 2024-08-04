import sys
import pika

message = " ".join(sys.argv[1:]) or "Hello World!"

credentials = pika.PlainCredentials("myuser", "mypassword")
parameters = pika.ConnectionParameters("localhost", 5672, "/", credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue="task_queue", durable=True)

channel.basic_publish(
    exchange="",
    routing_key="task_queue",
    body=message,
    properties=pika.BasicProperties(delivery_mode=pika.DeliveryMode.Persistent),
)
print(" [x] Sent 'Hello World!'")

connection.close()
