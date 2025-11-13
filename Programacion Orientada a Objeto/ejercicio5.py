class Persona:
    def __init__(self,nombre,edad):
        self.__nombre=nombre
        self.__edad=edad
    
    @property
    def edad (self):
        return self.__edad 
    
    @edad.setter
    def edad(self,valor):
        if valor >=0:
            self.__edad=valor
        else:
            raise ValueError("La edad no puede ser negativa.")    
    
persona=Persona("carlos",25)  
print(persona.edad) #getter

persona.edad=30 #setter
print(persona.edad)
    