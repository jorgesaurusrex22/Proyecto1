cantidad=0
while True:
    try:
        print('¿Cuántas notas quiere poner?')
        cantidad = int(input())
        break
    except ValueError:
        print('Debe poner un número entero')
print('Primero que nada, su nombre')
Nombre=input()
Suma=0
Notas=[]
for i in range(cantidad):
    while True:
        try:
            print('Dame la Nota ' + str(i+1) + ':')
            nota = int(input())
            break
        except ValueError:
            print('Debe poner un número entero')
    Notas.append(nota)
    Suma = Suma + nota


Promedio=Suma/cantidad
for i in range(cantidad):
    if Notas[i]>=40:
        print('Señor '+Nombre+' Su promedio es '+str(Notas[i])+' por lo tanto usted aprobó')
    else:
        print('Señor '+Nombre+' Su promedio es '+str(Notas[i])+' por lo tanto usted reprobó')
print(Promedio)