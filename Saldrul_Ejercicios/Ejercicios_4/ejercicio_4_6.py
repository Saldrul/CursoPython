# Ejercicio 6 – Dificultad alta
# Cree una función que tome la siguiente lista y reordene de menor a mayor sus componentes:
# [3, 44, 21, 78, 5, 56, 9]
def arreglar_lista():
    lista = [3, 44, 21, 78, 5, 56, 9]
    for i in range(1, len(lista)):
        for pos in range(len(lista) - i):
            if lista[pos] > lista[pos+1]:
                cambiar_posicion = lista[pos]
                lista[pos] = lista[pos+1]
                lista[pos + 1] = cambiar_posicion



    print(lista)


arreglar_lista()

# no me sale lsoy retard
