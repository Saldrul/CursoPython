# Ejercicio 6
# A partir del ejercicio 5 cree un programa que vaya agregando en una lista las compras realizadas

def calculadora_verduleria(total_debido: int = 0, productos_comprados=None, ) -> None:
    if productos_comprados is None:
        productos_comprados = []
    pregunta_compra = input("Desea continuar su compra? Ingrese sí o no : ")
    pregunta_compra = pregunta_compra.lower()
    if not (pregunta_compra == "sí" or pregunta_compra == "si"):
        print(f"Su total debido es {total_debido} y compró {productos_comprados}")
        print(f"¡Vuelva prontos!")
        exit()
    else:
        tipo_de_producto = input("¿Qué producto desea comprar? ")
        cantidad = int(input("¿Cuántos KG/Unidades desea? "))
        precio = int(input("¿Qué precio tiene por kg/unidad? "))
        productos_comprados.append([cantidad, tipo_de_producto])
        total_debido += cantidad * precio
        calculadora_verduleria(total_debido, productos_comprados)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Bienvenido a la verdulería virtual 'Ricky'!")
print("Ingrese el nombre de su producto, así como también la cantidad y el precio por kg.")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
calculadora_verduleria()