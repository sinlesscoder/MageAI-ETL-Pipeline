import duckdb
from sqlalchemy import create_engine

# DB cursor
def setup_duckdb_engine(db_name: str):
    # Connection string
    ## // for network URI and /// for local URI
    con = f'duckdb:///{db_name}'

    # Create SQLAlchemy engine
    engine = create_engine(con)

    return engine

def setup_duckdb_db(db_name: str):
    cursor = duckdb.connect(db_name)

    duckdb.sql("CREATE TABLE random AS (SELECT 'Hi')", connection=cursor)

    cursor.close()

