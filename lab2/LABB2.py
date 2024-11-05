avslut = "tack för den här gången"


def kör_program_igen():  # låter användaren välja om hen vill köra om programmet.
    kör_igen = input("vill du köra programmet igen? ja/nej: ")
    if kör_igen == "ja":
        return beräkna_aritmetisk_geo_summa("n", "differens", "a1", "kvot", "g1")
    else:
        print(avslut)
        exit()


def beräkna_aritmetisk_geo_summa(n, differens, a1, kvot, g1):  # beräknar aritmetisk och geometrisk summa.
    try:
        n = int(input("Välj ett heltal n: "))
    except ValueError:
        print("Du måste välja ett heltal, ex 1,2 eller 3")
        kör_program_igen()
    try:
        differens = float(input("Välj differensen d: "))
        a1 = float(input("Välj ett värde på aritmetiskt starttal a1: "))
    except ValueError:
        print("Värdet du väljer måste vara ett nummer")
        kör_program_igen()
    try:
        kvot = float(input("Välj värdet på kvoten: "))
        if kvot == 1:
            print("du får inte dividera med noll")
            kör_program_igen()
        g1 = float(input("Välj ett värde på geometriskt starttal g1: "))
    except ValueError:
        print("värdet du väljer måste vara ett nummer")
        kör_program_igen()

    aritmetisk_summa = (n * (a1 + (a1 + differens * (n - 1))) / 2)
    geometrisk_summa = (g1 * ((kvot ** n - 1) / ((kvot) - 1)))

    print(f"Den aritmetiska summan är {aritmetisk_summa}")
    print(f"Den geometriska summan är {geometrisk_summa}")
    if geometrisk_summa < aritmetisk_summa:
        print("Den geometriska summan är mindre än den aritmetiska")
        kör_program_igen()
    elif geometrisk_summa > aritmetisk_summa:
        print("Den geometriska summan är större än den aritmetiska")
        kör_program_igen()
    elif geometrisk_summa == aritmetisk_summa:
        print("summorna är lika")
        kör_program_igen()


beräkna_aritmetisk_geo_summa("n", "differens", "a1", "kvot", "g1")
