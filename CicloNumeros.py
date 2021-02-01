print('¿Cuántos números quieres poner?')
veces=int(input())
contPar=0
contImp=0
acumPar=0
acumImp=0
for i in range(veces):

    print("---ciclo"+str(i+1)+"---")
    print("Ingrese un número")
    num=int(input())
    if num%2==0:
        contPar=contPar+1
        acumPar=acumPar+num
    else:
        contImp=contImp+1
        acumImp=acumImp+num

print("De numero pares hay ",contPar," Números y suman ",acumPar)
print("De numero impares hay ",contImp," Números y suman ",acumImp)
