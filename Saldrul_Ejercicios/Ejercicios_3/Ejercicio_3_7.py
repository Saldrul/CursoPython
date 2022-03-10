# A partir del ejercicio 5 cree un programa que vaya agregando en un
# diccionario las compras realizadas.

class Verdu:
    def __init__(self):
        self.dicc_compras = {}
        self.total_compras = 0

    def comprarCosas(self):
        que = input("¿Qué vas a comprar? ")
        cuanto = int(input(f"¿Cuánto/a {que} vas a comprar? "))
        precio = int(input(f"¿Cuánto vale? {que} "))
        monto_total = precio * cuanto
        self.dicc_compras[que] = monto_total
        print(f"{cuanto} {que} te cuesta: {monto_total}")
        self.total_compras = sum(self.dicc_compras.values())

    def mostrarCosas(self):
        print(self.dicc_compras)
        print("Todas tus compras cuestan: ", self.total_compras)


comprador = Verdu()
seguir_com_mayu = "Y"
while seguir_com_mayu == "Y":
    comprador.comprarCosas()
    seguir_comprando = input("¿Querés seguir comprando? Y for yes. N for no ")
    seguir_com_mayu = seguir_comprando.upper()
comprador.mostrarCosas()
