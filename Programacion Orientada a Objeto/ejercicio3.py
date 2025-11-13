class Empleado:
    def __init__(self):
        self.nombre=input("Ingrese el nombre del empleado: ")
        self.sueldo=float(input("Ingrese el sueldo del empleado: "))
        
    def imprimir(self):
        print(f"\nEmpleado: {self.nombre}")
        print(f"\nSueldo: {self.sueldo}")
    
    def paga_impuesto(self):
        if self.sueldo>3000:
            print(f"\n{self.nombre} debe pagar impuesto." )
        else:
            print(f"\n{self.nombre} no paga impuesto.")    
        
#Bloque pricipal del programa
      
empleado1 =Empleado()  
empleado1.imprimir()
empleado1.paga_impuesto()      