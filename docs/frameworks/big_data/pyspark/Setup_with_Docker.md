## Setting Up Apache Spark Using Docker

1. Get the Docker image for `pyspark-notebook` from `jupyter`.

   - [Docker Hub Link](https://hub.docker.com/r/jupyter/pyspark-notebook/tags?page=1)

2. Run a `docker pull` on the image you retrieved inside a Command Prompt or Terminal.

- Replace `tag-name` with the `tag` you chose.
  - Default is `latest`

```bash
docker pull jupyter/pyspark-notebook:tag-name
```

3. Choose between running with `docker run` or using `docker-compose.yml`

#### 1. Docker Run

- Replace the `name` with your desired container name.
- Replace the `host` with your desired port number.
- Replace the `tag-name` with your installed tag-name.

```bash
docker run --name name -p host:8888 -itd --restart on-failure jupyter/pyspark-notebook:tag-name
```

#### 2. docker-compose.yml

- Replace the `host` with your desired port number.
- Replace the `tag-name` with your installed tag-name.

```yaml
version: '3.3'

services:
  # Service 1
  pyspark-notebook-ali:
    container_name: pyspark-notebook-ali
    image: jupyter/pyspark-notebook:tag-name
    ports:
      - 'host:8888'
    restart: on-failure
```
