from normalizing_data import normalize_collection

# Get Mongo Collections from both APIs
priceshark_df = normalize_collection('cheapshark_col', 'Database_1')
opencritic_df = normalize_collection('opencritic_col', 'Database_1')


# # Get the name columns
# priceshark_name_cols = [col for col in priceshark_df.columns.tolist() if 'Name' in col]
# opencritic_name_cols = [col for col in opencritic_df.columns.tolist() if 'name' in col]

# print(priceshark_name_cols)
# print(priceshark_df.columns)
# print(opencritic_name_cols)

# Title and Name
print(priceshark_df['title'])
print(opencritic_df['name'])

# Merge dataframes using inner join
game_subset = priceshark_df.merge(opencritic_df, how='inner', left_on='title', right_on='name')

print(game_subset.shape)

print(game_subset)