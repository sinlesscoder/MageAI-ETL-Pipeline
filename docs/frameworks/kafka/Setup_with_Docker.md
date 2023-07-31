## Setting Up Kafka with Docker

### Docker Images

#### Kafka with Zookeeper

- Two services: Kafka with 1 broker and Zookeeper server.
- Setup with Docker using two Docker images:
  - [Image 1: zookeeper](https://hub.docker.com/_/zookeeper)
  - [Image 2: ubuntu/kafka](https://hub.docker.com/r/ubuntu/kafka)

#### Kafka with Kraft Protocol

- Single service Kafka server that starts one broker.
- Setup with Docker using the official Docker image from `Bitnami`

  - [Bitnami Kafka Image](https://hub.docker.com/r/bitnami/kafka)

### Steps to Run

#### Kafka with Zookeeper

1. Write a `docker-compose.yml` file that contains the following services:
   - `zookeeper`
   - `kafka`

```yml
# docker-compose.yml
version: '3.1'

services:
  # Get Zookeeper Services (1 Per Kafka Broker)

  # Zookeeper Server 1
  zoo1:
    image: zookeeper
    restart: always
    hostname: zoo1
    ports:
      - 2181:2181
    environment:
      ZOO_MY_ID: 1
      ZOO_SERVERS: server.1=zoo1:2888:3888;2181 server.2=zoo2:2888:3888;2181 server.3=zoo3:2888:3888;2181

  # Zookeeper Server 2
  zoo2:
    image: zookeeper
    restart: always
    hostname: zoo2
    ports:
      - 2182:2181
    environment:
      ZOO_MY_ID: 2
      ZOO_SERVERS: server.1=zoo1:2888:3888;2181 server.2=zoo2:2888:3888;2181 server.3=zoo3:2888:3888;2181

  # Zookeeper Server 3
  zoo3:
    image: zookeeper
    restart: always
    hostname: zoo3
    ports:
      - 2183:2181
    environment:
      ZOO_MY_ID: 3
      ZOO_SERVERS: server.1=zoo1:2888:3888;2181 server.2=zoo2:2888:3888;2181 server.3=zoo3:2888:3888;2181

  # Kafka Server from Ubuntu
  kakfa:
    container_name: kafka_tutorial_karyssa
    image: ubuntu/kafka
    ports:
      - 9092:9092
    environment:
      TZ: UTC
      ZOOKEEPER_HOST: host.docker.internal
```

2. Run the `docker-compose.yml` file.

```bash
docker-compose up -d
```

3. Investigate the `docker logs` of the `zoo1` service and also the `kafka` service.

```bash
# Inspecting Zookeeper Server
docker logs zoo1

# Inspecting Kafka Server
docker logs kafka_tutorial_karyssa
```

4. After successfully verifying that the servers are up and running, you want to enter the container for Kafka.

```bash
docker exec -it kafka_tutorial_karyssa bash
```

5. List out topics in the current Kafka broker server.

```bash
sh kafka-topics.sh --list --zookeeper host.docker.internal:2181
```

#### Kafka with Kraft Protocol

1. Get the `docker-compose.yml` file from the curl command provided by `Bitnami`.

```bash
curl -sSL https://raw.githubusercontent.com/bitnami/containers/main/bitnami/kafka/docker-compose.yml
```

2. Edit the `docker-compose.yml` with your desired configuration including container name, port number, environment variables, etc.

3. Run the `docker-compose.yml` file with `docker-compose up -d` in order to create a new container.

```bash
docker compose up -d
```

4. Investigate the `docker logs` of the existing container to see what exactly is running
   - Kafka Server with the Kraft Protocol
   - Replaces `Zookeeper` through the use of `qorum controllers` that will periodically add snapshots of metadata in a topic to all the provisioned brokers in the Kafka cluster.

- Replace `container_name` with your container name.

```bash
docker logs container_name
```

![](https://p131.p1.n0.cdn.getcloudapp.com/items/L1uvR6Em/198429f4-3899-4d84-8f9f-16ba8cd74868.jpg?v=15b49601145de4af32cd9aafb73729ac)

5. Enter the Docker container that is running the Kafka cluster, Kraft, and broker server

- Replace `container_name` with your container name.

```bash
docker exec -it container_name bash
```

6. Within the container, navigate to the path below:

```bash
cd /opt/bitnami/kafka/bin
```

7. List out if topics are already available

```bash
sh kafka-topics.sh --list --bootstrap-server localhost:9092
```
