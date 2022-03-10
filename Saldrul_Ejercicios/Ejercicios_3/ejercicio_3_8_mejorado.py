class Verdu:
    def __init__(self):
        self.compras_cliente = []
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
        cual = "Compra numero:"
        iden = 1
        self.lista_compras = []
        que = input("¿Qué producto vas a comprar? ").capitalize()
        cuanto = int(input("¿Cuánto vas a comprar? "))
        precio = int(input("Precio del producto: "))
        total = f"total:, ${cuanto * precio}"
        self.lista_compras.append(cual)
        self.lista_compras.append(iden)
        self.lista_compras.append(que)
        self.lista_compras.append(cuanto)
        self.lista_compras.append(precio)
        self.lista_compras.append(total)
        iden += 1
        self.compras_cliente.append(self.lista_compras)
        print("Compraste ", self.lista_compras)

    def remover(self):
        sacar = int(input("Para remover una compra pone la posición en la que se encuentra tu producto, "
                          "posición primera = 1: "))
        if sacar > len(self.compras_cliente):
            print("---" * 34)
            print("Tu posición no es una compra realizada")
            print("---" * 34)
            self.remover()
        self.compras_cliente.pop(sacar - 1)
        print("Removiste")

    def mirar(self):
        print("Miraste tus compras")
        print(self.compras_cliente)

    def terminar(self):
        self.loop = False
        print("Terminaste")

    def organizar(self):
        cambiar = int(input("Para cambiar una compra pone la posición en la que se encuentra tu producto, "
                            "posición primera = 1: "))
        if cambiar > len(self.compras_cliente):
            print("---" * 34)
            print("Tu posición no es una compra realizada ")
            print("---" * 34)
            self.organizar()
        whating = int(input("¿Qué cosa querés cambiar? nombre = 1, cantidad = 2, precio = 3 "))
        if whating == 1:
            nombre = input("Pone el nuevo nombre ")
            self.compras_cliente[cambiar-1][2] = nombre
        elif whating == 2:
            cantidad = int(input("Pone la nueva cantidad "))
            self.compras_cliente[cambiar-1][3] = cantidad
            actualizar = f"total:, {self.compras_cliente[cambiar-1][3] * self.compras_cliente[cambiar-1][4]}"
            self.compras_cliente[cambiar-1][5] = actualizar
        elif whating == 3:
            precio = int(input("Pone el nuevo precio "))
            self.compras_cliente[cambiar-1][4] = precio
            actualizar = f"total:, ${self.compras_cliente[cambiar-1][3] * self.compras_cliente[cambiar-1][4]}"
            self.compras_cliente[cambiar-1][5] = actualizar
        print("Organizaste")


verd = Verdu()
verd.comprarCosas()
