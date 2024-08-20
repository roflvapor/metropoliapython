import math

leiviska = float(input("Anna leiviskät: "))
naula = float(input("Anna naulat: "))
luoti = float(input("Anna luodit: "))

leiviskagramma = leiviska * 20 * 32 * 13.3
naulat = naula * 32 * 13.3
luoti = luoti * 13.3

print(leiviskagramma + naulat + leiviska)
#leiviska 25 536 g
#naula  3 830,4 g
#luoti 179,55