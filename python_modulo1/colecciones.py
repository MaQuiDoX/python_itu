import math

print("Agregar elemento")
'''
Crea una función que reciba una lista, solicite al usuario agregar un número y lo agregue a la lista
'''

def addNumber(list):
    num = int(input("Ingrese un número para añadir a la lista: "))
    list.append(num)
    return list

list1 = [1,2,3]

print(list1)

addNumber(list1)

print(list1)


print("")
print("Promedio")
'''
Crea una función que reciba una lista de números y retorne el promedio.
'''

def averageList(list):
    average = sum(list) / len(list)
    return average

list2 = [1,2,3,4,5,6,7,8]

average = averageList(list2)

print("El promedio de todos los numeros de la lista es de: ", average)


print("")
print("Compara")
'''
Crea una función que reciba dos listas y retorne si ambas comienzan por el mismo elemento.
'''

def compareList(list1, list2):
    if list1[0] == list2[0]:
        return True
    else:
        return False

list3a = [1,2,3]
list3b = [2,3,4]
list3c = [1,5,6]

print("Lista A y lista B: ", compareList(list3a, list3b))
print("Lista A y lista C: ", compareList(list3a, list3c))


print("")
print("Distancia entre dos puntos")
'''
Crea una funcion que reciba 2 tuplas de 2 elementos (punto 1 y punto 2) y retorne la distancia entre los dos puntos (investiga la formula)
'''

def distanceTupla(tupla1, tupla2):
    distance = math.sqrt(((tupla2[0] - tupla1[0]) ** 2) + ((tupla2[1] - tupla1[1]) ** 2))
    return distance

tupla1 = (1,5)
tupla2 = (3,9)

print("Las distancias entre las tuplas 1 y 2 es de: ", distanceTupla(tupla1, tupla2))


print("")
print("Modifica indirectamente una tupla")
'''
Crea una función que reciba una tupla, una posición y un valor y retorne una tupla igual a la recibida pero cambiando el valor en la posición enviada por el valor pasado por parámetro.
'''

def tupleModifier(tupla, position, value):
    listTupla = list(tupla)
    listTupla[position] = value
    modifiedTupla = tuple(listTupla)
    return modifiedTupla


tupla3 = (1,2)
print(tupla3)

tupla4 = tupleModifier(tupla3, 0, 3)
print(tupla4)


print("")
print("Solicitar datos al usuario")
'''
Crea una función que solicite al usuario nombre, apellido e email y retorne un diccionario con los datos.
'''

def userData():
    username = input("Ingrese el nombre del usuario: ")
    userlastname = input("Ingrese el apellido del usuario: ")
    usermail = input("Ingrese el mail del usuario: ")

    dictionary = {'name': username, 'lastname': userlastname, 'mail': usermail}
    return dictionary

newdict = userData()

print("")
print("Nombre de usuario: ", newdict['name'])
print("Apellido de usuario: ", newdict['lastname'])
print("Mail del usuario: ", newdict['mail'])


print("")
print("Conjuntos disjuntos")
'''
Escribe una función que reciba dos sets y retorne si son o no disjuntos.'
'''

def setDisjoint(set1, set2):
    return not bool(set1 & set2)

set1 = {1,2,3,4,5}
set2 = {6,7,8,9,10}
set3 = {1,11,22}

print("Conjuntos disjuntos setA y setB: ", setDisjoint(set1, set2))
print("Conjuntos disjuntos setA y setC: ", setDisjoint(set1, set3))
