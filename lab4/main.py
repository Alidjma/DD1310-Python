class Student:
    """Class som tar emot information för förnamn, efternamn, personnummer."""
    def __init__(self, first_name, last_name, ssn):
        self.first_name = first_name
        self.last_name = last_name
        self.ssn = ssn

    def __str__(self):
        """Representerar vårat objekt som vi skapar och returnerar en sträng."""
        return f"Studenten heter {self.first_name} {self.last_name} och har personnummer {self.ssn}"


def name_error_mgmt(comment):
    """ Felhanterar input för förnamn och efternamn"""

    while True:
        name = input(comment)
        if name.isdigit():
            print("Namnet kan inte bestå av något annat än bokstäver. Försök igen.")
            continue
        else:
            return name


def ssn_error_mgmt(comment):
    """ Felhanterar input för personnummer"""
    while True:
        ssn = input(comment)
        if ssn.isalpha():
            print("\nDu måste välja ett heltal, till exempel 1, 3 eller 20. Försök igen.")
            continue
        if len(ssn) < 10 and len(ssn) < 12:
            print("Ogiltigt personnummer. Det måste vara 10 eller 12 siffror")
        else:
            return ssn


def main():
    """Main funktion som kör programmet."""
    n = 0
    while n < 1:
        try:
            n = int(input("Hur många studenter vill du lägga till? "))
        except ValueError:
            print("Du måste välja ett heltal att skriva ut!")
        if n < 1:
            print("Du måste välja minst 1 student.")

    """ Skapar en lista som lagrar all student information."""
    students = []
    for i in range(n):
        first_name = name_error_mgmt("Förnamn: ")
        last_name = name_error_mgmt("Efternamn: ")
        ssn = ssn_error_mgmt("Personnummer: ")
        student = Student(first_name, last_name, ssn)
        students.append(student)
        print("\nObjekt skapat!\n")

    """Skriver ut alla studenter som skapats."""
    for student in students:
        print(student)
    print(f"Totala antalet studenter är: {len(students)}")


main()
