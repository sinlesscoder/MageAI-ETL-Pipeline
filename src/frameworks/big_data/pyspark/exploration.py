from pyspark.sql import SparkSession

# Start a Spark Session
spark = SparkSession.builder.master("local[4]").appName('SparkExploration').getOrCreate()

# Create some dummy data
dummy_data = [
    ('Ali', 23, 'Data'),
    ('Zeehan', 25, 'PSO'),
    ('Sohel', 42, 'PSO'),
    ('Krithika', 25, 'SWE')
]

columns = ['Name', 'Age', 'Track']

# Create Spark DataFrame
df = spark.createDataFrame(data=dummy_data, schema=columns)

# See the data
print(df.show())
