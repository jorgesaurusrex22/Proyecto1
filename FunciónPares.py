num=[]

def numeros(Numero):
    for i in range(5):
        while True:
            try:
                print('Ingrese un número')
                Numero=int(input())
                break
            except ValueError:
                print('Debe poner un número entero')
        num.append(Numero)

def impresionNumeros(numer):
    for i in range(5):
        print(str(numer[i]))
def numerosPares(numPar):
    contPar=0
    acPar=0
    for i in range(5):
        if numPar[i]%2==0:
            contPar=contPar+1
            acPar=acPar+numPar[i]
    if contPar!=0:
        print('Hay ' + str(contPar) + ' Número pares')
        print('Y en total suman '+str(acPar))
    else:
        if contPar<=0:
            print('No hay números pares')
def numeroImpares(numImp):
    contImp=0
    acImp=0
    for i in range(5):
        if numImp[i]%2!=0:
            contImp=contImp+1
            acImp=acImp+numImp[i]
    if contImp!=0:
        print('Hay '+str(contImp)+' Números impares')
        print('Y en total suman '+str(acImp))
    else:
        print('No hay números impares')
def numerosPositivos(numPos):
    contPos=0
    acPos=0
    for i in range(5):
        if numPos[i]>=0:
            contPos=contPos+1
            acPos=acPos+numPos[i]
    if contPos!=0:
        print('Hay '+str(contPos)+' números positivos')
        print('Y en total hay '+str(acPos))
    else:
        print('No hay números positivos')
numeros(num)
impresionNumeros(num)
numerosPares(num)
numeroImpares(num)
numerosPositivos(num)
