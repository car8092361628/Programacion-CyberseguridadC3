class automovil:
    def __init__(self,marca, modelo,color):
        """contructor de la clase automovil """
        self.marca= marca #atributo
        self.modelo= modelo # atributo
        self.color=color # atributos
        self.velocidad= 0 #inicialmente , el esta detenido
    
    def acelarar (self,  incremento ) :
        """metodo para aumentar la velocidad del automovil"""
        self.velocidad+=incremento
        return f"el {self.marca} {self.modelo} acelero a {self.velocidad} km/h"
    
    def frenar (self, decremento): 
        """metodo para diminuir la velocidad del automovil"""
        if self.velocidad -decremento <0:
            self.velocidad=0
        else:
            self.velocidad-=decremento
        return f"El {self.marca}{self.modelo} redujo su velocidad a {self.velocidad} km/h."
    
    def tocar_Bocina(self):
        """Metodo para hacer tocar la bocina"""
        return "!Beep Beep!"
           
    def mostrar_info(self):
        """Metodo para mostrar infomacion del automovil"""
        return f"Marca:{self.marca}, Modelo: {self.modelo}, Color: {self.color}, Velocidad : {self.velocidad} km/h."
    
# Crear el objeto Automovil

mi_auto=automovil("Toyota","Corolla","Rojo") 
print(mi_auto.mostrar_info()) 

#acelerar el automovil  
print(mi_auto.acelarar(50))   

#Frenar el automovil
print(mi_auto.frenar(20)) 

#Tocar Bocina
print(mi_auto.tocar_Bocina())

#mostrar informacion
print(mi_auto.mostrar_info())
  