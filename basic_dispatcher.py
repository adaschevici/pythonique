import sys
import pika

message = " ".join(sys.argv[1:]) or "Hello World!"

credentials = pika.PlainCredentials("myuser", "mypassword")
parameters = pika.ConnectionParameters("localhost", 5672, "/", credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue="hello")

channel.basic_publish(exchange="", routing_key="hello", body=message)
print(" [x] Sent 'Hello World!'")

connection.close()
