# PV Simulator

Generates simulated photovoltaic (PV) power production and household consumption values and writes the results (in Kilowatts kW) to the disk.

## Stack
- Docker
- RabbitMQ
- Pika
- Python 3.8

## How to use

### Using Docker Compose
 - To create and run the image use the following command, Make sure that docker is already installed in your system.

```bash
docker-compose up --build
```

 - Copy storage file from docker container to the local system. Make sure that your docker containers are up and running.

```bash
docker cp simulator:/simulator/output.csv ./
```

## About the system

The configuration will create a cluster with 3 containers:

- Meter container
- Simulator container
- RabbitMQ container

The Meter container will continuously generates a random consumption value between 0 to 9.0 KW and publishes meter data to RabbitMQ. 

The Simulator container will read message from the RabbitMQ and parses the message. Then calculates the PV values using the PV Simulator. 

The simlilation values are looks like this,

```cmd
+------+-------+
| Hour | BasePV|
+------+-------+
|  4   |  0.1  |
|  5   | 0.15  |
|  6   |  0.2  |
|  7   |  0.3  |
|  8   |  0.5  |
|  9   |  1.0  |
| 10   |  2.0  |
| 11   |  2.5  |
| 12   |  3.0  |
| 13   |  3.5  |
| 14   |  3.5  |
| 15   |  3.2  |
| 16   |  3.0  |
| 17   |  2.5  |
| 18   |  2.0  |
| 19   |  1.0  |
| 20   |  0.2  |
| 21   |  0.1  |
+------+-------+
```

#### Calcultion of PV values

If hour less than 14:00
```bash
    Final PV value = BasePV + (0.01 * Minutes)
```
If hour greater than 14:00
```bash
    Final PV value = BasePV - (0.01 * Minutes)
```

Examples:
```bash
11:30 => 2.5 + (0.01 * 30) => 2.8
18:13 => 2.0 - (0.01 * 13) => 1.87
```

#### Calcultion of Sum up value
```bash
Sum up value = PV value - meter consumption value
```

Created sum up value with PV values and meter consumption values. Finally all values (timestamp, PV values, meter consumption value, sum up value) stored into a CSV file.

#### Format for CSV file
```bash
timestamp, pv_value, meter_consumption_value, sumup_value
```

RabbitMQ container is where messages flow through RabbitMQ and applications, stored inside a queue. A web browser access to the Dashboard is also provided for RabbitMQ message management and monitoring which can be accessed at `http://localhost:15672`.


## Project Structure
Below is a project structure created:

```cmd
.
├── README.md
├── docker-compose.yml
├── meter
│   ├── Dockerfile
│   ├── module
│   │   ├── __init__.py
│   │   ├── __main__.py
│   │   ├── config.py
│   │   ├── gateway
│   │   │   ├── __init__.py
│   │   │   └── rabbitmq.py
│   │   ├── handler.py
│   │   └── meter.py
│   ├── requirements.txt
│   └── tests
│       ├── __init__.py
│       └── test_meter.py
└── simulator
    ├── Dockerfile
    ├── module
    │   ├── __init__.py
    │   ├── __main__.py
    │   ├── config.py
    │   ├── gateway
    │   │   ├── __init__.py
    │   │   └── rabbitmq.py
    │   ├── handler.py
    │   ├── simulator.py
    │   └── storage.py
    ├── requirements.txt
    └── tests
        ├── __init__.py
        └── test_simulator.py
```

## Help and Resources
You can read more about the tools documentation:

- [Docker](https://docs.docker.com/get-started/overview/)
- [RabbitMQ](https://www.rabbitmq.com)
- [Pika](https://pika.readthedocs.io/en/stable/#)