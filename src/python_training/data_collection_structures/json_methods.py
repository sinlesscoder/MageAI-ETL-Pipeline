import json

# Save data into a .json file
ex_dict = {'1': 1, '2': 2, '3' : {'4': 4, '5': 5}}

## Context Manager
with open('local_file.json', 'w') as f:
    # JSON dump method
    json.dump(ex_dict, f)


# Loading data from a .json file

## Context Manager
with open('local_file.json', "r") as f:
    # JSON load method
    result = json.load(f)

print(result)