estudiante={"nombre": "maria","promedio":4.8}



def mostrar_estudiante (estudiante):
    print("nombre:",estudiante["nombre"])
    print("promedio:",estudiante["promedio"])
def aprobo(estudiante):
    return estudiante ["promedio"] >= 3.0
mostrar_estudiante(estudiante)
print("aprobo:",aprobo(estudiante))    