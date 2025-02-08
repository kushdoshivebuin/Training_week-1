class Account:
    """
    A class to represent a bank account.

    Attributes:
    balance (int): The balance of the account (default is 0).
    account_no (int): The unique account number.
    """

    # Initialize the account with a unique account number
    def __init__(self, acc):
        """
        Initialize an Account object with an account number.

        Parameters:
        acc (int): The account number to associate with the account.
        """
        self.account_no = acc
        self.balance = 0  # Default balance is 0

    # Method to deposit money into the account
    def credit(self):
        """
        Deposit a specified amount into the account.
        """
        deposit = int(input("Enter the amount to be deposited: "))
        self.balance += deposit  # Add deposit to balance
        print("The balance after depositing is:", self.balance)

    # Method to withdraw money from the account
    def debit(self):
        """
        Withdraw a specified amount from the account.
        """
        withdraw = int(input("Enter the amount to be withdrawn: "))
        if withdraw <= self.balance:
            self.balance -= withdraw  # Deduct withdrawal from balance
            print("The balance after withdrawal is:", self.balance)
        else:
            print("Insufficient balance.")

    # Method to view the final balance of the account
    def final_balance(self):
        """
        Display the current balance of the account.
        """
        print("The final balance for account number", self.account_no, "is:", self.balance)

# Create an Account object with a specific account number
acc1 = Account(123456)

# Display menu options to the user
print("What would you like to do?")
print("1. Deposit")
print("2. Withdraw")
print("3. Balance View")
print("4. Exit")

# Loop to allow the user to perform multiple operations
ans = "Y"
while ans == "Y" or ans == "y":
    # Get user choice for operation
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        acc1.credit()  # Deposit money
    elif choice == 2:
        acc1.debit()  # Withdraw money
    elif choice == 3:
        acc1.final_balance()  # View balance
    elif choice == 4:
        break  # Exit the loop if the user chooses to quit
    else:
        print("Invalid choice. Please enter a valid option.")

    # Ask user if they want to continue
    ans = input("Do you want to continue? (Y/N): ")
