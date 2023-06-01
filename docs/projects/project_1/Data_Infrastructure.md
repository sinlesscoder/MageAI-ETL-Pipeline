## Data Infrastructure: Project 1

### PostgreSQL

- `host`: `104.225.217.176`
- `port` : `8362`
- `username` : `postgres`
- `password` : `pathrise2023!`
- `container` : `ca8d2c7d8be1d46ee2afd1abb456e96b5eb9131346192fc6b36909fc9f2e7b50`
- `container name` : `ali_project_1_postgres`

#### Databases

- `postgres`
- `json_data`
- `project`

#### Create with Docker

```bash
docker run --name ali_project_1_postgres \
        -e "POSTGRES_PASSWORD=pathrise2023!" \
        -p 8362:5432 \
        -itd \
        postgres:latest
```

### MongoDB

- `port`: `8363`

- `URI` : `mongodb://104.225.217.176:8363`

- `Container ID`: `879f4d6153880216a00961c441664fd8c2cce8e8604ce28f4fe3907713e0c141`

- `Container Name` : `ali_project_1_mongo`

#### Create with Docker

```bash
docker run --name ali_project_1_mongo \
        -p 8363:27017 \
        -itd \
        mongo:latest
```

#### Accessing the Container

1.

```bash
docker exec -it ali_project_1_mongo bash
```

2. Use Mongo Shell

```bash
mongosh
```

3. Exit the Shell

```bash
quit
```

4. Exit the container

```bash
exit
```
