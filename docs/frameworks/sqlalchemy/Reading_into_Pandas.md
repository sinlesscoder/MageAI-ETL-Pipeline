## Reading into Pandas

- Assuming that you have a [connection object setup](./Intro.md), you can connect a connection object into pandas to get SQL tables as DataFrame objects.

- Within pandas, there are three `read` methods that are related to SQL:

1. `read_sql()`
2. `read_sql_table()`
3. `read_sql_query()`

### Example: Reading the table `aliexpress_results`

```python
import pandas as pd

# Assuming you already have a connection object from SQLAlchemy

df = pd.read_sql_table('aliexpress_results', con=con)

# View the first 5 rows
df.head()
```

### Example: Reading a SQL Query on `aliexpress_results`

```python
import pandas as pd
from sqlalchemy import text

# Write a SQL query as a string and convert it into SQL Executable Text which is what the text() method does

# Write your query
query = "SELECT * FROM aliexpress_results LIMIT 30"

# Convert to SQL executable query
query = text(query)

# Read into pandas
df = pd.read_sql_query(query, con=con)
```
