sueldo_mensual = 1200
gasto_mensual = 600
#if anidados y elif
if sueldo_mensual > 1000:
    if sueldo_mensual - gasto_mensual > 500:
        print("Eres un trabajador con un buen sueldo, pero tienes gastos altos")
    else:
        print("Eres un trabajador con un buen sueldo y gastos bajos")
    
elif sueldo_mensual >= 500:
    print("Tienes un sueldo medio")
else:
    print("Tienes un sueldo bajo")