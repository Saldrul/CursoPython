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
        lista_adentro = []
        lista_adentro.append(que)
        lista_adentro.append(monto_total)
        self.compras_cliente.append(lista_adentro)
        print(f"{cuanto} {que} te cuesta: {monto_total}")

    def mostrarCosas(self):
        print(self.compras_cliente)
        suma = 0
        for i in self.compras_cliente:
            suma += i[1]
        print(f"esta es la suma total: {suma}")

comprador = Verdu()
seguir_com_mayu = "Y"


while seguir_com_mayu == "Y":
    comprador.comprarCosas()
    seguir_comprando = input("¿Querés seguir comprando? Y for yes. N for no ")
    seguir_com_mayu = seguir_comprando.upper()
comprador.mostrarCosas()
