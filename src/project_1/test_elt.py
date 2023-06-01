from load_mongodb import db_load

# Select a search term
search_term = 'iphone'

print(db_load(search_term))