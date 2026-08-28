# P1A4 - Ejercicio 4

file_name = input("Ingresa nombre de archivo: ")

file = open(file_name)

words_list = []

for line in file:

    words = line.split()

    for word in words:

        if word not in words_list:
            words_list.append(word)

words_list.sort()

print(words_list)
