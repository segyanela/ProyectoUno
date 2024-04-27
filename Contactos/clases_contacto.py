class Persona:
    def __init__(self, apellido, nombre):
        self.apellido  = apellido
        self.nombre  = nombre

    def obtener_nombre_completo(self):
        return f"{self.apellido}, {self.nombre}"

class Contacto(Persona):
    def __init__(self, apellido, nombre, telefono, email):
        super().__init__(apellido, nombre)
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

    
    def imprimir_linea(self):
        print(f"{self.obtener_nombre_completo()}\t\t\t\t{self.telefono}\t\t\t\t{self.email}")

    
    def to_linea(self):
        return self.apellido.upper()+"-"+self.nombre.upper()+f"-{self.telefono}-{self.email}\n"
    
