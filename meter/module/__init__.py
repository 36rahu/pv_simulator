from time import sleep
import logging

from module.config import EnvVariable
from module.gateway.rabbitmq import RabbitMQ
from module.handler import Handler


def main():
    """
    The main function that starts the application.

    It initializes the logging configuration, waits for the RabbitMQ server to start,
    creates an instance of the RabbitMQ class using the environment variables,
    and starts the handler to continuously publish meter data to RabbitMQ.
    """
    logging.basicConfig(
        format='%(asctime)s %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p',
        level=logging.INFO
    )

    # Waiting to RMQ server to start
    sleep(10)

    rabbitMQ_instance = RabbitMQ(
        queue=EnvVariable.RABBITMQ_QUEUE.get_env(),
        host=EnvVariable.RABBITMQ_HOST.get_env(),
        routing_key=EnvVariable.RABBITMQ_ROUTING_KEY.get_env(),
        username=EnvVariable.RABBITMQ_USERNAME.get_env(),
        password=EnvVariable.RABBITMQ_PASSSWORD.get_env(),
        exchange=EnvVariable.RABBITMQ_EXCHANGE.get_env()
    )

    handler = Handler(rabbitMQ_instance)
    handler.start()
