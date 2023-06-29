import os

from enum import Enum


class EnvVariable(str, Enum):
    """
    Class handle environment variables related to this service.

    Enum Values:
        RABBITMQ_USERNAME: The environment variable for RabbitMQ username.
        RABBITMQ_PASSWORD: The environment variable for RabbitMQ password.
        RABBITMQ_HOST: The environment variable for RabbitMQ host.
        RABBITMQ_QUEUE: The environment variable for RabbitMQ queue.
        RABBITMQ_ROUTING_KEY: The environment variable for RabbitMQ routing key.
        RABBITMQ_EXCHANGE: The environment variable for RabbitMQ exchange.

    Methods:
        get_env: Retrieves the value of the environment variable.

    """
    RABBITMQ_USERNAME = 'RABBITMQ_USERNAME'
    RABBITMQ_PASSSWORD = 'RABBITMQ_PASSSWORD'
    RABBITMQ_HOST = 'RABBITMQ_HOST'
    RABBITMQ_QUEUE = 'RABBITMQ_QUEUE'
    RABBITMQ_ROUTING_KEY = 'RABBITMQ_ROUTING_KEY'
    RABBITMQ_EXCHANGE = 'RABBITMQ_EXCHANGE'

    def get_env(self, variable=None):
        """
        Retrieves the value of the environment variable.

        Args:
            variable (Optional[str]): A default value to return if the environment variable is not found.

        Returns:
            str: The value of the environment variable, or the provided default value if not found.

        Example:
            username = EnvVariable.RABBITMQ_USERNAME.get_env()
        """
        return os.environ.get(self, variable)
