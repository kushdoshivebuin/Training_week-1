# Custom exception for handling numbers outside the specified range
class RangeError(Exception):
    """
    Exception raised when a number is not between 5 and 9.
    """
    pass

# Try block to get user input and handle exceptions
try:
    # Ask the user to input a number
    a = int(input("Enter a number between 5 and 9: "))

    # Check if the input number is outside the range [5, 9]
    if a < 5 or a > 9:
        raise RangeError  # Raise RangeError if the number is out of range

# Exception handling for RangeError (number out of range)
except RangeError:
    print("The given number is not in the range")

# Exception handling for invalid input (non-integer)
except ValueError:
    print("The given input is not a valid number")

# Else block executes if no exception occurs
else:
    print("Your number is", a)
