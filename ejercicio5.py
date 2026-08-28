# P1A4 - Ejercicio 5

file_name = input("Ingresa un nombre de archivo: ")

file = open(file_name)

count = 0

for line in file:

    if not line.startswith("From "):
        continue

    words = line.split()

    print(words[1])

    count = count + 1

print("Hay", count, "lineas en el archivo con la palabra From al inicio")
