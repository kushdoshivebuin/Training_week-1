# List of numbers
n = [1, 2, 3, 4, 5, 6]

# Use filter to select even numbers (those that satisfy the condition x % 2 == 0)
even = filter(lambda x: x % 2 == 0, n)

# Convert the filter object to a list and print the even numbers
print("Even numbers:", list(even))
