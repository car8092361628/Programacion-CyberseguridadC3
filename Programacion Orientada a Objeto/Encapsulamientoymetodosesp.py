class IntentoIntrusion:
    def __init__(self, ip_origen, severidad, tipo):
        """
        Método especial __init__:
        Constructor del objeto. Se ejecuta automáticamente al instanciar la clase.
        Aquí usamos atributos privados con '__' para aplicar encapsulamiento.
        """
        self.__ip_origen = ip_origen
        self.__severidad = severidad  # Escala de 1 a 10
        self.__tipo = tipo

    # ========== ENCAPSULAMIENTO: MÉTODOS GETTERS Y SETTERS ==========

    @property
    def ip_origen(self):
        """Getter: permite leer la IP de origen de forma segura."""
        return self.__ip_origen

    @ip_origen.setter
    def ip_origen(self, valor):
        """Setter: valida antes de modificar la IP."""
        if isinstance(valor, str) and len(valor.split(".")) == 4:
            self.__ip_origen = valor
        else:
            raise ValueError("Dirección IP inválida")

    @property
    def severidad(self):
        """Getter: devuelve el nivel de severidad"""
        return self.__severidad

    @severidad.setter
    def severidad(self, valor):
        """Setter: asegura que la severidad esté entre 1 y 10"""
        if 1 <= valor <= 10:
            self.__severidad = valor
        else:
            raise ValueError("La severidad debe estar entre 1 y 10")

    @property
    def tipo(self):
        """Getter: devuelve el tipo de ataque"""
        return self.__tipo

    # ========== MÉTODOS ESPECIALES ==========

    def __str__(self):
        """
        Se ejecuta al usar print(objeto)
        Devuelve una descripción legible de la alerta.
        """
        return f"[ALERTA] IP: {self.__ip_origen} | Tipo: {self.__tipo} | Severidad: {self.__severidad}"

    def __eq__(self, otro):
        """
        Define la igualdad entre dos objetos.
        Útil para detectar ataques similares (misma IP y tipo).
        """
        return (self.__ip_origen == otro.__ip_origen) and (self.__tipo == otro.__tipo)

    def __add__(self, otro):
        """
        Permite sumar las severidades de dos intentos.
        Ideal para calcular riesgo total de un conjunto de eventos.
        """
        return self.__severidad + otro.__severidad

    def __lt__(self, otro):
        """
        Permite comparar qué intento es menos severo.
        """
        return self.__severidad < otro.__severidad

# Crear objetos de tipo IntentoIntrusion
ataque1 = IntentoIntrusion("10.0.0.15", 7, "Fuerza Bruta SSH")
ataque2 = IntentoIntrusion("10.0.0.15", 9, "Fuerza Bruta SSH")
ataque3 = IntentoIntrusion("172.16.0.3", 4, "Escaneo de Puertos")

# Mostrar alertas
print(ataque1)
print(ataque3)

# Comparar ataques (usa __eq__)
print("¿ataque1 y ataque2 son del mismo tipo/IP?", ataque1 == ataque2)

# Sumar severidades (usa __add__)
riesgo_total = ataque1 + ataque3
print(f"Riesgo acumulado: {riesgo_total}")

# Comparar severidad (usa __lt__)
if ataque3 < ataque1:
    print("El ataque1 es más severo que ataque3")

# Cambiar la IP usando el setter con validación
ataque3.ip_origen = "192.168.1.10"
print("Nueva IP de ataque3:", ataque3.ip_origen)

# Intentar asignar severidad inválida
try:
    ataque1.severidad = 12
except ValueError as e:
    print("Error:", e)
