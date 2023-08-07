## Kafka Consumer CLI Fundamentals

### Retrieving Messages

- Kafka uses the `kafka-console-consumer.sh` file in order to perform operations at the consumer level to be viewed in the console.

- To view all the messages within a topic, you can use the following command:

- Replace `my_topic` with your topic name.

```bash
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic my_topic --from-beginning
```
