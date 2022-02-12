# Escriba un programa que solicite un valor entero por pantalla y presente en la terminal
# editor el valor incrementado en un 10%.

def incrementarvalor():
    valor = int(input("Pone un valor: "))
    incremento = valor * 10 / 100
    valor_incrementado = incremento + valor
    print(valor_incrementado)


incrementarvalor()
