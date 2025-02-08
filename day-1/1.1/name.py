# Function to ask for user's name and age
def ask_name():
    """
    Prompts the user to input their name and age.

    Sets global variables `name` and `age` based on user input.
    """
    global name, age
    # Get the user's name as a string
    name = str(input("What is your name? "))
    # Get the user's age as an integer
    age = int(input("What is your age? "))

# Function to print the user's details
def print_details():
    """
    Calls the ask_name function to get the user's details
    and prints their name and age.
    """
    # Ask the user for their name and age
    ask_name()
    
    # Print the user's name and age
    print("Your name is", name)
    print("Your age is", age)

# Call print_details to prompt the user and display their information
print_details()
