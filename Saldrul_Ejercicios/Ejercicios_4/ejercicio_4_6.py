# Ejercicio 6 – Dificultad alta
# Cree una función que tome la siguiente lista y reordene de menor a mayor sus componentes:
# [3, 44, 21, 78, 5, 56, 9]
def arreglar_lista():
    lista_rota = [3, 44, 21, 78, 5, 56, 9]
    for i in range(-1, len(lista_rota)-1):
        if lista_rota[i+1] < lista_rota[i]:
            lista_rota.append(lista_rota.pop(i))

    print(lista_rota)


arreglar_lista()

# no me sale lsoy retard
