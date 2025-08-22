#creando diccionario con dict()
diccionario = dict(nombre="Manuel", apellido="Escalona")

#las listas no puieden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["dalto", "rancio"]) : "jajaj"}

#creando diccionarios con fromkeys() valor por defeto none
diccionario = dict.fromkeys(["Nombre", "Apellido"])

#creando diccionarios con fromkeys() cono dos parametros
diccionario = dict.fromkeys(["Nombre", "Apellido"] , "no se")
print(diccionario)