numPar =0
numImp =0

num= int(input("introduce un numero o escriba 0 para salir: "))

while num!= 0 :
    if num % 2 ==0:
        numPar +=1
    else:
        numImp+=1
    num= int(input("ingrese 0 para detener ejecucion o un numero para seguir"))


print("cantidad de numeros pares : ", numPar)
print("cantidad de numeros impares : ", numImp)
