
import sys

for i in range(1, len(sys.argv)):
    if int(sys.argv[i]) % 2 == 0:
        print("El número :", sys.argv[i], "Es multiplo de 2")
    else:
        print("El número :", sys.argv[i], "No es multiplo de 2")
