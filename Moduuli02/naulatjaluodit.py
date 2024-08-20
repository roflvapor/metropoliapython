import math

leiviska = float(input("Anna leiviskät: "))
naula = float(input("Anna naulat: "))
luoti = float(input("Anna luodit: "))

grammat = luoti * 13.3 + naula * 32 * 13.3 + leiviska * 20 * 32 * 13.3
kilot = grammat / 1000

grammat1 = math.trunc(kilot) * 1000
grammat2 = grammat - grammat1

grammatvastaus = str(grammat2)
grammatvastaus.split(".")
print(str(math.trunc(kilot)) + " kilogrammaa ja " + grammatvastaus[0:6] + " grammaa.")
print(grammat)