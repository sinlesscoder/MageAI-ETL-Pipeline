from pymongo import MongoClient

uri='104.225.217.176:8363'

client = MongoClient(uri)

db = client['aliexpress_items']

# See all the collections
results = db.list_collection_names()

# print(type(results))
# <<<<<<< HEAD
# <<<<<<< HEAD
# print(db.list_collection_names())
# =======
# =======
# >>>>>>> 74ec4a4940f1854c89c33aaea5f6b95abc5f6682
# print(results)

# Dictionary for All Collections
col_dict = {col: list(db[col].find())[0] for col in results}

print(col_dict.keys())

for key in col_dict.keys():
    print(key)
    print(col_dict[key])
    print("-----------------------")
# <<<<<<< HEAD
# >>>>>>> 4113f666234475208418a930fdad35c647c356a3
# =======
# >>>>>>> 74ec4a4940f1854c89c33aaea5f6b95abc5f6682
