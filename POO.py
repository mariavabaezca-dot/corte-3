class libro:
    def __init__(self, codigo, titulo,autor):
        self.codigo=codigo
        self.titulo=titulo
        self.autor=autor
        self.disponible=True
    def prestar_libros_disp(self):
        if self.disponible:
            self.disponible=False
            return True
        return False
    def devolver_libros_pres(self):
        if not self.disponible:
            self.disponible=True
            return True
        return False
class usuario:
    def __init__(self,nombre,identificacion_persona):
        self.nombre=nombre 
        self.identificacion_persona = identificacion_persona
        self.libros_prest=[]
class biblioteca:
    def __init__(self):
        self.libros=[]
        self.usuarios=[]
    def buscar_libro_a_prestarrr(self,codigo):
        for libro in self.libros:
            if libro.codigo == codigo:
                return libro
        return None
    def buscar_a_usuario(self,identificacion):
        for usuario in self.usuarios:
            if usuario.identificacion_persona== identificacion:
                return usuario
        return None
    def regitrando_libro(self,libro):
        if self.buscar_libro_a_prestarrr(libro.codigo)is None:
            self.libros.append(libro)
            return True
        return False
    def registrar_usuar(self,usuario):
        if self.buscar_a_usuario(usuario.identificacion_persona) is None :
            self.usuarios.append(usuario)
            return True
        return False
    def prestarlib(self,codigo,identificacion):
        libro = self.buscar_libro_a_prestarrr(codigo)
        usuario = self.buscar_a_usuario(identificacion)
        if libro is None or usuario is None:
            return False
        if libro.prestar_libros_disp():
            usuario.libros_prest.append(codigo)
            return True
        return  False
    def devol_libros(self, codigo,identificacion):
        libro = self.buscar_libro_a_prestarrr(codigo)
        usuario= self.buscar_a_usuario(identificacion)
        if libro is None or usuario is  None :
            return False
        if codigo in usuario.libros_prest:
            libro.devolver_libros_pres()
            usuario.libros_prest.remove(codigo)
            return True
        return False
    def cons_disp(self):
        print("los libros disponibles del la biblioteca de la universidad sonn:")
        for libro in self.libros:
            if libro.disponible:
                print(libro.codigo,"-",libro.titulo,"-","del autor",libro.autor)
ecci_biblioteca=biblioteca()
libro1=libro("cod1","Don Quijote de la Mancha","Miguel de Cervantes")
libro2=libro("cod2","Orgullo y prejuicio","Jane Austen") 
libro3=libro("cod3","Fahrenheit 451","Ray Bradbury") 
libro4=libro("cod4","dune","Frank Herbert")     
usuario1=usuario("rosalinda perez","1028887477")
ecci_biblioteca.regitrando_libro(libro1)
ecci_biblioteca.regitrando_libro(libro2)
ecci_biblioteca.regitrando_libro(libro3)
ecci_biblioteca.regitrando_libro(libro4)
ecci_biblioteca.registrar_usuar(usuario1)
if ecci_biblioteca.prestarlib("cod4","1028887477"):
    print("se registro el prestamo del libro de la biblioteca")
else: 
    print("no se puede prestar el libro porque alguien mas lo tiene")
ecci_biblioteca.cons_disp()
if ecci_biblioteca.devol_libros("cod4","1028887477"):
    print("el libro se devolvió")
else:
    print("no se puede devolver el librp")
ecci_biblioteca.cons_disp()


        

        
            
            