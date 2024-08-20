
i = 0
x = 999999999999999
z = []
for i in range(x):
    input1 = input("anna luku")
    if input1 == '':
        break
    else:
        z.append(int(input1))
z.sort(reverse=True)
k = z[0:5]
l = ' '.join(str(k) for k in k)
print(l)