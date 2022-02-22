# Ejercicio 2
# Escriba un programa que consulte al usuario por una oración y comente al usuario cuantas veces aparece la letra “a”.
candidate_letter = "a"
intro = input(f"Ingrese una oración; le diré cuantas veces aparece la letra '{candidate_letter}' ")

response = intro.count("a")
print(f"La letra {candidate_letter} aparece {response} veces")
