def bensiini(gallons):
    litroina = gallons * 3.785
    return litroina

kyse = int(input("Anna gallonin määrä: "))
while kyse > 0:
    x = bensiini(kyse)
    print(x)
    kyse = int(input("Anna gallonin määrä: "))
