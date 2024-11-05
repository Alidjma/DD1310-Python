class Student:
    """Class that receiving information for first name, last name, ssn."""
    def __init__(self, first_name, last_name, ssn):
        self.first_name = first_name
        self.last_name = last_name
        self.ssn = ssn

    def __repr__(self):
        """Represents out objects that we create and returns a string."""
        return f" {self.first_name} {self.last_name} with a ssn of {self.ssn}\n"


class School:
    def __init__(self):
        self.student_list = []


def name_error_mgmt(comment):
    """ Error handles input for first/last name."""

    while True:
        name = input(comment)
        if name.isdigit():
            print("The name cannot consist of anything but letters. Try again.")
            continue
        elif len(name) == 0:
            print("You must at least use 1 letter.")
        else:
            return name


def ssn_error_mgmt(comment):
    """ Error handles input for ssn"""
    while True:
        ssn = input(comment)
        if ssn.isalpha():
            print("\nYou must select an integer, such as 1, 3, or 20. Please try again.")
            continue
        if len(ssn) != 10 and len(ssn) != 12:
            print("Invalid Social Security number. It must be 10 or 12 digits!")
        else:
            return ssn


def main():
    """Main function that runs the program."""
    n = 0
    while n < 1:
        try:
            n = int(input("How many students do you want to add? "))
        except ValueError:
            print("You must select an integer to print!")
        if n < 1:
            print("You must select at least 1 student.")
    students = School()
    """ Creates a list that stores all student information."""
    for i in range(n):
        first_name = name_error_mgmt("First name: ")
        last_name = name_error_mgmt("Last name: ")
        ssn = ssn_error_mgmt("SSN: ")
        student = Student(first_name, last_name, ssn)
        students.student_list.append(student)
        print("----------------------------------")
        print(f"Student {student} \n----> Created!\n")

    """Prints all students created."""

    print(f"----------------------------------\nStudents at KTH:\n {students.student_list}")

    print(f"The total number of students is: {len(students.student_list)}")


if __name__ == "__main__":
    main()
