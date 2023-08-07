## Intro to DuckDB Engine

### Description

- `duckdb` is a new transaction-processing database that exists as a file in-memory. It's actually faster than the majority of relational databases in existence including PostgreSQL and Microsoft SQL.

### Installation

- `duckdb` can be installed using `pip`

```bash
pip install duckdb
```

- You can also access `duckdb` even faster by using the `duckdb_engine` which is compatible with `sqlalchemy`.

```bash
pip install duckdb_engine
```

### Basic Usage

```python
import duckdb
import duckdb_engine
from sqlalchemy import create_engine

# Setup a connection object
connection = duckdb.connect('example.db')

#
```
