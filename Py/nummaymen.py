num1 = int(input("ingrese el 1er nro: "))
num2 = int(input("ingrese el 2do nro: "))
num3 = int(input("ingrese el 3er nro: "))

masGrande=num1

if num1<num2:
    masGrande = num2
if num3 >masGrande:
    masGrande=num3

print("el  numero mas grande es: ", masGrande)
