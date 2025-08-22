cadena1 = "Hola Mundo"
cadena2 = "PythonEsGenial"
cadena3 = "Espacios al Inicio y al Final"
# print(dir(cadena1))  # (dir es un metodo) Muestra los atributos y métodos de cadena1

mayusc = cadena1.upper()  # Convierte cadena1 a mayúsculas

minusc = cadena1.lower()  # Convierte cadena1 a minúsculas

# Convierte la primera letra de cadena3 a mayúscula
primera_letra_mayuscula = (cadena3.capitalize()) 

# Busca la subcadena "genial" en cadena2, si no hay coincidencias devuelve -1
busqueda_find = cadena2.find("genial")  

# Busca la subcadena "Inicio" en cadena3, si no hay coincidencias lanza un error
busqueda_index = cadena3.index("Inicio")  

# Verifica si cadena1 es numérica, devuelve False porque contiene letras
es_numerico = cadena1.isnumeric()

# Verifica si cadena2 es alfanumérica, devuelve True porque tiene solo letras sin numeros
es_alfa_numerico = cadena2.isalpha()

# Cuenta el número de espacios en cadena3
contar_coincidencias = cadena3.count(" ")

# len es una funcion Cuenta el número de caracteres en cadena1
contar_caracteres = len(cadena1)

# Verifica si una cadena empieza con una cadena dada, si es asi devuelve True
empieza_con = cadena1.startswith("Hola")

# Verifica si una cadena termina con una cadena dada, si es asi devuelve True
termina_con = cadena1.endswith("o")

#Remplaza una cadena por otra
cadena_nueva = cadena2.replace("Python", "HMTL")

#Es una funcion especial que separa una cadenas con la cadena que pasemos y devuelve una lista
cadena_separada = cadena3.split(" ")
print(cadena_separada)