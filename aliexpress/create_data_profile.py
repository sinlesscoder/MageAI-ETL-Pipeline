import pandas as pd
from ydata_profiling import ProfileReport
from final_data_connection import engine
from os import getcwd

# Connection Object
con = engine.connect()

# Read the aliexpress_results table
df = pd.read_sql_table('aliexpress_results', con=con)

# View first 5 rows
print(df.head())

# Creating a ProfileReport object
report = ProfileReport(df, dark_mode=True)

# Report path
report_path = getcwd() + "/aliexpress"

# Save as HTML
report.to_file(f'{report_path}/aliexpress_results_summary.html')