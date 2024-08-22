import math
def pizza(halkaisija, euro):
    halkaisija = halkaisija / 2
    neliocm = math.pi * halkaisija ** 2
    neliom = neliocm / 10000
    europerm = euro / neliom
    return europerm

piz1cm = int(input("Anna pizzan 1 halkaisija: "))
piz1eur = int(input("Anna pizzan 1 hinta: "))
piz2cm = int(input("Anna pizzan 2 halkaisija: "))
piz2eur = int(input("Anna pizzan 2 hinta: "))

piz1 = pizza(piz1cm, piz1eur)
piz2 = pizza(piz2cm, piz2eur)

minhintaper = min(piz1, piz2)
if minhintaper == piz1:
    print("Pizza 1 on paras hinta, ", minhintaper, "euroa per neliometri")
if minhintaper == piz2:
    print("Pizza 2 on paras hinta", minhintaper, "euroa per neliometri")