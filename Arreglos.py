""" #Declarando un arreglo
numeros = [10, 20, 30, 40, 50]

#Imprimimos un elemento espe. del arreglo 
print(numeros[2])

#Reasignación
numeros[3]= 35
print(numeros)

#Agregamos en nuevo valor 
numeros.append(60)
print(numeros)

#Eliminamos en valor en el arreglo
numeros.remove(35)
print(numeros)

#Eliminamos un valor del arreglo usando posición 
numeros.pop(4)
print(numeros)

#ejemplop 2 de texto en futas
frutas = ["Manzana", "Fresa", "Sandia", "Mango", "Melon", "Platano"]
frutas.pop(4)
print(frutas)

#Eliminamos un elemneto del arreglo usando el nombre
frutas.remove("Manzana")
print(frutas)

#Declaracion de un arreglo vacio
arreglo = []

n = int(input("Ingrese el tamaño del arreglo"))
print(n)

for i in range(n):
    dato = int(input("Ingrese un numero"))
    arreglo.append(dato)

print("El arreglo es:", arreglo)


n = int(input("Ingrese el tamaño del arreglo"))

arreglo = [0] * n

for i in range(n):
    dato = int(input("Ingresa un numero: "))
    arreglo[i] = dato
 """



""" 
n = int(input("Ingrese el tamaño del arreglo"))
print(n) """


arreglo = []


for i in range(15):
    dato = int(input("Ingrese un numero"))
    arreglo.append(dato)

circuerizado = []

for i in range(15):
    dato = arreglo[i]
    while dato % 5 != 0:
        dato = dato + 1
    circuerizado.append(dato)

print("Array original: ", arreglo)
print("Array circuerizado:", circuerizado)



