# P1A4 - Listas en Python
# Ejemplos del Capitulo 8


# 8.1 Una lista es una secuencia

numbers = [25, 50, 75, 100]
foods = ["pizza", "tacos", "hamburguesa"]
mixed_list = ["Python", 3.5, 20, [5, 10]]
empty_list = []

print(numbers)
print(foods)
print(mixed_list)
print(empty_list)


# 8.2 Las listas son mutables

fruits = ["apple", "mango", "orange"]
print(fruits[0])

numbers = [45, 90]
numbers[1] = 60
print(numbers)


# 8.3 Recorriendo una lista

animals = ["dog", "cat", "rabbit"]

for animal in animals:
    print(animal)

numbers = [2, 4, 6, 8]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

print(numbers)


# 8.4 Operaciones de listas

list1 = [5, 10, 15]
list2 = [20, 25, 30]

combined = list1 + list2
print(combined)

repeated = ["Hello"] * 3
print(repeated)


# 8.5 Rebanado de listas

colors = ["red", "blue", "green", "yellow", "purple", "black"]

print(colors[1:4])
print(colors[:3])
print(colors[3:])


# 8.6 Metodos de listas

cars = []

cars.append("Toyota")
cars.append("Honda")
cars.append("Ford")

print(cars)

more_cars = ["BMW", "Audi"]
cars.extend(more_cars)

print(cars)

cars.sort()
print(cars)


# 8.7 Eliminando elementos

students = ["Daniel", "Sofia", "Mateo", "Emma"]

removed_student = students.pop(1)
print(students)
print(removed_student)

del students[0]
print(students)

students.remove("Emma")
print(students)


# 8.8 Listas y funciones

grades = [85, 92, 76, 88, 95]

print(len(grades))
print(max(grades))
print(min(grades))
print(sum(grades))
print(sum(grades) / len(grades))


# 8.9 Listas y cadenas

sentence = "Python makes programming easier"

words = sentence.split()

print(words)

separator = " "
new_sentence = separator.join(words)

print(new_sentence)


# 8.11 Objetos y valores

a = "computer"
b = "computer"

print(a is b)


# 8.12 Alias

a = [10, 20, 30]
b = a

b[0] = 99

print(a)
print(b)


# 8.13 Listas como argumentos

def remove_first(my_list):
    del my_list[0]


letters = ["x", "y", "z"]

remove_first(letters)

print(letters)


def tail(my_list):
    return my_list[1:]


letters = ["m", "n", "o", "p"]

rest = tail(letters)

print(letters)
print(rest)
