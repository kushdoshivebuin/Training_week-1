import random

# Generate a random float number between 0 and 1
print("Random float between 0 and 1:", random.random())

# Generate a random integer between 2 and 3 (both 2 and 3 are inclusive)
print("Random integer between 2 and 3:", random.randint(2, 3))

# Generate a random integer between 2 and 4 (range 2 <= n < 4, 4 is not included)
print("Random integer between 2 and 4 (excluding 4):", random.randrange(2, 4))
