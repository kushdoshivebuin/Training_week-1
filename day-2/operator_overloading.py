class Complex:
    """
    A class to represent a complex number with real and imaginary parts.

    Attributes:
    real (float): The real part of the complex number.
    img (float): The imaginary part of the complex number.
    """
    
    def __init__(self, real, img):
        """
        Initialize a Complex number with the real and imaginary parts.

        Parameters:
        real (float): The real part of the complex number.
        img (float): The imaginary part of the complex number.
        """
        self.real = real
        self.img = img

    def showNumber(self):
        """
        Display the complex number in the format "real + imaginary * i".

        Returns:
        str: The string representation of the complex number.
        """
        return f"The number is: {self.real} + {self.img}j"

    def __add__(self, num1):
        """
        Add two complex numbers by adding their real and imaginary parts separately.

        Parameters:
        num1 (Complex): Another Complex number to add to the current Complex number.

        Returns:
        Complex: A new Complex number that is the sum of the current and passed complex numbers.
        """
        newReal = self.real + num1.real  # Add real parts
        newImg = self.img + num1.img  # Add imaginary parts
        return Complex(newReal, newImg)

# Create two Complex number instances
C1 = Complex(4, 5)
C2 = Complex(5, 4)

# Add the two Complex numbers
ans = C1 + C2

# Display the result of the addition
print(ans.showNumber())  # Output the sum of the two complex numbers
