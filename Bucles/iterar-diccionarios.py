diccionario = {
    "nombre" : "Juan",
    "apellido" : "Colinas",
    "edad" : 21
}
#Recorriendo el diccionaro para obtener las claves/keys (pero no los valores/values)
for dato in diccionario:
    print(dato)


#Recorriendo el diccionaro con items() para obetener la clave y el valor
for dato in diccionario.items():
    key = dato[0]
    value = dato[1]
    print(f"Las clave es: {key} y el dato es: {value}")