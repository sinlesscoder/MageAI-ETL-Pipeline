from pyspark.sql import SparkSession
from client_authorization import client
from extract_artist_data import retrieve_artist_data

artist_link = "https://open.spotify.com/artist/70KxgbZNsd9xOttXW67mh3?si=_rccoTQfTlek0zJyyju06g"

print(retrieve_artist_data(artist_link, client))

# Setup a Spark Session
session = SparkSession.builder.master("spark://104.225.218.162:7077").appName("Spark Remote Test").getOrCreate()