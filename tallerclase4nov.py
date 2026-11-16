###punto1
producto={"codigo":101,"nombre":"cuaderno","precio":154500,"stock":21}
print("datos del producto.........")
print("el codigo es :",producto["codigo"])
print("el nombre del producto es:",producto["nombre"])
print("el precio es:",producto["precio"])
print("el stock es:",producto["stock"])

#####punto2
inventario={101:"kit_maquillaje",102:"kit_skincare,",103:"kit_niños"}
codigo=int(input("ingrese el codigo del producto que quiera:"))
if codigo in inventario:
    print("el producto existe en el inventario:)")
    print("nombre del producto:",inventario[codigo])
else:
    print("el codigo no existe") 
#####punto3
notas={"matematicas":4.5,"estadistica":4.0,"programacion":3.9,"contabilidad":4.2,"ingles":4.5}
promedio=sum(notas.values())/len(notas)
print("notas estudianteee:)") 
for materia,nota in notas.items():
    print(materia,":",nota)
print("el promedio del estudiante es:",promedio)    
##punto4
lista_alumnos=[{"nombre":"maria","promedio":4.5},{"nombre":"juan","promedio":2.9},{"nombre":"andrea","promedio":2.5},{"nombre":"carlos","promedio":2.9},{"nombre":"andres","promedio":3.5}]
print("estudiantes aprobados")
for alumno in lista_alumnos:
    if alumno["promedio"]>=3.0:
        print("nombre:",alumno["nombre"])
        print("promedio:",alumno["promedio"])
##punto 5
def calcular_inv(articulo):
    totalinv = articulo["precio"] * articulo["stock"]
    return totalinv
articulo= {"codigo":107,"nombre":"juegos de mesa","precio":500000,"stock":33}
valor_total=calcular_inv(articulo)
print("el producto es :",articulo["nombre"])
print("el precio es :",articulo["precio"])
print("en el stock estan :",articulo["stock"])
print("valor total del inventario:",valor_total)        




       
     