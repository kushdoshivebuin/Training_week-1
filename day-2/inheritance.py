class Parent:
    """
    A class to represent the parent class.

    Methods:
    parentmethod(): A static method that prints a message related to the parent class.
    """

    @staticmethod
    def parentmethod():
        """
        A static method in the Parent class that prints a message.
        """
        print("This is a Parent Class method")

    def __init__(self):
        """
        Default constructor for the Parent class. It prints a message when an object is created.
        """
        print("This is a default constructor of Parent Class")


class Child1(Parent):
    """
    A class to represent a child class that inherits from the Parent class.

    Methods:
    child1method(): A static method that prints a message related to Child 1.
    """

    @staticmethod
    def child1method():
        """
        A static method in the Child1 class that prints a message.
        """
        print("This is a Child 1 Class Method")

    def __init__(self):
        """
        Default constructor for the Child1 class. It prints a message when an object is created.
        """
        print("This is a default constructor of Child 1 Class")


class Child2(Child1):
    """
    A class to represent another child class that inherits from Child1.

    Methods:
    child2method(): A static method that prints a message related to Child 2.
    """

    @staticmethod
    def child2method():
        """
        A static method in the Child2 class that prints a message.
        """
        print("This is a Child 2 Class Method")

    def __init__(self):
        """
        Default constructor for the Child2 class. It prints a message when an object is created.
        """
        print("This is a default constructor of Child 2 Class")


c1 = Child2()

c1.child2method() 
c1.child1method() 
c1.parentmethod() 
