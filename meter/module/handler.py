from time import sleep

from module.meter import Meter


class Handler(Meter):
    """
    A class representing a handler that publishes meter data to RabbitMQ.

    Args:
        rabbitmq (RabbitMQ): An instance of the RabbitMQ class for publishing messages.

    Methods:
        start: Starts the handler and continuously publishes meter data to RabbitMQ.
    """

    def __init__(self, rabbitmq) -> None:
        """
        Initializes a new instance of the Handler class.

        Args:
            rabbitmq (RabbitMQ): An instance of the RabbitMQ class for publishing messages.
        """
        self.rabbitmq = rabbitmq

    def start(self):
        """
        Starts the handler and continuously publishes meter data to RabbitMQ.
        The handler sleeps for 2 seconds between each publishing.

        Example:
            handler = Handler(rabbitmq_instance)
            handler.start()
        """
        while True:
            sleep(2)
            self.rabbitmq.publish(message={"data": self.generate_value()})