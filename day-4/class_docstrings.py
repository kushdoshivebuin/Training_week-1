class Employee :
    """
    Represents a employee.

    Attributes :
    name (str) : The name of the employee.
    position (str) : The job position of the employee.
    salary (float) : The salary of the employee.

    Methods :
    give_raise (percentage) : Increases the salary by a given percentage.
    """

    def __init__(self , name , position , salary):
        self.name = name
        self.position = position
        self.salary = salary

    def give_raise (self , percentage) :
        """
        Increases the salary by the given percentage.
        
        Parameters :
        percentage (int or float) : The percentage increase of the salary.
        
        Returns :
        The increased salary by the given percentage.
        """

        self.salary += self.salary * (percentage / 100)

E1 = Employee("Kush" , "AI Intern" , 10000)
E1.give_raise(5)
print(E1.salary)
