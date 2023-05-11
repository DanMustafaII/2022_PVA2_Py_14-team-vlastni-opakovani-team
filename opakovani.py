#1
cisla = [80, 52, 4, 46, 19]
soucet = sum(cisla)
print("Součet všech čísel v seznamu je:", soucet)

#2
cisla = [1, 12, 3, 4, 5]
druha_mocnina = [cislo**2 for cislo in cisla]
print("Druha mocnina všech čísel v seznamu je:", druha_mocnina)

#3
cisla = [16, 4, 55, 63, 77]
cisla.append(4)
cisla.sort(reverse=True)
print("Seznam čísla seřazen od největšího po nejmenší:", cisla[:-1])

#4
seznam = [("Anna", 50000), ("Petr", 60000), ("Jana", 45000)]
novy_pracovnik = ("Jan", 55000)
seznam.append(novy_pracovnik)
seznam = [pracovnik if pracovnik[0]!="Petr" else ("Pavel", 75000) for pracovnik in seznam]
platy = [pracovnik[1] for pracovnik in seznam]
celkova_castka = sum(platy)
print("Celkova castka vsech plat u pracovniku je:", celkova_castka)
seznam = [pracovnik for pracovnik in seznam if pracovnik[0]!="Anna"]
seznam2 = [("Tomas", 58000), ("Martina", 49000)]
seznam += seznam2
print("Novy seznam pracovniku je:", seznam)
