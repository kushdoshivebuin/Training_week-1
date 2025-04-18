class Circle:
    """
    A class to represent a circle.

    Attributes:
    radius (float): The radius of the circle.
    """
    
    def __init__(self, radius):
        """
        Initialize the Circle object with a specified radius and calculate its area and perimeter.
        
        Parameters:
        radius (float): The radius of the circle.
        """
        self.radius = radius 
        self.calcarea() 
        self.calcperi()  

    def calcarea(self):
        """
        Calculate and print the area of the circle using the formula: π * radius^2
        """
        area = 3.14 * self.radius * self.radius  
        print("The area of the circle is:", area)

    def calcperi(self):
        """
        Calculate and print the perimeter (circumference) of the circle using the formula: 2 * π * radius
        """
        perimeter = 2 * 3.14 * self.radius 
        print("The perimeter (circumference) of the circle is:", perimeter)


C1 = Circle(5)
