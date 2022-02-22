# A partir del ejercicio 5 cree un programa que vaya agregando en un
# diccionario las compras realizadas.

class Verdu:
    def __init__(self):
        self.compras_cliente = []

    def comprarCosas(self):
        que = input("¿Qué vas a comprar? ")
        cuanto = int(input(f"¿Cuánto/a {que} vas a comprar? "))
        precio = int(input(f"¿Cuánto vale? {que} "))
        monto_total = precio * cuanto
        self.compras_cliente.append(que)
        self.compras_cliente.append(monto_total)
        print(f"{cuanto} {que} te cuesta: {monto_total}")

    def mostrarCosas(self):
        print(self.compras_cliente)


comprador = Verdu()
seguir_com_mayu = "Y"
while seguir_com_mayu == "Y":
    comprador.comprarCosas()
    seguir_comprando = input("¿Querés seguir comprando? Y for yes. N for no ")
    seguir_com_mayu = seguir_comprando.upper()
comprador.mostrarCosas()