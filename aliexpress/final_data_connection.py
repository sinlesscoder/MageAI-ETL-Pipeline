from sqlalchemy import create_engine
from getpass import getpass

# Add your credentials
username = 'postgres'
password = getpass("Type in your server password: ")
host = '104.225.217.176'
port = '8362'
database = 'project'

# Dialect together: Example PostgreSQL
dialect = f'postgresql://{username}:{password}@{host}:{port}/{database}'

# Create the engine object
engine = create_engine(dialect)