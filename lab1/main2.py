"""laboration som gör att du kan välja att beräkna aritmetiska och geometriska talföljder"""

def beräkna_differans(d1, d2):
    return d2 - d1
"""här beräknas differansen mellan två tal"""

def beräkna_talföljd_an(a1, n):
    return a1 - beräkna_differans(3, 2) * (n - 1)
"""här beräknas taljfölden an beräkna aritmetiska summor för talet n"""

def beräkna_aritmetiska_summa(a1,n):
    return (n*(a1 + beräkna_talföljd_an(3, 2))) // 2
"""beräknas den aritmetiska summan för talen genom följande formel ovan"""

def beräkna_element_kvot(g2,g1):
    return g2//g1
"""beräknar kvoten mellan två efterliggande tal"""

def beräkna_gn(g1,n):
    return g1*beräkna_element_kvot(4,2)**(n-1)
"""beräknar talet gn"""

def beräkna_geometrisk_summa(g1,n):
    return g1*(beräkna_element_kvot(4,2)**(n-1))//(beräkna_element_kvot(4,2)-1)
"""beräknar den geometriska summan"""

print(f"aritmetiska summan blir {beräkna_aritmetiska_summa(1,2)}")
print(f"geometriska summan blir {beräkna_geometrisk_summa(4,2)}")

"""det som gick bra: skriva upp funktioner och returnera och strukturera koden
det som gick mindre bra: att formulera om de matematiska formlerna så att koden fungerade """