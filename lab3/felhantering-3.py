"""Detta är modulen för felhantering."""


def hantera_fel_för_heltal(kommentar):
    """Felhantering för användarens inmatning av heltal"""

    while True:
        try:
            heltal = int(input(kommentar))
            if heltal <= 0:
                print("Du måste välja ett heltal större än noll")
                continue
        except ValueError:
            print("Du måste välja ett heltal, till exempel 1, 3 eller 20. Försök igen.")
        else:
            return heltal


def hantera_fel_för_flyttal(kommentar):
    """Felhantering för användarens inmatning av flyttal"""

    while True:
        try:
            flyttal = float(input(kommentar))
        except ValueError:
            print("Värdet du väljer måste vara ett reellt tal, till exempel 0.2, 3 eller 4.45. Försök igen")
            continue
        else:
            return flyttal


def hantera_fel_för_kvot(kommentar):
    """Felhanterar division med noll samt användarens inmatning av flyttal för kvoten"""

    while True:
        try:
            kvot = float(input(kommentar))
            if kvot == 1:
                print("Du får inte dividera med noll. Försök igen")
                continue
        except ValueError:
            print("Värdet du väljer måste vara ett reellt tal, till exempel 0.2, 3 eller 4.45. Försök igen")
            continue
        else:
            return kvot
