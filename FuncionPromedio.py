nom=[]
not1=[]
not2=[]
not3=[]
prom=[]
def nombreYpromedio(Nombre,Nota1,Nota2,Nota3,Promedio):
    for i in range(2):
        while True:
            try:
                print('Ingrese su nombre')
                Nombre=input()
                print('Ingrese sus notas')
                Nota1=int(input())
                Nota2 = int(input())
                Nota3 = int(input())
                Promedio=(Nota1+Nota2+Nota3)/3
                break
            except ValueError:
                print('Debe poner un número válido')
        nom.append(Nombre)
        not1.append(Nota1)
        not2.append(Nota2)
        not3.append(Nota3)
        prom.append(Promedio)
    for i in range(2):
        print(nom[i]+' '+str(not1[i])+' '+str(not2[i])+' '+str(not3[i])+' '+str(prom[i]))
nombreYpromedio(nom,not1,not2,not3,prom)