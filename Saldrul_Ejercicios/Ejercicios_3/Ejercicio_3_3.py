# Escriba un programa que consulte al usuario por una oración
# y comente al usuario cuantas veces aparecen todas las vocales
# considerando minúsculas, mayúsculas y acentos.

pone_oracion = input("Pone una oración: ")
dicc = {}
for i in pone_oracion:
    if i in dicc:
        dicc[i] += 1
    else:
        dicc[i] = 1

for x, c in dicc.items():
    print(f"Hay {c} letras {x}")
