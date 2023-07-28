## Python Client for Kafka

### Installation

- Via `pip`

```bash
pip install kafka-python
```

### Basic Usage

#### Connecting to a Kafka Producer

```python
from kafka import KafkaProducer

# Authenticate into the Kafka producer
def connect_kafka_producer():
    # Server to connect to Kafka producer
    bootstrap_server = '209.182.236.218:9092'

    # Initiate the producer
    producer = KafkaProducer(bootstrap_servers=[bootstrap_server],
     api_version=(0,10))

    return producer
```

#### Sending a Message in a Topic

```python
# Publish a message
def publish_message(producer, topic_name, key, value):
    # Serialize your keys and values
    key_bytes = bytes(key, encoding='utf-8')
    value_bytes = bytes(value, encoding='utf-8')

    # Producer send a message
    producer.send(topic_name, key=key_bytes, value=value_bytes)

    # Clear the current stream
    producer.flush()

    # Log that the message was sent
    print("Message sent successfully!")
```

#### Testing the Above

```python
# Connecting to Kafka Producer
producer = connect_kafka_producer()

# Publish a message
message = 'This is a test message for the Python client of Apache Kafka.'

# Utilize the publish_message() function
publish_message(producer, 'test', 'sample', message)
```
