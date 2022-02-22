# Cree una lista de frutas de 2 elementos, y realice un programa que muestre una oración
# conteniendo los dos elementos de la lista concatenándolos con texto para formar una
# oración con sentido Presente el resultado en la terminal del editor.
import sys
module_object = 2
for i in range(1, len(sys.argv)):
    if int(sys.argv[i]) % module_object == 0:
        print(f"El elemento número {i} es múltiplo de {module_object}")
    else:
        print(f"El elemento número {i} no es múltiplo de {module_object}")

