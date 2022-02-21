# Escriba un programa que consulte al usuario por una oración
# y comente al usuario cuantas veces aparecen todas las vocales
# considerando minúsculas, mayúsculas y acentos.
from collections import Counter

pone_oracion = input("Pone una oración: ")
contador = Counter(pone_oracion)
print(contador)


