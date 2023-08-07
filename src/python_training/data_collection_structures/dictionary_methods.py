# Setup a key,value pair

new_dict = {
    '1' : 1,
    '2' : 2,
    '3' : 3
}

# Add new key,value pair
new_dict['4'] = 4

print(new_dict)

# Remove a key, value pair
print(new_dict.pop('4'))

print(new_dict)

print(list(new_dict.items()))

ex = (1,2,3)
print(ex)
print(type(ex))

# Find a key based on value
ex_two = {'5', 5}

# Method 1: Use .keys()
updated_dict = {key : new_dict[key] + 1 for key in new_dict.keys()}

print(updated_dict)

# List called results
results = [1,2,3,4,5]

print('----------------')

print(dict(enumerate(results)))

result_dict = {f"{i+1}" : result for i, result in enumerate(results)}

# Complex Dictionary

user_metadata = [{'id': 1,
                  'address': {
                      'street_number' : 1000,
                      'street_name' : 'carleton',
                      'city' : 'Albany',
                      'state' : 'NY',
                      'zip_code': 80129
                  },
                  'name': 'big_bob',
                  'time_spent': 260
                 },
                 
                 {'id': 2,
                  'address': {
                      'street_number' : 1001,
                      'street_name' : 'marleton',
                      'city' : 'Albany',
                      'state' : 'NY',
                      'zip_code': 80129
                  },
                  'name': 'big_bob',
                  'time_spent': 260
                 },

                 {'id': 3,
                  'address': {
                      'street_number' : 1002,
                      'street_name' : 'carleton',
                      'city' : 'Albany',
                      'state' : 'NY',
                      'zip_code': 80129
                  },
                  'name': 'big_bob',
                  'time_spent': 260
                 },

                 {'id': 4,
                  'address': {
                      'street_number' : 1003,
                      'street_name' : 'carleton',
                      'city' : 'Albany',
                      'state' : 'NY',
                      'zip_code': 80129
                  },
                  'name': 'big_bob',
                  'time_spent': 260
                 },
                 ]

# Get the street number
print('first dictionary', user_metadata[0])
print('dictionary inside first dictionary', user_metadata[0]['address'])
print('street number inside of second dictionary which is inside of first dictionary which is inside a list', user_metadata[0]['address']['street_number'])