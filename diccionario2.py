estudiante = {}
estudiante["nombre"] = input("Nombre: ")
estudiante["edad"] = int(input("Edad: "))
estudiante["programa"] = input("Programa: ")
estudiante["promedio"] = float(input("Promedio: "))
for clave, valor in estudiante.items():
 print(f"{clave}: {valor}")
promedio = estudiante[ "promedio"]

if promedio >= 3.0:
    estudiante["estado"] = "aprobado"
else:
    estudiante["estado"] = "reprobado"
    
    
print(estudiante.get("estado"))