import logging

import pika

from module.handler import handler


class rabbitMQServer():
    """
    A class for interacting with RabbitMQ.

    Args:
        queue (str): The name of the queue to bind and publish messages.
        host (str): The host address of the RabbitMQ server.
        routing_key (str): The routing key for message routing.
        username (str): The username for authentication.
        password (str): The password for authentication.
        exchange (str): The exchange to declare (optional).

    Methods:
        start_server: Starts the RabbitMQ server by creating a channel, declaring an exchange, and binding the queue.
        create_channel: Creates a new channel and establishes a connection to the RabbitMQ server.
        create_exchange: Declares the exchange with specified options.
        create_bind: Binds the queue to the exchange with the routing key.
        publish: Publishes a message to the RabbitMQ server.

    """

    def __init__(self, queue, host, routing_key, username, password, exchange=''):
        """
        Initializes a new instance of the RabbitMQ class.

        Args:
            queue (str): The name of the queue to bind and publish messages.
            host (str): The host address of the RabbitMQ server.
            routing_key (str): The routing key for message routing.
            username (str): The username for authentication.
            password (str): The password for authentication.
            exchange (str): The exchange to declare (optional).
        """
        self._queue = queue
        self._host = host
        self._routing_key = routing_key
        self._exchange = exchange
        self._username = username
        self._password = password
        self.start_server()

    def start_server(self):
        """
        Starts the RabbitMQ server by creating a channel, declaring an exchange, and binding the queue.
        """
        self.create_channel()
        self.create_exchange()
        self.create_bind()
        logging.info("Channel created...")

    def create_channel(self):
        """
        Creates a new channel and establishes a connection to the RabbitMQ server.
        """
        credentials = pika.PlainCredentials(username=self._username, password=self._password)
        parameters = pika.ConnectionParameters(self._host, credentials=credentials)
        self._connection = pika.BlockingConnection(parameters)
        self._channel = self._connection.channel()

    def create_exchange(self):
        """
        Declares the exchange with specified options.
        """
        self._channel.exchange_declare(
            exchange=self._exchange,
            exchange_type='direct',
            passive=False,
            durable=True,
            auto_delete=False
        )
        self._channel.queue_declare(queue=self._queue, durable=False)

    def create_bind(self):
        """
        Binds the queue to the exchange with the routing key.
        """
        self._channel.queue_bind(
            queue=self._queue,
            exchange=self._exchange,
            routing_key=self._routing_key
        )
        self._channel.basic_qos(prefetch_count=1)

    def get_messages(self):
        """
        Starts consuming messages from the queue.
        """
        try:
            logging.info("Starting the server...")
            self._channel.basic_consume(
                queue=self._queue,
                on_message_callback=handler,
                auto_ack=True
            )
            self._channel.start_consuming()
        except Exception as e:
            logging.debug(f'Exception: {e}')
