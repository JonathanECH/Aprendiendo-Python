#Creando las listas
frutas = ["manzana", "banana", "naranja", "pera", "uva", "sandía", "kiwi", "mango", "piña", "cereza"]
cadena = "Hello world"
numeros = [9,4,2,5,6,1]
#Se come todas las frutas
for fruta in frutas:
    print(f"Me voy a comer una: {fruta}")

print("-----------------------")
#Evitando que se coma un kiwi con la sentecia "continue"
for fruta in frutas:
    if fruta == "kiwi" :
        continue
    print(f"Me voy a comer una: {fruta}")


print("-----------------------")
#Evitando que el bucle se siga ejecutando cuando se coma la sandía elselse no se ejecuta tampoco
for fruta in frutas:
    print(f"Me voy a comer una: {fruta}")
    
    if fruta == "sandía" :
        break
else:
    print("fin del bucle")

print("-----------------------")
#Recoriendo una cadena de texto
for letra in cadena:
    print(letra)


print("-----------------------")
#For en una linea de codigo (duplicamos los numeros)
numertos_duplicados = [x*2 for x in numeros]

print(numertos_duplicados)