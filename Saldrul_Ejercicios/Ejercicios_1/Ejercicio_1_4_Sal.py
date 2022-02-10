"""
Escriba un programa que solicite el radio de una circunferencia y permita calcular el su
área. Presente el resultado en la terminal del editor.
Utilice la siguiente fórmula:
𝐴 = 𝜋. r^2
A = Área
"""
radio = int(input("Pone el radio de una circunferencia: "))
n_pi = 3.1416
area = n_pi * radio ** 2
print(area)
