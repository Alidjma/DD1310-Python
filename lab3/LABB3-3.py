"""Detta är ett program för att beräkna aritmetiska och geometriska summor
samt att jämföra storleken på dessa"""

import felhantering
avslut = "Tack för den här gången"


def beräkna_aritmetisk_summa(nte_element, differens, aritmetiskt_starttal):
    """Beräknar den aritmetiska summan där nte_element = värdet på det nte elementet,
    differensen = differensen mellan två intilliggande tal och aritmetiskt starttal =
    värdet på det element användaren vill starta med i den aritmetiska talföljden"""

    return nte_element * (aritmetiskt_starttal + (aritmetiskt_starttal + differens * (nte_element - 1))) / 2


def beräkna_geometrisk_summa(nte_element, geometriskt_starttal, kvot):
    """Beräknar den geometriska summan där nte_element = värdet på det n:te elementet,
    kvoten = kvoten mellan två intilliggande tal och geometriskt_starttal =
    värdet på det element användaren vill starta med i den geometriska talföljden"""

    return geometriskt_starttal * ((kvot ** nte_element) - 1) / ((kvot) - 1)


def beräkna_aritmetisk_geo_summa():
    """Kör huvudprogrammet och låter användaren välja sina värden på de olika variablerna.
    felhanteringen sköts via modulen "felhantering.py" """
    while True:

        print("Detta program räknar ut aritmetiska och geometriska talfljder samt"
              "jämför storleken på dessa.\n")

        nte_element = felhantering.hantera_fel_för_heltal("Välj ett värde på det n:te elementet: ")

        differens = felhantering.hantera_fel_för_flyttal("Välj differensen: ")

        aritmetiskt_starttal = felhantering.hantera_fel_för_flyttal("Välj ett värde på aritmetiskt starttal: ")

        kvot = felhantering.hantera_fel_för_kvot("välj ett värde på kvoten: ")

        geometriskt_starttal = felhantering.hantera_fel_för_flyttal("Välj ett värde på geometriskt starttal: ")

        aritmetisk_summa = beräkna_aritmetisk_summa(nte_element, differens, aritmetiskt_starttal)
        geometrisk_summa = beräkna_geometrisk_summa(nte_element, geometriskt_starttal, kvot)

        print(f"Den aritmetiska summan är {aritmetisk_summa}")

        print(f"Den geometriska summan är {geometrisk_summa}")

        if geometrisk_summa < aritmetisk_summa:
            print("Den geometriska summan är mindre än den aritmetiska")
        elif geometrisk_summa > aritmetisk_summa:
            print("Den geometriska summan är större än den aritmetiska")
        elif geometrisk_summa == aritmetisk_summa:
            print("summorna är lika")

        avsluta = str(input("\nOm du vill köra programmet igen skriv ja och tryck enter, annars valfri"
                            "tangent och enter för att avsluta: \n"))
        if "ja" in avsluta:
            continue
        else:
            print("\n", avslut)
            break


beräkna_aritmetisk_geo_summa()
