# Cree un programa que tome tres valores por consola
# multiplique el primero por el segundo y le sume el tercero.
# Presente el resultado en la terminal
def calcu(x: int, y: int, z: int) -> int:
    return(x * y) + z


print("A continuación coloque 3 numeros, el 1ero será multiplicado por el 2do y luego el 3ero"
          "será sumado a la cuenta")
valor_1 = int(input("Primer Número: "))
valor_2 = int(input("Segundo Número: "))
valor_3 = int(input("Tercer Número: "))


print(calcu(valor_1,valor_2,valor_3))


