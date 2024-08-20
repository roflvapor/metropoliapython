
input1 = int(input("anna kokonaisluku: "))
counter = 0
for i in range(2, input1):
    if input1 % i == 0:
        counter += 1
        if counter == 1:
            print("ei ole alkuluku")
            break
if counter != 1:
    print("on alkuluku")