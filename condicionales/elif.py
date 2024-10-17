ingreso_mensual = 12000
gasto_mensual = 13000

#if anidados y else if (elif)

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("Estas en deficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("Estas bien pa")
    else:
        print("y pa, estas gastando una bada")
elif ingreso_mensual > 1000: #se usa para
    print("Estas bien economicamente en tu ciudad")
else:
    print("Sos pobre")