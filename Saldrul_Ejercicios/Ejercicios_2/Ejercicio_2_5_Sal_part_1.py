"""
Escriba un programa que solicite el radio de una circunferencia y permita calcular el
perímetro. Presente el resultado en la terminal del editor.
Utilice la siguiente fórmula:

L = 2 · π · r
L = Longitud de perímetro
π = Número pí igual a 3.1416
r = Radio
"""
import math


def calcularperimetro():
    radio = int(input("Ingrese un Radio: "))
    longitud_perimetro = 2 * math.pi * radio
    print(longitud_perimetro)


calcularperimetro()
