from itertools import combinations
from fuzzywuzzy import fuzz, process

# Example List
example_one = ['apple', 'banana', 'cherry', 'grape']
example_two = ['apples', 'bananas', 'cherries', 'grapes', 'oranges']

# Combinations
results = set(filter(lambda x: x[0] in example_one and x[1] in example_one, 
                     combinations(example_two, r=2)))

#print(results)

fuzzy_threshold = 50 

# Generate combinations
combinations_list = list(combinations(example_two, r=2))

# Filter combinations using fuzzy matching
filtered_combinations = list(filter(lambda x: all(fuzz.ratio(x[0], example) 
                        >= fuzzy_threshold or fuzz.ratio(x[1], example) 
                        >= fuzzy_threshold for example in example_one), 
                        combinations_list))

# Print the filtered combinations
for combo in filtered_combinations:
    print(combo)


# for combo in combinations_list:
#     matching_details = [(example, fuzz.ratio(combo[0], example), fuzz.ratio(combo[1], example)) for example in example_one]
#     print(combo, matching_details)
#     if any(fuzzy >= fuzzy_threshold for _, fuzzy1, fuzzy2 in matching_details):
#         filtered_combinations.append(combo)

# # Print the filtered combinations
# for combo in filtered_combinations:
#     print(combo)