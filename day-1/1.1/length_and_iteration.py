# Function to calculate and print the length of a list
def length(lst):
    """
    Prints the length of the given list.

    Parameters:
    lst (list): The list whose length is to be calculated.

    Example:
    length([1, 2, 3]) will print 3.
    """
    print(len(lst))

# List of cities
cities = ["Surat", "Ahmedabad", "Valsad"]

# Function to print each element of a list
def printelements(lst):
    """
    Prints each element of the list on a new line.

    Parameters:
    lst (list): The list whose elements are to be printed.
    """
    for i in lst:
        print(i)

# Calling the function to print elements of the cities list
printelements(cities)

# Uncomment to print the length of the cities list
# length(cities)
