class Student:
    """
    A class to represent a student and calculate the average marks.

    Attributes:
    no_of_subjects (int): The number of subjects the student is enrolled in.
    marks (list): A list to store the marks for each subject.
    """

    def __init__(self):
        """
        Initialize the Student object by asking for the number of subjects.
        It also initializes the 'marks' attribute as an empty list.
        """
        self.no_of_subjects = int(input("Enter how many subjects are there: "))
        self.marks = []  # List to store marks for each subject

    @staticmethod
    def greet():
        """
        Static method to greet the user.
        This method does not depend on any instance attributes.
        """
        print("Hi...")

    def ask_marks(self):
        """
        Ask the user to input marks for each subject.
        The marks are then stored in the 'marks' list.
        """
        self.greet()  # Call the static greet method
        for i in range(1, self.no_of_subjects + 1):
            mark = int(input(f"Enter the marks of Subject {i}: "))
            self.marks.append(mark)  # Add the entered mark to the marks list

    def average_marks(self):
        """
        Calculate and display the average marks of the student.
        It calls 'ask_marks' to gather the marks first.
        """
        self.ask_marks()  # Gather marks from the user
        avg = sum(self.marks) / self.no_of_subjects  # Calculate the average of marks
        print("The average of marks is:", avg)

# Create a Student object and calculate the average marks
s1 = Student()
s1.average_marks()
