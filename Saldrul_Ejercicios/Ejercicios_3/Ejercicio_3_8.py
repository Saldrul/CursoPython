# A partir del ejerció 6 cree un programa con 4 funciones:
# alta() para dar de alta la nueva compra
# baja() para dar de baja una compra
# consulta() para consultar por todas las compras realizadas hasta el momento
# modificar() para modificar una compra realizada

class Verdu:
    def __init__(self):
        self.compras_cliente = []

    def comprarCosas(self):
        que = input("¿Qué vas a comprar?  (X para cancelar compra) ")
        if que == "X":
            comprador.consulta()
        cuanto = int(input(f"¿Cuánto/a {que} vas a comprar? "))
        precio = int(input(f"¿Cuánto vale? {que} "))
        monto_total = precio * cuanto
        lista_adentro = []
        lista_adentro.append(que)
        lista_adentro.append(monto_total)
        self.compras_cliente.append(lista_adentro)
        print(f"{cuanto} {que} te cuesta: {monto_total}")

    def mostrarCosas(self):
        suma = 0
        for i in self.compras_cliente:
            suma += i[1]
        print(f"esta es la suma total por el momento: ${suma}")

    def baja(self):
        seguir_com_mayu = "Y"
        while seguir_com_mayu == "Y":
            comprador.comprarCosas()
            seguir_comprando = input("¿Querés seguir comprando? Y for yes. N for no ").upper()
            comprador.consulta()

    def consulta(self):
        preguntar = input("Para terminar de comprar: X, para consultar compras: C ").upper()
        if pregun_mayu == "X":
            exit()
        else:
            print("---"*30)
            comprador.mostrarCosas()
            print("---" * 30)
            comprador.baja()


comprador = Verdu()
comprador.mostrarCosas()
comprador.baja()
comprador.consulta()
