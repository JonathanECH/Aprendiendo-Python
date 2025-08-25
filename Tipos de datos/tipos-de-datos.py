#Ejemplo de lista en Python (se pueden almacenar diferentes tipos de datos y modificar)
lista = ["Jose Colinas", 19, 1.75, True, "Python"]
#Esto es valido porque una lista puede contener diferentes tipos de datos
lista[0] = "Juan Perez"  # Modifica el primer elemento de la lista
print(f"lista: {lista[0]}")  # Imprime el elemento en la posición 1 de la lista

#Ejemplo de tupla en Python (no se pueden modificar) (son solo de lectura)
tupla = ("Jose Colinas", 19, 1.75, True, "Python")
#Esto no es valido
# tupla[0] = "Juan Manuel"  # Intento de modificar el primer elemento de la tupla
print(f"tupla: {tupla[0]}")  # Imprime el primer elemento de la tupla

#Ejemplo de conjunto en Python (set) (no se pueden acceder a los datos mediante el indice, no se pueden repetir elementos)
conjunto = {"Manuel Gomez", "Jose Colinas", 21, 1.65, False, "Python"}

# print(conjunto[1]) # No se puede acceder por índice en un conjunto

conjunto.add("Maria Lopez") # Agrega un nuevo elemento al conjunto
print(f"conjunto: {conjunto}")  # Imprime el conjunto completo

#Ejemplo de diccionario en Python (se pueden acceder a los datos mediante una clave)
diccionario = {
    "nombre" : "Jose Colinas",
    "edad" : 19,
    "altura" : 1.75,
    "es_estudiante" : True,
    "lenguaje" : "Python"
}
print(f"diccionario: {diccionario['lenguaje']}")  # Imprime el valor asociado a la clave 'lenguaje'