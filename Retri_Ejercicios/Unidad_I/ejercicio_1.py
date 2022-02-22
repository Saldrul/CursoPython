# Ejercicio 1:
# Cree un programa que tome tres valores por consola multiplique el primero por el segundo
# y le sume el tercero. Presente el resultado en la terminal
import sys


# import sys
#
#
# def multiplier_then_adder(x: int, y: int, z: int) -> int:  # Multiplies the first two variables then adds the third.
#     return (x * y) + z
#
#
# valor_1 = int(input("Ingrese el primer valor aquí "))
#
# valor_2 = int(input("Ingrese el segundo valor aquí "))
#
# valor_3 = int(input("Ingrese el tercer valor aquí "))
#
# print(multiplier_then_adder(valor_1, valor_2, valor_3))


def funcion_loca(analyzed_list: list[str]) -> None:
    for i in range(1, len(sys.argv)):
        if int(sys.argv[i]) % 2 == 0:
            continue
        else:
            print("Falso. No todos los valores son múltiplos de 2")
            exit()
    print("Todos los valore son múltiplos de 2.")


funcion_loca(sys.argv)
