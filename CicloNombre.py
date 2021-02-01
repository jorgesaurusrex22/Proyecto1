print('¿Cuántos nombres quieres poner?')
cantidad=int(input())
acNom=""
for i in range(cantidad):
    print("Ingrese un nombre")
    nombre=input()
    acNom=acNom+" \n "+nombre
print(acNom)