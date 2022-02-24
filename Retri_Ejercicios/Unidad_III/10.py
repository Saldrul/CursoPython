preguntar_contra = input("Ingrese su contraseña ultra-secreta!")
a = None
while a is None or a != preguntar_contra:
    a = input("Ingrese su contraseña!")
    if a != preguntar_contra:
        print("Incorrecto. Intente de nuevo.")
if a == preguntar_contra:
    print(f"Correcto! Ingrese.")
    exit()