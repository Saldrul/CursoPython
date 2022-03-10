class Verdu:
    def __init__(self):
        self.dicc_compras = {}
        self.loop = True

    def comprarCosas(self):
        while (self.loop) == True:
            resp = input("Comrar: C, Remover compra: R, Mirar compra: M, Terminar: T "
                         "Organizar compra: O ").upper()
            if resp == "C":
                self.comprar()
            elif resp == "R":
                self.remover()
            elif resp == "M":
                self.mirar()
            elif resp == "T":
                self.terminar()
            elif resp == "O":
                self.organizar()
            else:
                print("No pusiste un comando valido")
        print("Llevate esta... sheesh!!!")

    def comprar(self):

        self.dicc_compras = {}
        que = input("¿Qué producto vas a comprar? ").capitalize()
        cuanto = int(input("¿Cuánto vas a comprar? "))
        precio = int(input("Precio del producto: "))
        total = f"total:, ${cuanto * precio}"
        self.dicc_compras[que] = que
        self.dicc_compras[cuanto] = cuanto
        self.dicc_compras[precio] = precio
        self.dicc_compras[total] = total
        print("Compraste ", self.dicc_compras)

    def remover(self):
        sacar = input("Para remover una compra pone el número de la compra que quieras eliminar")

        if sacar != self.dicc_compras:
            print("---" * 34)
            print("No existe esa compra")
            print("---" * 34)
            self.remover()
        self.dicc_compras.pop(sacar)
        print("Removiste")

    def mirar(self):
        print("Miraste tus compras")
        print(self.dicc_compras)

    def terminar(self):
        self.loop = False
        print("Terminaste")

    def organizar(self):
        cambiar = int(input("Para cambiar una compra pone la posición en la que se encuentra tu producto, "
                            "posición primera = 1: "))
        if cambiar > len(self.dicc_compras):
            print("---" * 34)
            print("Tu posición no es una compra realizada ")
            print("---" * 34)
            self.organizar()
        whating = int(input("¿Qué cosa querés cambiar? nombre = 1, cantidad = 2, precio = 3 "))
        if whating == 1:
            nombre = input("Pone el nuevo nombre ")
            self.dicc_compras[cambiar-1][2] = nombre
        elif whating == 2:
            cantidad = int(input("Pone la nueva cantidad "))
            self.dicc_compras[cambiar-1][3] = cantidad
            actualizar = f"total:, {self.dicc_compras[cambiar-1][3] * self.dicc_compras[cambiar-1][4]}"
            self.dicc_compras[cambiar-1][5] = actualizar
        elif whating == 3:
            precio = int(input("Pone el nuevo precio "))
            self.dicc_compras[cambiar-1][4] = precio
            actualizar = f"total:, ${self.dicc_compras[cambiar-1][3] * self.dicc_compras[cambiar-1][4]}"
            self.dicc_compras[cambiar-1][5] = actualizar
        print("Organizaste")


verd = Verdu()
verd.comprarCosas()
