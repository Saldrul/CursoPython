# Ejercicio 3
# Escriba un programa que consulte al usuario por una oración y comente al usuario cuantas
# veces aparecen todas las vocales considerando minúsculas, mayúsculas y acentos.
import string
vocales_presentes = []
letras_contadas = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0, "á": 0, "é": 0, "í": 0, "ó": 0, "ú": 0}
input_usuario = input("Ingrese su oración; le contaré cuantas veces se repita una vocal : ")
for x in input_usuario:
    if x in letras_contadas:
        letras_contadas[x] += 1
        if x not in vocales_presentes:
            vocales_presentes.append(x)
        continue
for i in range(0, len(vocales_presentes)):
    print(f"La letra {vocales_presentes[i]} aparece {letras_contadas[vocales_presentes[i]]} veces")




