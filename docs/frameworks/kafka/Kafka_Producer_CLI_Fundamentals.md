## Working with Producers in Kafka from the Command Line

- Kafka uses bash scripting in order to execute actions directly on the broker.
- For entities such as `topics` or `messages`, there would be an equivalent bash script that would allow an end user to add additional arguments to specify operations.

### Topic Operations within a Kafka Broker

- A bootstrap server is essentially the server of the Kafka broker. When you start a Kafka cluster with Docker, you are provisioned with only one broker since you're running Docker on a single server (e.g. node).

- You will have only one bootstrap server that is available to you to list out / create topics.

#### Listing Out Topics

- Utilizes the `kafka-topics.sh` script.

- Listing topics is provided with the action flag `--list`

- The default Broker server (e.g. bootstrap server) is running on localhost:9092 as defined by the `docker-compose.yml` file.
  - Specify the bootstrap server with the following flag `--bootstrap-server`
- The reason for the above flag is because we're using Apache Kafka with the `Kraft` protocol as opposed to Zookeeper.
  - If we were using Zookeeper, we would replace the `--bootstrap-server` with `--zookeeper` and the URL of where Zookeeper is running.

```bash
sh kafka-topics.sh --list --bootstrap-server localhost:9092
```

- Creating topics is provided with the action flag `--create`

  - Properties
    - `--replication-factor` : integer value representing how many copies of the topic you want
    - `--partitions` : integer value representing number of partitions in the topic
    - `--topic` : string value (written without quotes) which represents the name of the topic

- Example without properties (Kraft)
  - Replace `topic_name` with your desired topic name.

```bash
sh kafka-topics.sh --create --topic topic_name --bootstrap-server localhost:9092
```

- Example without properties (Zookeeper)
  - Replace `topic_name` with your desired topic name.

```bash
sh kafka-topics.sh --create --topic topic_name --zookeeper host.docker.internal:2181
```

- Example with properties (Kraft)
  - Replace `topic_name` with your desired topic name.

```bash
sh kafka-topics.sh --create --topic topic_name --replication-factor 1 --partitions 1 --bootstrap-server localhost:9092
```

- Example with properties (Zookeeper)
  - Replace `topic_name` with your desired topic name.

```bash
sh kafka-topics.sh --create --topic topic_name --replication-factor 1 --partitions 1 --zookeeper host.docker.internal:2181
```

---

> For the rest of this documentation, it is assumed that we're using Kafka with Kraft.

---

### Messaging with Producers in Kafka

- To work with messages in Kafka, we have to use a producer.
- Within the scripts that are provided within the `bitnami` image, we are going to leverage the following script:
  - `kafka-console-producer.sh`

#### Sending a message in an existing topic

- Get the list of brokers based on the bootstrap server using the property:

  - `--broker-list`

- Replace `topic_name` with your topic name.

```bash
sh kafka-console-producer.sh --broker-list localhost:9092 --topic topic_name
```

#### Finding the logs

- Within the `/opt/kafka/logs` directory, there should be a subdirectory that corresponds to your topic name. You'll find all relevant logs in there.

### Resources

- [Kafka Apache Foundation Documentation](https://kafka.apache.org/quickstart)
