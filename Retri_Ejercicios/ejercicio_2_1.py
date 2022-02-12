import sys
try:
    for i in range(1, 4):
        if int(sys.argv[i]) % 2 == 0:
            continue
        else:
            print("Falso. No todos los valores son múltiplos de 2")
            exit()
    print("Todos los valore son múltiplos de 2.")
except ValueError or IndexError:
    print("Error en el input del usuario. Ingrese valores numéricos.")
