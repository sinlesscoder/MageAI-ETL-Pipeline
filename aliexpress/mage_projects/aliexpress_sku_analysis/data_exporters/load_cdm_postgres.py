from sqlalchemy import create_engine

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

# Helper Function: Connecting to Postgres
def postgres_connection():
    # Credentials for the connection
    username = 'postgres'
    password = 'pathrise2023!'
    host = uri
    port = 8362
    db_name = 'project'

    # Establishing an Authentication URI
    dialect = f'postgresql://{username}:{password}@{host}:{port}/{db_name}'

    # Setup an engine
    engine = create_engine(dialect)

    return engine




@data_exporter
def export_data(data, *args, **kwargs):
    """
    Exports data to some source.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Output (optional):
        Optionally return any object and it'll be logged and
        displayed when inspecting the block run.
    """
    # Specify your data exporting logic here
    
    # Connection object
    cursor = postgres_connection().connect()
    
    # Loading as a SQL table in Postgres server
    data.to_sql('aliexpress_results', con=cursor, index=False, if_exists='replace')

