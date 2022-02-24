# Ejercicio 5
# Suponga que tiene una verdulería y carga la cantidad y el precio de lo comprado por un cliente.
# Realice un programa que tome de a uno la cantidad y el precio comprado por el cliente
# y al finalizar la compra retorne el monto total gastado
# partir del ejercicio 5 cree un programa que vaya agregando en un diccionario las compras realizadas.

# Hagamos un combo de ejercicio 7, 8 y 9.
# Alta, baja, modificar, consultar.


def preguntar_usuario(diccionario_compras=None) -> None:
    if diccionario_compras is None:
        diccionario_compras = {}
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"Bienvenido a la verdulería virtual 'Ricky'!")
    print("Ingrese lo que desea hacer, posee 5 opciones disponibles")
    print("1. Comprar.")
    print("2. Cancelar compra.")
    print("3. Consultar.")
    print("4. Modificar")
    print("5. Salir")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    x = int(input("Ingrese lo que desea hacer, del 1 al 5 : "))
    if x == 5:
        print(f"Su lista de productos es : {diccionario_compras}")
        (valores_diccionario) = sum(diccionario_compras.values())
        print(f"Su total debido es : ${valores_diccionario}")
        print("Gracias por venir! Vuelva pronto!")
        exit()
    if x == 1:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        nom_pro = input("Ingrese el nombre de su producto : ")
        precio = (input("Ingrese el precio total de su compra :"))
        precio = int(precio)
        diccionario_compras[nom_pro] = int(precio)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    if x == 2:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(diccionario_compras)
        n = (input("Escriba el nombre del producto que desea eliminar : "))
        show = diccionario_compras.pop(n)
        print(f"Se ha eliminado {show}")
    if x == 3:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("En su carrito de compras tenemos lo siguiente : ")
        print(f"{diccionario_compras}")
        subtotal_actual = sum(diccionario_compras.values())
        print(f"Y el subtotal es ${subtotal_actual}")
    if x == 4:
        print("¿Desea modificar el nombre o el precio total? ")
        y = input("Ingrese 'nombre' o 'precio' : ")
        if y == "nombre":
            nombre_buscado = input("Ingrese el nombre del producto : ")
            nombre_final = input("Ingrese su nuevo nombre : ")
            diccionario_compras[nombre_final] = diccionario_compras[nombre_buscado]
            diccionario_compras.pop(nombre_buscado)
            print(f"El nuevo listado de productos es {diccionario_compras}")
        else:
            objetivo = input("Ingrese el nombre de su producto : ")
            nuevo_precio = input("Ingrese el nuevo precio : ")
            diccionario_compras[objetivo] = nuevo_precio
            print(f"Su lista de productos es ahora {diccionario_compras}")
    preguntar_usuario(diccionario_compras)




preguntar_usuario()


