
x = "python"
y = "rules"

inp1 = str(input("Käyttäjätunnus: "))
inp2 = str(input("Salasana: "))
counter = 0
while counter < 4:
    if inp1 == x and inp2 == y:
        print("Tervetuloa")
        break
    else:
        counter += 1
        print("Jotain meni pieleen.")
        inp1 = str(input("Käyttäjätunnus: "))
        inp2 = str(input("Salasana: "))

if(counter == 4):
    print("Pääsy evätty")