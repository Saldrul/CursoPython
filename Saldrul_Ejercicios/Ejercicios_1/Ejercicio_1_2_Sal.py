# Cree un programa que incorpore el módulo sys, al cual desde la terminal se le puedan
# pasar tres parámetros. El programa debe tomar los parámetros e indicar en la terminal si
# son múltiplos de dos.
import sys


print(sys.argv[0])
print(sys.argv[1])

for i in range(1, len(sys.argv)):
    if int(sys.argv[i]) % 2 == 0:
        print((sys.argv[i]), "Es multiplo de 2")
    else:
        print((sys.argv[i]), "No es multiplo de 2")
