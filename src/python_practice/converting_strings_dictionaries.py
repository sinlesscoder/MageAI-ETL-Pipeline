from ast import literal_eval

fruits = {'fruit_1': 'apple', 'fruit_2': 'banana'}
fruit_str = str(fruits)
fruits_v2 = literal_eval(fruit_str)

print(fruits)
print(fruit_str)
print(fruits_v2)