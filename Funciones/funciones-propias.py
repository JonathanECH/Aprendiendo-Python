#funcion sin parametros
def saludo_simple():
    print("Hello, good morning")

saludo_simple()

#funcion con parametros
def saludo(nombre, sexo):
    sexo = sexo.lower()
    if sexo == "hombre":
        adjetivo = "hermano"
        print(f"Hola, {nombre} como estas mi {adjetivo}?")
    elif sexo == "mujer":
        adjetivo = "reina"
        print(f"Hola, {nombre} como estas mi {adjetivo}?")
    else:
        adjetivo = "mausa"
        print(f"Hola, {nombre} como estas mi {adjetivo}?")

saludo("Jose", "hombre")
saludo("Sofia", "mujer")
saludo("Frank", "")

# creando una función que nos retorne un valor
def contraseña_random(num):
    chars = "abcdefghijklmnopqrstuvwxyz"
    numero_entero = str(num) #esta funcion convierte los elementos a texto
    num = int(numero_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 4
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña,num
#desempaquetando la función 
password,primer_numero = contraseña_random(90)

#mostardo los resultados obtenidos y los datos utilizados
print(f"Contraseña generada: {password}")
print(f"El numero utilizdo para generarla fue: {primer_numero}")

# #Esta es una función que hice pero es mas tractico usar la función max()
#Encontrando el numero mayor de una lista
def encontra_numero_mayor(list):
    numero_mayor = list[0]
    for num in list:
        if num > numero_mayor:
            numero_mayor = num
    
    return numero_mayor

# major_number = encontra_numero_mayor(numeros)

# print(major_number)