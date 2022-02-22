# Asumimos una edad de jubilación de 65 para hombres y 60 para los demás.
ask_user = int(input("Ingrese su edad : "))
edad = ask_user
if ask_user < 60:
    print("Usted no está en edad de jubilarse.")
elif ask_user < 65:
    ask_user = (input("¿Es usted un hombre? "))
    ask_user.lower()
    if ask_user == "sí" or ask_user == "si":
        print("Usted no está en edad de jubilarse.")
    else:
        if edad > 60:
            (print("Usted está en edad de jubilarse."))
elif ask_user >= 65:
    print("Usted está en edad de jubilarse")


