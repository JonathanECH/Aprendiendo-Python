animales = {"Loro", "Pero" , "Cocodrilo" , "Tiburon"}
numeros = { 6, 2, 12, 5}

#recorriendo la conjunto de animales
for animal in animales:
    print(f"Animal es igual a: {animal}")
    

print("--------------------")
#recorriendo la conjunto de numeros y multiplicando cada valor por 10
for numero in numeros:
    resultado = numero * 10
    print(f"El numero multiplicado por 10 es igual a: {resultado}")

print("--------------------")
#recoriendo dos conjunto al mismo tiempo
for animal,numero in zip(animales, numeros):
    print(f"conjunto 1: {animal}")
    print(f"conjunto 2: {numero}")
    

print("--------------------")
#Usando range() como forma de iterrar
for num in range(1,11): #El untimo numero no se cuenta, este for recorre desde el 1 hasta el 10 (sin contar al 11)
    print(num)

# print("--------------------")
#forma no optima de recorer una conjunto por su indice
# print("forma NO optima ❌:") Esto no fuciona con los conjuntos
# for num in range(len(numeros)):
#     print(f"Numero en el indice {num}: {numeros[num]}")
    

print("--------------------")
#forma optima de recorer una conjunto por su indice
print("forma optima ✅:")
for num in enumerate(numeros):
    indice = num[0]
    numer = num[1]
    print(f"Numero en el indice {indice}: {numer}")

print("--------------------")
#Usando el for/else
for numero in numeros:
    print(f"Ejecutando en ultimo bucle, valor actual: {numero}")
    
else: 
    print("El bucle termino")


#TODO LO ANTERIOR FUNCIONA EXATAMENTE IGUAL CON LAS TUPLAS Y CONJUNTOS