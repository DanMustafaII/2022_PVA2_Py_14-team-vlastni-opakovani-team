#1
cisla_1 = [1, 2, 3, 4, 5]
sum = 0

for number in cisla_1:
    sum += number

#2
cisla_2 = [2, 4, 8, 9, 3]

for number in cisla_2:
    print("mocnina čísla", cisla_2, "je", cisla_2**2)

#3
cisla_3 = [3, 6, 1, 8, 2, 10, 5]
cisla_3.append(4)

sr_cisla = sorted(cisla_3, reverse=True)

print("čísla od největší po nejmenšího:", sr_cisla)

#4
zamestnanci = {"Alice": 50000, "Bob": 60000, "Charlie": 70000}

zamestnanci.update({"David": 55000})

zamestnanci[1] = {"Bob": 65000}

celkova_mzda = sum(zamestnanci.values())

print("Celková mzda všech zaměstnanců je:", celkova_mzda)

del zamestnanci[0]

dalsi_zamestnanci = {"Eva": 45000, "Frank": 55000, "George": 65000}

zamestnanci.update(dalsi_zamestnanci)

print("Seznam zaměstnanců a jejich mzdy:", zamestnanci)
