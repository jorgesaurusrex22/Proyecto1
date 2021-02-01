cantidad=0
while True:
    try:
        print('¿Cuántas personas quiere poner?')
        cantidad = int(input())
        break
    except ValueError:
        print('Debe poner un número entero')
nom=[]
ed=[]
for i in range(cantidad):
    while True:
        try:
            print('Ingrese su nombre y edad')
            Nombre=input()
            Edad = int(input())
            nom.append(Nombre)
            ed.append(Edad)
            break
        except ValueError:
            print('Debe poner un número entero')
for i in range(cantidad):
    print('Nombre: '+nom[i]+' Edad: '+str(ed[i]))