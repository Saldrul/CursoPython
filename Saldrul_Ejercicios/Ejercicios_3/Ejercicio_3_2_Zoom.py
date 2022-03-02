# Escriba un programa que consulte al usuario por una oración y
# comente al usuario cuantas veces aparece la letra “a”.


oracion = input("Pone una oración: ")
cantidad_de_a = 0
for i in range(0, len(oracion)):
    if oracion[i] == "a":
        cantidad_de_a += 1
print(cantidad_de_a)
