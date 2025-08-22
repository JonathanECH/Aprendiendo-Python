#Pedir un dato al usuario
nombre = input("Escribe tu nombre: ").capitalize() # capitalize es para mostrar solo la primera letra en mayuscula

#Mostrar nombre
print(f"Hola buenos dias {nombre}👋")

#Pedir un numero
numero = input("Ingresa un numero:")

#convierto el numero en entero y lo multiplico por dos
#resultado = int(numero) * 2

#convierto el numero en flotante y lo multiplico por dos
resultado = float(numero) * 2

#Muestro el numero multiplicado por dos
print(resultado)