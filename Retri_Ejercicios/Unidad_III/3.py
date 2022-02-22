# Ejercicio 3
# Escriba un programa que consulte al usuario por una oración y comente al usuario cuantas
# veces aparecen todas las vocales considerando minúsculas, mayúsculas y acentos.
import string
response = 0
candidate_letter = "aeiouáéíóú"
intro = input(f"Ingrese una oración; le diré cuantas veces aparece las vocales 'aeiou' ")
intro = intro.lower()
for i, k in enumerate(intro):
    if k in candidate_letter:
        response += 1
    else:
        continue

print(f"Las letras '{candidate_letter}' aparecen {response} veces")
