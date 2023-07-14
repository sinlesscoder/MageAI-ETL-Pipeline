import numpy as np
import pandas as pd
from boto3 import resource
from os import getcwd

# S3 Client using resource()
s3_client = resource('s3', aws_access_key_id='AKIAYL6E4F3TDFYDICNR', aws_secret_access_key='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')

# Get a Bucket
bucket = s3_client.Bucket('covid-19-deaths-vaccinations')

# Data Path
data_path = getcwd() + "/data/aws/s3"

# Generate random data
random_matrix = np.random.randint(0, 100, size=(10000, 20))
df = pd.DataFrame(random_matrix)
df.columns = [f'col_{i+1}' for i in range(df.shape[1])]
df.to_csv(f"{data_path}/random_integers.csv", index=False)

# Upload the data to S3 Bucket
bucket.upload_file(f'{data_path}/random_integers.csv', Key='uploaded_files/random_integers.csv')
