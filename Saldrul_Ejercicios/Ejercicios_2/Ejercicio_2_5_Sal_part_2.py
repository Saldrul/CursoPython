# Escriba un programa que solicite el radio de una circunferencia y permita calcular el su
# área. Presente el resultado en la terminal del editor.
# Utilice la siguiente fórmula:
# 𝐴 = 𝜋. r^2
# A = Área

import math


def calculararea():
    radio = int(input("Pone el radio de una circunferencia: "))
    area = math.pi * radio ** 2
    print(area)


calculararea()
