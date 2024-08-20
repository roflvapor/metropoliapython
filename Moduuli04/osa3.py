maxluku = 0
minluku = 0
syote = input("anna luku: ")
while syote != '':
    syote1 = int(syote)
    if syote1 > maxluku:
        maxluku = int(syote1)
    elif syote1 < minluku:
        minluku = int(syote1)
    syote = input("anna luku: ")

print("suurin luku: ", maxluku)
print("pienin luku: ", minluku)
