nombre = input("ingrese su nombre completo")
edad = int(input("digite su edad"))
estatura = float(input("digite su estatura en metros"))
ciudad = input("digite la ciudad en la que vive")
nombre_mayusculas = nombre.upper()
caracteres_cant = len(nombre)
if edad < 18:
    clasificacion = "menor de edad"
else:
    if edad < 60:
        clasificacion= "Adulta"
    else:
        clasificacion ="Adulta mayor"
if edad % 2==0:
    tipo_edad = "par"
else:
    tipo_edad="impar"
print(tipo_edad)
print("\n--- RESULTADOS DEL PUNTO 1 ---")
print(f"nombre:{nombre_mayusculas}")
print(f"cantidad de caracteres:{caracteres_cant}")
print(f"la estatura:{estatura} metros")
print(f"edad:{edad} años")
print(f"clasificacion:{clasificacion}")
print(f"la ciudad es:{ciudad}")
print(f"el tipo de edad es:{tipo_edad}")
###punto2
cantidad=int(input("cuantos numeros desea ingresar:"))
while cantidad < 1:
    print("error ingrese una cantidad que supere al 0:")
    cantidad= int(input("cuantos numeros desea ingresar"))
numeros = []
for i in range(cantidad):
    numero = float(input(f"ingrese el numero{i+1}:"))
    numeros.append(numero)
def calcular_suma(lista):
    suma = 0
    for numero in lista:
        suma = suma + numero
    return suma
def calcular_promedio(lista):
    promedio= calcular_suma(lista)/len(lista)
    return promedio
def encontrar_may(lista):
    mayor = lista[0]
    for numero in lista:
        if numero > mayor:
            mayor = numero
    return mayor
def encontrar_men(lista):
    menor =lista[0]
    for numero in lista:
        if numero <menor:
            menor = numero
            return menor
def contar_imp_par(lista):
    pares=0
    impares=0
    for numero in lista:
        if numero % 2 ==0:
            pares = pares + 1
        else:
            impares= impares +1
    return pares,impares

def obtener_positivos(lista):  
    positivos=[]
    for numero in lista :
        if numero >0:
            positivos.append(numero)
    return positivos
def obtener_unicos(lista):
    unicos=set(lista)
    return unicos  
suma=calcular_suma(numeros)
promedio=calcular_promedio(numeros)
mayor=encontrar_may(numeros)
menor=encontrar_men(numeros)
pares,impares=contar_imp_par(numeros)
positivos=obtener_positivos(numeros)
unicos=obtener_unicos(numeros)
print("punto__2")
print("numeros ingresados:",numeros)
print("la suma de los numeros son :",suma)
print("el promedio es:",promedio)
print("el numero mayor es:",mayor)
print("el numero menor es",menor)
print("los numeros pares son:",pares)
print("los numeros impares son",impares)
print("los numeros positivos son",positivos)
print("los valores unicos son:",unicos)
###punto3
texto=input("ingrese una frase o palabra para invertirla:")
def invertir_tex(palabra):
    if len(palabra)<=1:
        return palabra
    else:
        return invertir_tex(palabra[1:])+palabra[0]
invertido = invertir_tex(texto)
print("punto___3_texto_invertido")
print("texto original",texto)
print("texto invertido",invertido) 
limpio=texto.lower().replace("","")
texto_inv=invertir_tex(limpio)
if limpio ==texto_inv:
    print("el texto es un palidromo")
else:
    print("el texto no es un palidromo")
vocales=0
for letra in texto.lower():
    if letra in "aeiouáéíóú":
        vocales=vocales+1
print("vocales")
print("la cantidad de vocales es:",vocales)
resultado=texto,invertido,vocales
print("_-los resultados son-___")
print(resultado)
#punto4
estudiantes=[]
for i in range (3):
    print(f"-----registro estudiante-----{i+1}-------")
    nombre=input("ingrese el nombre del estudiante:)")
    codigo=input("ingrese el codigo institucional:")
    notas=[]
    for j in range(3):
        nota=float(input(f"ingrese la nota{j+1}"))
        while nota <0 or nota >5:
            print("no se pueden colocar valores fuera del rango(0.0 y 5.0)")
            nota=float(input(f"ingrese otravez la nota{j+1}"))
        notas.append(nota)
    estudiante = {"nombre": nombre, "codigo": codigo,"notas": notas}
    estudiantes.append(estudiante)
def promedio_calcular(notas):
    suma =0
    for nota in notas:
        suma =suma+nota
    res =suma/len(notas)
    return res
for estudiante in estudiantes:
    res=promedio_calcular(estudiante["notas"])
    estudiante["promedio"]=res
    if res >=3.0:
        estudiante["estado"]="aprobado"
    else:
        estudiante["estado"]="reprobado"
for estudiante in estudiantes:
    print("\nNombre:", estudiante["nombre"])
    print("Codigo:", estudiante["codigo"])
    print("Notas:", estudiante["notas"])
    print("Promedio:", round(estudiante["promedio"], 2))
    print("Estado:", estudiante["estado"])
#punto 5
grupo_python = ["Ana", "Luis", "Carlos", "Sofia", "Mateo"]
grupo_datos = ["Sofia", "Mateo", "Laura", "Ana", "Daniel"]
python=set(grupo_python)
datos=set(grupo_datos)
grupos=python & datos
print("estudiantes que estan en los 2 grupos")
print(grupos)
solo_p=python-datos
print("estudiantes que solo estan en el grupo de pyton")
print(solo_p)
solo_d=datos-python 
print("estudiantes que solo estan en datos")
print(solo_d)
todos=python|datos
print("total de los estudiantes diferentes")
print (len(todos))
lista=sorted(todos)
print("lista alfabeticamente de los estudiantes")
print(lista)
grupos_t={}
for alumno in todos:
    cantidad =0
    if alumno in python:
        cantidad=cantidad+1
    if alumno in datos:
            cantidad=cantidad+1
    grupos_t[alumno]=cantidad
print("cantidad grupo por estudiantes")    
for alumno in lista:
    print(alumno,"pertenece a:",grupos_t[alumno],"grupos")
    #punto6
inventario = [{"codigo": "P01", "nombre": "Mouse", "precio": 45000, "cantidad": 10},{"codigo": "P02", "nombre": "Teclado", "precio": 80000, "cantidad": 3},{"codigo": "P03", "nombre": "Memoria USB", "precio": 35000, "cantidad": 4}]
for producto in inventario:
    if producto["precio"] < 0:
        print("El precio no puede ser negativo")
    if producto["cantidad"] < 0:
        print("La cantidad no puede ser negativa")
def mostrar(inventario):
    print("el inventario de produtos")
    for producto in inventario:
        print("el codigo es:",producto["codigo"])
        print("el nombre es :",producto["nombre"])
        print("el precio es:",producto["precio"])
        print("la cantidad es:",producto["cantidad"])
def buscar(inventario):
    codigo=input("ingrese el codigo del producto que comprara:")
    encontrado = False
    
    for producto in inventario:
        if producto["codigo"].lower()==codigo.lower():
            print("el producto esssssss")
            print("el nombre es :",producto["nombre"])
            print("el precio es:",producto["precio"])
            print("la cantidad es:",producto["cantidad"])
            encontrado=True
    if encontrado== False:
        print("el producto no existe")
def total(inventario):
    total_inv=0
    for producto in inventario:
        valor =producto["precio"]*producto["cantidad"]
        total_inv = total_inv+ valor
    return total_inv
opcion =0
while opcion!=5:
    print("menu inv")
    print("1. Mostrar inventario")
    print("2. Buscar producto por codigo")
    print("3. Calcular valor total del inventario")
    print("4. Mostrar productos con cantidad menor que 5")
    print("5. Salir")        
    opcion=int(input("seleccione una opcion:)"))
    if opcion ==1:
        mostrar(inventario)
    else:
        if opcion==2:
            buscar(inventario)
        else:
            if opcion==3:
                resul= total (inventario)
                print("el total del inv es:",resul)
            else:
                if opcion==4:
                    print("produc menores a 5")
                    for producto in inventario:
                        if producto["cantidad"]<5:
                            print("el nombre es :",producto["nombre"])
                            print("el precio es:",producto["precio"])
                            print("la cantidad es:",producto["cantidad"])
                else:
                    if opcion==5:
                        print("graciasss por utilizar este software de inventario")
                    else:
                        print("opcion incorrecta")
codigos=set()
for producto in inventario:
    codigos.add(producto["codigo"])
print("son estos los codigos diferentes:",len(codigos))                                    
                                
                             
                            
                        
                      