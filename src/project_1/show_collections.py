from pymongo import MongoClient

uri='104.225.217.176:8363'

client = MongoClient(uri)

db = client['aliexpress_items']

# See all the collections
results = db.list_collection_names()

print(type(results))
<<<<<<< HEAD
print(db.list_collection_names())
=======
print(results)

# Dictionary for All Collections
col_dict = {col: list(db[col].find())[0] for col in results}

print(col_dict.keys())

for key in col_dict.keys():
    print(key)
    print(col_dict[key])
    print("-----------------------")
>>>>>>> 4113f666234475208418a930fdad35c647c356a3
