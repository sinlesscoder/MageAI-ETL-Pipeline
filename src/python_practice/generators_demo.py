# Squaring the numbers 1 through 100

sq_nums = []

for i in range(1, 101):
    value = i**2
    sq_nums.append(value)

print(sq_nums)

# Generator
def sq_nums(start_ind: int, end_ind: int):
    for i in range(start_ind, end_ind + 1):
        value = i ** 2

        # Yield
        yield value

examples_sq = sq_nums(1, 100)

print(examples_sq)

# First number from generator
val = next(examples_sq)
print(val)
val = next(examples_sq)
print(val)
val = next(examples_sq)
print(val)
val = next(examples_sq)
print(val)
val = next(examples_sq)
print(val)

# First 20 numbers

nums_to_receive = [next(examples_sq) for i in range(20)]

print(nums_to_receive)

# Getting all the numbers at once
print(list(examples_sq))