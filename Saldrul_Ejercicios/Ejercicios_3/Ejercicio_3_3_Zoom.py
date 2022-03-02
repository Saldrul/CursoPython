# Escriba un programa que consulte al usuario por una oración
# y comente al usuario cuantas veces aparecen todas las vocales
# considerando minúsculas, mayúsculas y acentos.
contador_a = 0
contador_e = 0
contador_i = 0
contador_o = 0
contador_u = 0
oracion = input("Pone una oración: ")
vocales = ["a","e","i","o","u"]
for vocal in vocales:
    for letra in oracion:
        if letra == vocal or letra == vocal.upper():
            contador_a += 1
for i in range(0, len(vocales)):
    print("hay", contador_a, vocales[0])

print("hay",contador_a, vocales[0])








"""
oracion = input("Pone una oración: ")
vocales = ["a","e","i","o","u"]
for vocal in vocales:
    contador = 0
    for letra in oracion:
        if letra == vocal or letra == vocal.upper():
            contador += 1
    print(vocal, contador)
"""

