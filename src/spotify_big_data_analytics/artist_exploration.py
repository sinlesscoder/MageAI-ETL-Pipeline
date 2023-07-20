from pyspark.sql import SparkSession
from os import getcwd

"""
Description:

This file aims to use PySpark to assist us in analyzing a larger dataset
related to music analytics with Spotify data.

"""

# Data Path
data_path = getcwd() + "/SpotGenTrack/Data Sources"

# Setup Spark Context
spark = SparkSession.builder.master('local[4]').appName('chanR_Spotify_Analytics').getOrCreate()

# Read a CSV file
## Select a header 

df = spark.read.option("header", True).option("inferSchema", True).csv(f"{data_path}/spotify_artists.csv")

# First 4 rows
print(df.show(4))

# Print the Schema
print(df.printSchema())

# Select genres and id
print(df.select('genres', 'id'))
