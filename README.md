# Portfolio Project: AliExpress Data Extraction and ETL Pipeline

## Project Overview

This portfolio project focuses on extracting data from AliExpress using their API, transforming and loading it into a PostgreSQL database through an ETL pipeline. The project demonstrates the process of collecting product information from AliExpress, storing it in a MongoDB collection, and subsequently migrating it to PostgreSQL for further analysis.

## Project Structure

The project is structured as follows:

- `data_extraction.py`: Python script responsible for interacting with the AliExpress API and pulling product data.
- `data_transformation.py`: This script focuses on transforming the extracted data into a suitable format for storage and future analysis.
- `mongo_storage.py`: Contains code to establish a connection with MongoDB and store the transformed data.
- `etl_pipeline.py`: Script that coordinates the ETL process using MageAI, orchestrating the flow of data from extraction to loading.
- `postgresql_import.py`: Handles the migration of data from MongoDB to PostgreSQL.
- `requirements.txt`: Lists all the required dependencies for the project.

## Getting Started

To replicate and run this project locally, follow these steps:

1. Clone this repository: `git clone https://github.com/sinlesscoder/aliexpress-etl-project.git`
2. Type in the following command in a terminal
```bash 
cd aliexpress
```
3. Install the required dependencies: `pip install -r requirements.txt`
4. Within a terminal, type the following command: 

```bash 
mage start .
```
## Future Enhancements

This portfolio project serves as a foundation for more advanced features and improvements. Some potential enhancements include:

- Creating a web-based dashboard to visualize the extracted and transformed data.

Thank you for checking out my AliExpress Data Extraction and ETL Pipeline project! Your feedback is highly appreciated.
