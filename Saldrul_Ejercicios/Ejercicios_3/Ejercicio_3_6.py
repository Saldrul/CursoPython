# A partir del ejercicio 5 cree un programa que vaya agregando en una lista
# las compras realizadas.


class Verdu:
    def __init__(self):
        self.compras_cliente = []

    def comprarCosas(self):
        que = input("¿Qué vas a comprar? ")
        cuanto = int(input(f"¿Cuánto/a {que} vas a comprar? "))
        precio = int(input(f"¿Cuánto vale? {que} "))
        monto_total = precio * cuanto
        amontonamiento = [que, monto_total]
        self.compras_cliente.append(amontonamiento)
        print(f"{cuanto} {que} te cuesta: {monto_total}")

    def mostrarCosas(self):
        print(self.compras_cliente)
        suma_total = 0
        for i in range(0, len(self.compras_cliente)-1):
            self.compras_cliente[i][1] += self.compras_cliente[i+1][1]
        print("esta es la suma total: ",self.compras_cliente[0][1])


comprador = Verdu()
seguir_com_mayu = "Y"
while seguir_com_mayu == "Y":
    comprador.comprarCosas()
    seguir_comprando = input("¿Querés seguir comprando? Y for yes. N for no ")
    seguir_com_mayu = seguir_comprando.upper()
comprador.mostrarCosas()
