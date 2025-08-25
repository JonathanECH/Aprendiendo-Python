#creando diccionario con dict()
diccionario = dict(nombre="Manuel", apellido="Escalona")

#las listas no puieden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["dalto", "rancio"]) : "jajaj"}

#creando diccionarios con fromkeys() valor por defecto: none
diccionario = dict.fromkeys(["Nombre", "Apellido"])

#creando diccionarios con fromkeys() con dos parametros con el valor: any value
diccionario = dict.fromkeys(["Nombre", "Apellido"] , "Any value")
print(diccionario)