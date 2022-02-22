# Escriba un programa que solicite la edad de la persona e
# imprima todos los años que la persona ha cumplido.

edad_persona = int(input("Pone tu edad: "))
todas_edades = []
for i in range(1, edad_persona + 1):
    todas_edades.append(i)
print(todas_edades)
