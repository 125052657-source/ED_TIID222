#Declarando un arreglo
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

frutas.remove("Manzana")
print(frutas)
