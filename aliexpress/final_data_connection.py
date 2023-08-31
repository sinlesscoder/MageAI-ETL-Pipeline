from json_read import json_reader
from sqlalchemy import create_engine
from getpass import getpass

# Add your credentials
username = 'postgres'
password = getpass("Type in your server password: ")
host = json_reader('HOST')
port = json_reader('PORT')
database = 'project'

# Dialect together: Example PostgreSQL
dialect = f'postgresql://{username}:{password}@{host}:{port}/{database}'

# Create the engine object
engine = create_engine(dialect)