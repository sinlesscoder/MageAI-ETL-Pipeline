from itertools import combinations

# Example List
example_one = [1,2,3,4]

# Second Example List
example_two = [i for i in range(1, 11)]

# Combinations
results = set(filter(lambda x: x[0] in example_one and x[1] in example_one, combinations(example_two, r=2)))

print(results)



