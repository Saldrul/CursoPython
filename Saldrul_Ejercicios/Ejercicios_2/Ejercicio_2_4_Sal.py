indicador_genero = input("¿Cuál es tu género? por favor indiquelo con una "
                         "M mayuscula (Masculino) o una F mayuscula (Femenino) ")
edad_jubilatoria_M = 65
edad_jubilatoria_F = 60

if indicador_genero == "M":
    hombre = int(input("¿ M Cuál es tu edad? "))
    if hombre < edad_jubilatoria_M:
        print("Aún está en edad de trabajar")
    elif hombre >= edad_jubilatoria_M:
        print("Ya esá en edad de jubilarse")
else:
    mujer = int(input("¿ F Cuál es tu edad? "))
    if mujer < edad_jubilatoria_F:
        print("Aún está en edad de trabajar")
    elif mujer >= edad_jubilatoria_F:
        print("Ya esá en edad de jubilarse")
