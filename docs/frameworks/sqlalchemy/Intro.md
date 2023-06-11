## Reading from a Table

### Description

- `sqlalchemy` is a Python module that acts as a bridge between a SQL server and Python. It uses a method called `create_engine` in order to set up a specific SQL server connection. In order to interpret a specific server, it uses a specialized dialect for a server.

For `postgresql`, `sqlalchemy` uses the `psycopg2` dialect with allows us to write a uniform resource identifier (URI) in the following way:

```
postgresql://user:password@server:port/database
```

### Installation

- via `pip`

```bash
pip install sqlalchemy
```

- It's preferred to get the stable version. You can find the exact stable version at this [link](https://www.sqlalchemy.org/)

- See the GIF below to get the exact version.

![Insert a GIF later]()

- To be compatible with `PostgreSQL`, you have to install the dialect.

```bash
pip install psycopg2-binary
```

### Basic Usage

- It uses the `create_engine()` method in order to set up a dialect for connecting to a SQL server.

```python
from sqlalchemy import create_engine
from getpass import getpass

# Add your credentials
username = ''
password = getpass("Type in your server password: ")
host = ''
port = ''
database = ''

# Dialect together: Example PostgreSQL
dialect = f'postgresql://{username}:{password}@{host}:{port}/{database}'

# Create the engine object
engine = create_engine(dialect)
```

- After you setup the `engine`, you want to create the final connection object.

```python
# Preferred variable names: con or cursor

con = engine.connect()
```
