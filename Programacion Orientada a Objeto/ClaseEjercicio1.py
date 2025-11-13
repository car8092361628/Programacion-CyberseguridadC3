class Profesion:
    def inicializar(self, Titulo, Experiencia, Empresa):
        self.titulo = Titulo
        self.experiencia = Experiencia
        self.empresa = Empresa
        
    def mostrar_profesion(self):
        print(f"Título: {self.titulo}")
        print(f"Experiencia: {self.experiencia} años")
        print(f"Empresa: {self.empresa}")

class Persona:
    # Constructor de la clase Atributos o (características)
    def inicializar(self, Nombre, Edad, Altura, Peso):#funcion que recibe parametros
        self.nombre = Nombre
        self.edad = Edad
        self.altura = Altura
        self.peso= Peso
        
        
    def Imprimir(self):
            print(f"Nombre: {self.nombre}") 
            print(f"Edad: {self.edad}")
            print(f"Altura: {self.altura}")
            print(f"Peso: {self.peso}")
            
            
     # Método de la clase (acciones o comportamientos)       
     # Crear objeto de la clase Persona
     
persona1 = Persona() # Crear instancia de la clase Persona
persona1.inicializar("Juan", 30, 1.75, 70) # Inicializar atributos o características
persona1.Imprimir() # Llamar al método imprimir para mostrar los datos  

profesion1 = Profesion() # Crear instancia de la clase Profesion
profesion1.inicializar("Ingeniero de Software", 5, "Tech Solutions")
profesion1.mostrar_profesion() # Llamar al método mostrar_profesion para mostrar los datos  




            
            