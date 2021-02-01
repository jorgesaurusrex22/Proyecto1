m=[]
f=3
c=2
for i in range(f):
    m.append([])
    for j in range(c):
        print('Introduce un Nombre en')
        Nombre=input()
        m[i].append(Nombre)

for i in range(f):
    for j in range(c):
        print(m[i][j],end=' ')
    print()