# Tome dos valores por consola, y guarde en una lista:
# [primer_valor, segundo_valor, la_suma_de_los_valores]
# Presente el resultado en la terminal del editor

valores = []

valor_1 = int(input("Pone un número:"))
valor_2 = int(input("Pone un número:"))
valores.append(valor_1)
valores.append(valor_2)
valores.append(valor_1 + valor_2)

print(valores)


