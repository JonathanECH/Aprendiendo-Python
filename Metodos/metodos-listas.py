#Creando una lista con list
lista = list(["Hola", 34, 21])

#Devuelve la cantidad de es=lentos que hay en la lista
cantidad_elementos = len(lista)

#Agregando elementos a una lista
lista.append(False)

#Agregando un elemento en un indice espesifico
lista.insert(2, 1.75) #En el indice 2 se agrega en 1.75

#Agregando varios elementos a la lista
lista.extend([True, 2025])

#Eliminando un elemento de la lista por su indice
lista.pop(0)#Elimino el primer elemento que es el indice 0

# lista.pop(-1) -> esto elimina el ultimo elemento de la lista, -2 para eliminar el anteultimo, y asi sucesivamente

#Eliminando un elemento de la lista por su valor
lista.remove(2025)

#Eliminando todos los elementos de la lista
#lista.clear()

#Organizando la lista de menor a mayor (si usamos el parametro reverse=True lo ordena en reversa de mayor a menor)
lista.sort()

#Invirtiendo los elementos de una lista
lista.reverse()

#Verificando si un elemento se encuentra en la lista
elemento_buscado = lista.index(21)# index busca si un elemento es igual a alguno de la lista, si no lo consigue da un error

cantidad_de_elementos = len(lista)
print(f"Lista: {lista}")
print(f"Cantidad: {cantidad_elementos}")
print(f"Elemento encontrado en el indice: {elemento_buscado}")