from functools import reduce

# List of numbers
n = [1, 2, 3, 4, 5, 6]

# Use reduce to apply a function (multiplication) cumulatively to the items in the list
mul = reduce(lambda x, y: x * y, n)

# Print the result of multiplying all numbers in the list
print("Product of all numbers:", mul)
