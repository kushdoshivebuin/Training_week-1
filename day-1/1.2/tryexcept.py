# Function to perform division with exception handling
def division():
    """
    Prompts the user for two integer inputs and performs division.
    
    Handles the following exceptions:
    - ZeroDivisionError: When division by zero occurs.
    - ValueError: When the input is not an integer.
    - Generic Exception: For any other errors.
    
    The finally block executes regardless of whether an exception occurs.
    """
    try:
        # Take two integer inputs from the user
        a = int(input("Enter value of a: "))
        b = int(input("Enter value of b: "))
        
        # Perform division and display the result
        print(a / b)

    # Handle division by zero
    except ZeroDivisionError:
        print("Division by zero is not possible")

    # Handle invalid input (non-integer)
    except ValueError:
        print("You have given a character as an input")

    # Catch any other exceptions
    except Exception as e:
        print("You have an error:", e)

    # Finally block runs regardless of exceptions
    finally:
        print("This is a default statement")

# Call the division function
division()
