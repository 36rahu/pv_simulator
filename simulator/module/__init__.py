from time import sleep
import logging

from module.config import EnvVariables
from module.gateway.rabbitmq import rabbitMQServer


def main():
    """
    The entry point of the script.

    Configures logging, waits for the RabbitMQ server to start, creates a RabbitMQ server instance,
    and starts consuming messages from the specified queue.

    """
    logging.basicConfig(
        format='%(asctime)s %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO
    )

    # Waiting to RMQ server to start
    sleep(10)

    server = rabbitMQServer(
        queue=EnvVariables.RABBITMQ_QUEUE.get_env(),
        host=EnvVariables.RABBITMQ_HOST.get_env(),
        routing_key=EnvVariables.RABBITMQ_ROUTING_KEY.get_env(),
        username=EnvVariables.RABBITMQ_USERNAME.get_env(),
        password=EnvVariables.RABBITMQ_PASSSWORD.get_env(),
        exchange=EnvVariables.RABBITMQ_EXCHANGE.get_env(),
    )
    server.get_messages()