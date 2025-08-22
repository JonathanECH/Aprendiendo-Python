diccionario = {
    "nombre" : "Miguel",
    "apellido" : "Colmenarez",
    "edad" : 21
}
#Nos devuelve un objeto dict_item
claves = diccionario.keys()

#obteniendo un elemento con get() (si no encuentra nada el programa continúa)
valor_de_cada_elemento = diccionario.get("edad")

#Eliminando todo del diccionario
#diccionario.clear()

#Eliminando un elemento del diccionario
diccionario.pop("nombre")

#obteniendo un elemento dict_item iterable
diccionario_iterable = diccionario.items()

print(diccionario)