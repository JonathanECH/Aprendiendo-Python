#Promedio de duración
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
este_curso = 1.5

#Duración crudo
crudo_promedio = 5
crudo_este_video = 3.5

#diferencias de duración
difernecia_con_min = 100 - (este_curso / otros_cursos_min * 100)
difernecia_con_max = 100 - (este_curso / otros_cursos_max * 100)
difernecia_con_promedio = 100 - (este_curso / otros_cursos_promedio * 100)

#Calculo el piempo vacio removido
tiempo_vacio_otros = 100 - (otros_cursos_promedio / crudo_promedio * 100)
tiempo_vacio_este = 100 - (este_curso / crudo_este_video * 100)

print("---------------------")
#Diferencia de duracion (ejercicio A)
print("El curso de Dalto dura:")
print(f" - un {difernecia_con_min}% menos que es mas rapido")
print(f" - un {round(difernecia_con_max , 1)}% menos que es mas lento")#round(num,2) esto lo que hacen es que redondea el numero a dos decimales
print(f" - un {difernecia_con_promedio}% menos que el promedio")
print("---------------------")

#Diferencia de crudo (ejercicio B)
print(f"Un curso promedio elimina un {tiempo_vacio_otros}% de tiempo vacio")
print(f"Este curso elimina un {round(tiempo_vacio_este,1)}% de tiempo vacio")
print("---------------------")

#Mostrar la diferencia si los cursos duraran 10 horas (ejercicio C)
print(f"Ver 10 horas de este curso equivale a ver {round((otros_cursos_promedio / este_curso * 10) , 1)} horas de otros cursos")
print(f"Ver 10 horas de otros curso equivale a ver {round((este_curso / otros_cursos_promedio * 10) , 1)} horas de este curso")
print("---------------------")