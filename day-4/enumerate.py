data = [1, 2, -4, -3]

for idx, num in enumerate(data):  
    """
    Replaces negative numbers in the data list with 0.

    Parameters:
    - idx (int): Index of the current element in the list.
    - num (int): The value at the current index.

    The loop checks if the value is less than 0, and if so, it sets that 
    element in the list to 0.
    """
    if num < 0:  # If the number is negative
        data[idx] = 0  # Replace negative value with 0

print(data)
