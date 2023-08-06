from functools import reduce
# Add things to lists

"""
Populate the numbers: 1 through 100 into a list
"""

# Use range to get the numbers 1 through 100
nums = []

for num in range(1, 101):
    nums.append(num)

print(nums)

# Alternative Technique: List Comprehension
nums = [num for num in range(1, 101)]

print(nums)

# Map and List Casting
## Can wrap into tuple or set
nums = list(map(lambda x: x+1, range(1, 101)))

print(nums)

# Sum of Squares from 1 through 1000
sum_squares = reduce(lambda a,b: a+b, map(lambda x: x**2, range(1, 1001)))
print(sum_squares)

# Flatten the following list:
list_of_lists = [
    [1,2,3,4,5,6,7],
    [8,9,10,11,12,13,14],
    [15,16,17,18,19,20,21]
]

list_one = [1,2,3]
list_two = [4,5,6]
list_three = list_one + list_two
print(list_one + list_two)
print(list_three)

flattened_list = reduce(lambda a,b: a+b, list_of_lists)

print(flattened_list)

# Removing numbers from a list

## Remove num
def remove_num(nums: list, num: int):
    # If the number is in the list, remove it, else do nothing
    if num in nums:
        # Use the .remove() method
        nums.remove(num)
    
    return nums

example_list = [1,2,3,4, 5]
example_num = 3

new_list = remove_num(example_list, example_num)

print("---------------------------")
print(new_list)

# # Remove everything
# example_list.clear()

# print(example_list)

# Find where a number is in the list
x = 4

print(new_list.index(x))