# Ejercicio 7
# A partir del ejercicio 5 cree un programa que vaya agregando en un diccionario las compras realizadas.

class Verduleria:
    def __init__(self, nombre: str, total_debido=0, productos_comprados=None):
        if productos_comprados is None:
            productos_comprados = []
        self.total_debido = total_debido
        self.productos_comprados = productos_comprados
        self.nombre = nombre

    def apertura(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"Bienvenido a la verdulería virtual '{self.nombre}'!")
        print("Ingrese el nombre de su producto, así como también la cantidad y el precio por kg.")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        self.preguntar_accion()

    def modificar(self):
        print(f"Sus productos son: {self.productos_comprados}")
        decision_usuario = input(f"¿Desea dar de baja un producto? Escriba sí para continuar.")
        decision_usuario = decision_usuario.lower()
        if decision_usuario == 'si' or decision_usuario == 'sí':
            print(f"La lista de productos comprados es : {self.productos_comprados}")
            print("Ingrese el índice del producto que desee eliminar; comenzando del 1 en adelante.")
            try:
                a_eliminar = ((int(input("Ingrese el número."))) - 1)
                new_string = ""
                new_string = self.productos_comprados[a_eliminar][2][0:-1]
                self.productos_comprados[a_eliminar][2] = new_string
                self.total_debido -= int(new_string)
                eliminado = self.productos_comprados.pop(a_eliminar)
                print(f"Se ha eliminado {eliminado}.")
            except ValueError:
                print("Ingrese un número, en su versión numérica '1', '2', etc.")
                self.modificar()
            self.preguntar_accion()

        else:
            self.preguntar_accion()

    def consultar(self):
        print(f"Su lista de productos es : {self.productos_comprados}")
        self.preguntar_accion()

    def comprar(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        nombre = input("Ingrese el nombre de su producto: ")
        cantidad = int(input("Ingrese la cantidad / KGs a comprar: "))
        precio = int(input("Ingrese el precio por KG/unidad : "))
        precio_total = str(precio * cantidad)
        self.productos_comprados.append([cantidad, nombre, precio_total + '$'])
        self.total_debido += int(precio_total)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        self.preguntar_accion()

    def preguntar_accion(self):
        input_usuario = input("Qué desea hacer? Comprar, consultar, finalizar, o modificar su compra? ")
        input_usuario = input_usuario.lower()
        if input_usuario == "finalizar" or input_usuario == "end" or input_usuario == "terminar":
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(f"¡Por supuesto! El total de su compra es ${self.total_debido}")
            print(f"Sus lista de objetos comprados es {self.productos_comprados}")
            print(f"Ha comprado un total de {len(self.productos_comprados)} productos.")
            print(f"¡Vuelva prontos!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            exit()
        if input_usuario == "comprar" or input_usuario == "compra":
            self.comprar()
        if input_usuario == "modificar":
            self.modificar()
        if input_usuario == "consulta" or input_usuario == "consultar":
            self.consultar()
        else:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Mmm, no reconozco esta oración. Intente usando 'comprar', 'finalizar' o 'modificar'")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            self.preguntar_accion()


mi_verduleria = Verduleria("Verduleria Ricky")
mi_verduleria.apertura()
