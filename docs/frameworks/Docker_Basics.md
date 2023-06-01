## Docker Basics

### Images

- Imagine that you have a computer that is built specifically to run your application.

- Linux: `CentOS`

#### Downloading Images

- Retrieving Images

  - Replace [image name] with actual image.

```bash
docker pull [image name]
```

#### Example

```bash
docker pull postgres
```

#### Building Images

```bash
docker build . -t my_app:latest
```

### Containers

- Specific instance of a Docker image.

#### Example: Setting Up Postgres on 8200

- Postgres usually runs on `5432` which is the default port in the image.

- We would tell our container to forward the content in `5432` directly to our desired port `8200` on our machine.

```bash
docker run -p host_port:image_port image_name:tag
```

$$ \downarrow $$

```bash
docker run -p 8200:5432 postgres:latest
```

#### Accessing Containers

- Initiate a `bash` session within a container just like you do with a server.

- Replace `container_name` with actual container.

```bash
docker exec -it container_name
```

#### Properties

- `-p`: Port mapping between host and image.
- `-d`: Detached mode: Creating a background process
- `-i` : Interactive mode
- `-t` : Time to Live (TTL)
- `-e` : Environment Variable
- `-v` : Volume is a mounted drive between the container and the host machine.
- `--name` : A unique name that refers to your container
- `--restart` : Policy in the event that your server crashes, the container will automatically restart
  - `on-failure`
  - `always`

#### Monitoring Containers

- Gives you a list of all the containers that are currently up and running.

```bash
docker ps
```
