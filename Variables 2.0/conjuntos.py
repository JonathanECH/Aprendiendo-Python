#creando un conjunto con (set)
conjunto = set(["Dato 1", "Dato 2"])

#Metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato 1", "dato 2"])
conjunto2 = {conjunto1, "dato 3"}
print(conjunto2)

#Teoria de conjuntos 
conjunto3 = {1,4,6,2,7}
conjunto4 = {4,7,1}

resultado = conjunto4.issubset(conjunto3) #Eso devuelve True porque todo lo que esta en 4 esta en 3
resultado = conjunto4 <= conjunto3 #Esto es otra forma de hacer exactamente lo mismo

resultado_2 = conjunto4.issuperset(conjunto3) #Eso devuelve False porque 3 no es un super conjunto del conjunto 4
resultado_2 = conjunto4 > conjunto3 #Esto es otra forma de hacer exactamente lo mismo


#Verificar si hay algun numero en comun
resultado_3 = conjunto3.isdisjoint(conjunto4) #Esto devuelve False si hay algun numero en comun
print(resultado_3)