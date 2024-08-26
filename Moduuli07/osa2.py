
syote = input("anna nimi: ")
nimet = set()
while syote != '':
    x = 0
    for each in nimet:
        if each == syote:
            x += 1
    if x == 0:
        print("Uusi nimi")
        nimet.add(syote)
    if x >= 1:
        print("Aiemmin syötetty nimi")
    syote = input("anna nimi: ")

for each in nimet:
    print(each)