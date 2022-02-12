i_g = str(input("¿Cuál es tu género? por favor indiquelo con una "
                "M (Masculino) o una F (Femenino) "))
edad_jubilatoria_M = 65
edad_jubilatoria_F = 60
i_g = i_g.lower()
print(i_g)
if i_g == "m" or i_g == "hombre" or i_g == "masculino":
    hombre = int(input("¿ M Cuál es tu edad? "))
    if hombre < edad_jubilatoria_M:
        print("Aún está en edad de trabajar")
    elif hombre >= edad_jubilatoria_M:
        print("Ya esá en edad de jubilarse")
if i_g == "f" or i_g == "mujer" or i_g == "femenino":
    mujer = int(input("¿ F Cuál es tu edad? "))
    if mujer < edad_jubilatoria_F:
        print("Aún está en edad de trabajar")
    elif mujer >= edad_jubilatoria_F:
        print("Ya esá en edad de jubilarse")
