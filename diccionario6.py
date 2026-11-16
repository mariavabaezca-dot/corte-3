estudiantes=[]
cantidad = int(input("cantidad de estudiantes:"))

for i in range(cantidad):
    estudiante = {}
    estudiante["nombre"]= input("nombre: ")
    estudiante["promedio"]=float(input("promedio: "))
    estudiantes.append(estudiante)

mejor =estudiantes[0]
for estudiante in estudiantes:
    print(estudiante)

for estudiante in estudiantes:
    if estudiante["promedio"]>mejor["promedio"]:
        mejor=estudiante

print("mejor estudiante:",mejor["nombre"])
print("promedio:",mejor["promedio"])            
