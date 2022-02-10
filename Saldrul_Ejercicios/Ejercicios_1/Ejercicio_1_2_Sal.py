# Cree un programa que incorpore el módulo sys, al cual desde la terminal se le puedan
# pasar tres parámetros. El programa debe tomar los parámetros e indicar en la terminal si
# son múltiplos de dos.
import sys


print(sys.argv[0])
print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])

if int(sys.argv[1]) % 2 == 0:
    print(sys.argv[1],"es multiplo de 2")
else:
    print(sys.argv[1],"no es multiplo de 2")
if int(sys.argv[2]) % 2 == 0:
    print(sys.argv[2], "es multiplo de 2")
else:
    print(sys.argv[2],"no es multiplo de 2")
if int(sys.argv[3]) % 2 == 0:
    print(sys.argv[2], "es multiplo de 2")
else:
    print(sys.argv[3],"no es multiplo de 2")




