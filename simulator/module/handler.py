import json
import logging

from module.simulator import PVSimulator
from module.storage import Storage

simulator = PVSimulator()
storage = Storage()


def handler(channel, method, properties, body):
    """
    Handles the consumed RabbitMQ message.

    Parses the message, calculates the PV value using the PVSimulator instance, performs calculations using
    the meter value from the message, and writes the results to the storage.

    Args:
        channel: The RabbitMQ channel.
        method: The RabbitMQ method.
        properties: The RabbitMQ properties.
        body (bytes): The message body in bytes.

    """
    try:
        logging.info(f'Consumed message {body.decode()} from queue')
        data = json.loads(body.decode())
        pv_value, timestamp = simulator.pv_value_and_ts()
        meter_value = data.get('data', {}).get('consumption')
        sum_up_pv_and_meter_value = round(pv_value - meter_value, 4)
        storage.write_file([timestamp, pv_value, meter_value, sum_up_pv_and_meter_value])
        logging.info(f'Values, pv value: {pv_value}, ts: {timestamp}, meter value: {meter_value}, sum up value: {sum_up_pv_and_meter_value}')
    except Exception as error:
        logging.error(f"handler failed error: {str(error)}")
        logging.exception(error)
