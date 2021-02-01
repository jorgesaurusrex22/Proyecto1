Nom=[]
def ImprimirNombre(Nombre):
    for i in range(5):
        print('Ingrese un Nombre')
        Nombre=input()
        Nom.append(Nombre)
    for i in range(5):
        print(Nom[i])
ImprimirNombre(Nom)