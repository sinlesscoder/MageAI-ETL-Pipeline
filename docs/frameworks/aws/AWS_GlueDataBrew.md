## AWS Glue DataBrew

### Description

- Glue DataBrew is primarily an analytics platform powered by AWS that is very data-centric. This means that you'll be able to assess your data quality, perform transformations with data, and load / export your data into various sources on Amazon or externally.

### Key Features

1. Glue Dataset

- Anytime you set up a DataBrew project, you have to ensure that it is loaded as a specific dataset on the DataBrew platform. This is referred to as a `Glue Dataset`.

  - Supported Formats

    - CSV / TSV
    - Parquet
    - JSON / AVRO
    - RDS Connection
    - JDBC Connection
    - S3 Bucket / Prefix

  - Sampling
    - When rendering your data, Glue DataBrew automatically chooses a smaller sample of your data for viewing within the platform, but operations are done on the entire dataset.
    - Lower the latency when trying to apply operations to your dataset.
    - Manual Sample or Random Sample

2. Data Profile

- Very similar to a pandas-profiler, AWS Glue DataBrew has its own data profiling system. It supports data quality assessment from the perspective of each column individually and also its interactions with other columns.
  - Correlation Analysis
  - Missing Value Analysis
  - Duplicate Value Analysis
  - High-Level Hints
  - Rich Exploratory Data Analysis

3. Data Transformation

- Entire suite of transformations that can be applied in the form of a `Recipe`. A recipe is a set of steps that allows you to go from step 1 to a final step of transformations that your data needs to go through to get to a final condition for proper data quality.

  - Transformations

    - Replacing Missing Values
    - Arithmetic
    - Aggregate Functions (e.g. AVG, COUNT, SUM)
    - Type Casting (e.g. string to integer)

  - Multiple Dataset Operations
    - JOINs
    - UNIONs
    - INTERSECTIONS

4. Job Creation

- After you've designed your profiler or recipe, then you can publish a job which allows you to monitor the progress of your custom data transformations.
  - Functionality
    - Success / Failure Monitoring
    - Step Analysis
