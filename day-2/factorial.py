class Factorial:
    """
    A class to calculate the factorial of a number using recursion.

    Methods:
    calc_fact(num): Calculates the factorial of a given number 'num'.
    """

    def calc_fact(self, num):
        """
        Calculate the factorial of a given number 'num' recursively.

        Parameters:
        num (int): The number to calculate the factorial of.

        Returns:
        int: The factorial of the number.
        """
        result = 1
        # Base case: Factorial of 0 is 1
        if num == 0:
            return 1
        
        # Recursive case: Multiply current number by the factorial of (num-1)
        return self.calc_fact(num - 1) * num

# Input number for which the factorial is to be calculated
n = int(input("Enter the number for factorial: "))

# Create an instance of the Factorial class and compute the factorial
f1 = Factorial()
print(f1.calc_fact(n))  # Output the factorial of the number
