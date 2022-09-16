
#***Solución momento evaluativo***
# 1.Construir un programa que permita ingresar 20 números enteros y cuente cuantos números negativos fueron ingresados (+1)
print("Programa para contar números negativos enteros")
numeroentero = 1
negativos = 0
positivos = 0
while (numeroentero<=3):
    n = int(input(f'Ingresa el número : '))
    if(n<0):
        negativos+=1
    else:
        positivos+=1
    numeroentero+=1
print(f'{negativos} son los números negativos')