data = (3, 5, 10, 2, -5)

# The sorted() function returns a new sorted list without modifying the original data.
sorted_data = sorted(data)
print(sorted_data)  

sorted_data = sorted(data, reverse=True)  # Descending Order
print(sorted_data)  

data = [{"name": "Max", "age": 6},
        {"name": "Lisa", "age": 20},
        {"name": "Ben", "age": 9}]

# Sorting the list of dictionaries based on the 'age' key using a lambda function as the key argument
# The lambda function extracts the 'age' value from each dictionary to use it as the sorting criterion.
sorted_data = sorted(data, key=lambda x: x["age"])

print(sorted_data)
