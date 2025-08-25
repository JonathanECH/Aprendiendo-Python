#lista te numeros
numeros = [2,9,12,31,23,4,1,6,14]

#función max() lo que hace es que busca el numero mayor
numero_mayor = max(numeros)
print(f"El numero mayor es: {numero_mayor}")

#función min() lo que hace es que busca el numero menor
numero_menor = min(numeros)
print(f"El numero manor es: {numero_menor}")

#función round() esto lo que hace es que redonde el numero
numero = round(21.72384) #En este caso lo redondea a 22 porque es el numero mas cercano

print(f"Numero redondiado: {numero}")

#Esto lo que hace es que en numero mantenga 2 decimales
numero2 = round(21.72384, 2) #En este caso el numero mantiene los primeros 2 decimales pero si quieres más o menos decimales lo puedes controlas con el numero despues de la coma
print(f"Numero redondiado con solo dos decimales: {numero}")

#funcicón bool retonar False -> 0 , vacio, none , False \ True -> cualquier numero distinto de 0, True, cadenas etc.
resultado_bool = bool([12,31])

print(f"Resulado de la función bool: {resultado_bool}")
