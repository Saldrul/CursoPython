# Ejercicio 1:
# Cree un programa que tome tres valores por consola multiplique el primero por el segundo
# y le sume el tercero. Presente el resultado en la terminal

def multiplier_then_adder(x: int, y: int, z: int) -> int:  # Multiplies the first two variables then adds the third.
    return (x * y) + z


valor_1 = int(input("Ingrese el primer valor aquí "))

valor_2 = int(input("Ingrese el segundo valor aquí "))

valor_3 = int(input("Ingrese el tercer valor aquí "))

print(multiplier_then_adder(valor_1, valor_2, valor_3))

