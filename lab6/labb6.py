"""Program that will ask for user input to open a file and read from it"""


class Student:
    """Class constructor that receives information for first name, last name, ssn."""
    def __init__(self, ssn, last_name, first_name):
        self.first_name = first_name
        self.last_name = last_name
        self.ssn = ssn

    def __str__(self):
        """Returns objects that we create and returns a string."""
        return f" Name: {self.first_name} {self.last_name} SSN: {self.ssn}\n"


class School:
    """Class that sorts our students in a list"""
    def __init__(self):
        self.student_list = []

    def read_file(self, user_input):
        """Function that opens & sorts the file and put it on a list"""

        file = open(user_input, "r")
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            cred_list = line.split(";")
            ssn = str(cred_list[0])
            last_name = str(cred_list[1])
            first_name = str(cred_list[2])
            student = Student(ssn, last_name, first_name)
            self.student_list.append(student)
            file.close()

    def __str__(self):
        """Takes the information from the list and makes it readable, student by student."""

        final_list = ""
        for student in self.student_list:
            final_list += f"{str(student)}"

        return final_list.strip()


def main():
    """Main function that opens file and ask user for input."""
    school = School()
    while True:
        try:
            school.read_file(input("Choose a file to open: "))
        except FileNotFoundError:
            print("File was not found! Try again. ")
            continue
        print("\nAccess open. File was found!")
        print(f"Students at KTH are:\n {school}")
        break


main()
