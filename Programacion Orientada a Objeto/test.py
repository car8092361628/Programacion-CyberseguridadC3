class Automovil:
    def __init__(self, marca, modelo, color):
        """Constructor de la clase Automovil"""
        self.marca = marca   # Atributo
        self.modelo = modelo  # Atributo
        self.color = color   # Atributo
        self.velocidad = 0   # Inicialmente, el auto está detenido

    def acelerar(self, incremento):
        """Método para aumentar la velocidad del automóvil"""
        self.velocidad += incremento
        return f"El {self.marca} {self.modelo} aceleró a {self.velocidad} km/h."

    def frenar(self, decremento):
        """Método para disminuir la velocidad del automóvil"""
        if self.velocidad - decremento < 0:
            self.velocidad = 0
        else:
            self.velocidad -= decremento
        return f"El {self.marca} {self.modelo} redujo su velocidad a {self.velocidad} km/h."

    def tocar_bocina(self):
        """Método para hacer sonar la bocina"""
        return "¡Beep Beep! 🚗"

    def mostrar_info(self):
        """Método para mostrar información del automóvil"""
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}, Velocidad: {self.velocidad} km/h"

# Crear un objeto Automovil
mi_auto = Automovil("Toyota", "Corolla", "Rojo")

# Mostrar información del automóvil
print(mi_auto.mostrar_info())

# Acelerar el automóvil
print(mi_auto.acelerar(50))  

# Frenar el automóvil
print(mi_auto.frenar(20))

# Tocar la bocina
print(mi_auto.tocar_bocina())

# Mostrar información después de acelerar y frenar
print(mi_auto.mostrar_info())
