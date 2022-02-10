"""
Escriba un programa que solicite el radio de una circunferencia y permita calcular el
perímetro. Presente el resultado en la terminal del editor.
Utilice la siguiente fórmula:

L = 2 · π · r
L = Longitud de perímetro
π = Número pí igual a 3.1416
r = Radio
"""

radio = int(input("Ingrese un Radio: "))
n_pi = 3.1416
longitud_perimetro = 2 * n_pi * radio
print(longitud_perimetro)


