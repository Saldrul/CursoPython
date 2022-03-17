#Ejercicio 5 – Dificultad media
# Cree un programa que utilizando una función, solicite la edad de la persona e imprima todos los años que
# la persona ha cumplido según el siguiente formato de ejemplo.
# 1, 2, 3, 4, 5
# Y
# 5, 4, 3, 2, 1

def edades():
    edad = int(input("Pone tu edad: "))
    edad_lista_1 = []
    edad_lista_2 = []
    for x in range(1, edad+1):
        edad_lista_1.append(x)
    print(edad_lista_1)
    for i in range(edad, 0 ,-1):
        edad_lista_2.append(i)
    print(edad_lista_2)

edades()

# lo hice en menos de 6 de minutos, estoy orgulloso de mi mismo y espero que ustedes también.

