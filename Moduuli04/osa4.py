import random

pc = random.randint(1,10)
human = int(input("anna luvun jonka kone pitää arvaa: "))

while pc != human:
    if pc > human:
        print("Liian suuri arvaus.")
    elif pc < human:
        print("Liian pieni arvaus.")
    pc = random.randint(1,10)
    human = int(input("anna luvun jonka kone pitää arvaa: "))

print("Oikein!")