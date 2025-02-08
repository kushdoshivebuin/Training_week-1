# List of numbers
n = [1, 2, 3, 4, 5, 6]

# Use map to apply the square operation to each number in the list
sqr = map(lambda x: x**2, n)

# Convert the map object to a list and print the squared numbers
print("Squared numbers:", list(sqr))
