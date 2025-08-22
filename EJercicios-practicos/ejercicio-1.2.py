frase = input("Dime una frase y te calculo cunto tardarias si tuvieras que decirla:")
palabras_separadas = frase.split(" ")
cantidad_de_palabras = len(palabras_separadas)
print(f"Dijiste {cantidad_de_palabras} y tardarias {cantidad_de_palabras/2} segundos en decirla")
print(f"Dalto lo diria en {round((cantidad_de_palabras/2*1.3), 1)} segundos en decirla")
if cantidad_de_palabras > 120:
    print("Qlq mano tampoco te pedi un testamento, pasao😒")