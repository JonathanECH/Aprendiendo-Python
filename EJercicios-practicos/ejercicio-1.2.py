# Se le pide al usuario que ingrese una frase.
# La función 'input' lee lo que el usuario escribe y lo guarda en la variable 'frase'.
frase = input("Dime una frase y te calculo cuanto tardarias si tuvieras que decirla: ")

# Se separan las palabras de la frase.
# El método '.split(" ")' divide la cadena de texto 'frase' en una lista de subcadenas,
# usando el espacio (" ") como separador. Cada palabra se convierte en un elemento de la lista.
palabras_separadas = frase.split(" ")

# Se cuenta la cantidad de palabras.
# La función 'len' devuelve el número de elementos que hay en la lista 'palabras_separadas'.
cantidad_de_palabras = len(palabras_separadas)

# Se muestra al usuario la cantidad de palabras y el tiempo estimado para decirlas.
# Se asume que una persona normal dice 2 palabras por segundo.
# Se usa un f-string para insertar los valores de las variables directamente en la cadena de texto.
print(f"Dijiste {cantidad_de_palabras} palabras y tardarias {cantidad_de_palabras/2} segundos en decirla.")

# Se calcula y muestra el tiempo que tardaría "Dalto" (un personaje o una persona hipotética).
# Se asume que habla 30% más rápido (1.3) que una persona normal.
# 'round(..., 1)' redondea el resultado a un decimal.
print(f"Dalto lo diria en {round((cantidad_de_palabras/2*1.3), 1)} segundos.")

# Se evalúa si la cantidad de palabras es excesiva.
# Si la cantidad de palabras es mayor a 120, se imprime un mensaje de advertencia.
if cantidad_de_palabras > 120:
    print("Qlq mano tampoco te pedi un testamento, pasao😒")