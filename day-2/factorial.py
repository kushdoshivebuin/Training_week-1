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
       
        if num == 0:
            return 1
        
        return self.calc_fact(num - 1) * num

n = int(input("Enter the number for factorial: "))

f1 = Factorial()
print(f1.calc_fact(n)) 
