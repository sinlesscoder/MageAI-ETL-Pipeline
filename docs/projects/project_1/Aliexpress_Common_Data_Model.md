## Common Data Model

- The `aliexpress` API gives you results for a specific item search. Each item search is based on a specific page.

![](https://p131.p1.n0.cdn.getcloudapp.com/items/lluXZyrm/a462d178-1cf2-4d74-940e-fb4ecdff412f.jpg?v=776122c2e8854efc71025ca119eba0e1)

- From the image above, harmonizing the data to become a single table requires the development of a common data model.

### Requirements

- A single table
- Support all search items
- Support all pages

### Assumptions

- API is idempotent
- Assumes that all calls to the API will follow the same scheme.

### Modeling Strategy

- Take all the columns that come from the original JSON response for each page.

- Convert each page's response into a DataFrame and keep track of the item search and page number by introducing them as separate columns in the same DataFrame.

- Loop through all your search items and pass the finalized DataFrames in a list.

- Apply a pandas operation to group up the DataFrames together into a single DataFrame since they'll have the same columns.

- Export the finalized table to PostgreSQL.

### MageAI Blueprint

- Pipeline Name: `aliexpress_cdm`

#### Blocks

- Data Loader

  - `retrieve_mongo_collection_names`
    - Get the names of the search terms that contain results.
    - Return a list of those names

- Data Transformer

  - `common_data_model`
    - Retrieve the actual data from the Mongo collection based on input search terms.
    - Create a single DataFrame that consolidates the normalized results of each term's page results.

- Data Exporter
  - `load_cdm_postgres`
    - Load the DataFrame from previous block into a PostgreSQL table.
