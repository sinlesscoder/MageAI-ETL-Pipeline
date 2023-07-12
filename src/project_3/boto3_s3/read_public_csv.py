import pandas as pd

df = pd.read_csv("https://covid-19-deaths-vaccinations.s3.amazonaws.com/uploaded_files/random_integers.csv")

print(df.shape)