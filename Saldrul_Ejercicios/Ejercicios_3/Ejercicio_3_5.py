# Suponga que tiene una verdulería y carga la cantidad y el precio de lo comprado por un cliente.
# Realice un programa que tome de a uno la cantidad y
# el precio comprado por el cliente y al finalizar la compra retorne el monto total gastado.


class Verdu:
    def __init__(self):
        self.compras = 0

    def comprarCosas(self):
        que = input("¿Qué vas a comprar? ")
        cuanto = int(input(f"¿Cuánto/a {que} vas a comprar? "))
        precio = int(input(f"¿Cuánto vale? {que} "))
        monto_total = precio * cuanto
        self.compras += 1
        print(monto_total)


comprador = Verdu()
mayuscula = "Y"
while mayuscula == "Y":
    comprador.comprarCosas()
    seguir_comprando = input("¿Querés seguir comprando? Y for yes. N for no ")
    mayuscula = seguir_comprando.upper()
