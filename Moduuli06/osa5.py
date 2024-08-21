

def funct1(lista):
    x = []
    z = lista
    for each in lista:
        if each % 2 == 0:
            x.append(each)
    l = ' '.join(str(x) for x in x)
    k = ' '.join(str(z) for z in z)
    return l, k

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 99, 98, 97]
print(funct1(lista))