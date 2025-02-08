class Employee:
    """
    A class to represent an employee.

    Attributes:
    role (str): The role of the employee.
    dept (str): The department in which the employee works.
    sal (float): The salary of the employee.
    """

    def __init__(self, role, dept, sal):
        """
        Initialize an Employee object with role, department, and salary.

        Parameters:
        role (str): The role of the employee.
        dept (str): The department where the employee works.
        sal (float): The salary of the employee.
        """
        self.role = role
        self.dept = dept
        self.sal = sal

    def showDetails(self):
        """
        Display the details of the employee, including role, department, and salary.
        """
        print("Role:", self.role)
        print("Department:", self.dept)
        print("Salary:", self.sal)


class Engineer(Employee):
    """
    A subclass of Employee to represent an Engineer with specific attributes like name and age.

    Attributes:
    name (str): The name of the engineer.
    age (int): The age of the engineer.
    """

    def __init__(self, name, age):
        """
        Initialize an Engineer object with name, age, and default role, department, and salary.

        Parameters:
        name (str): The name of the engineer.
        age (int): The age of the engineer.
        """
        self.name = name
        self.age = age
        
        # Initialize the parent class (Employee) with default role, department, and salary
        super().__init__("AI Intern", "Python", "10000")

# Create an instance of Engineer
Kush = Engineer("Kush Doshi", 22)

# Display details of the Engineer (inherited from Employee)
Kush.showDetails()

# Print individual attributes of the Engineer
print("Name:", Kush.name)
print("Age:", Kush.age)
