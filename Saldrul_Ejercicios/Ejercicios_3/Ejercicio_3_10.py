password_correcta = "albatros"
iniciar_sesion = input("Introduzca la contraseña: ")
while iniciar_sesion != password_correcta:
    iniciar_sesion = input("Esa contraseña no es correcta, itroduzca otra: ")
    if iniciar_sesion == password_correcta:
        print("Has ingresado, la contraseña era correcta")



