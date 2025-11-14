def mostrar_mensaje(mensaje):
    print("*********************************")
    print(mensaje)
    print("*********************************")
    
def calculadora():
    valor1=int(input("Ingrese el primer valor: "))
    valor2=int(input("Ingrese el segundo valor: ")) 
    suma=valor1+valor2
    resta=valor1-valor2
    mulplicacion=valor1*valor2
    division=valor1/valor2
    print(f"La suma de los valores son:\n{suma}") 
    print(f"La resta de los valores son:\n{resta}")   
    print(f"La mulplicacion de los valores son:\n{mulplicacion}")   
    print(f"La division de los valores son:\n{division}")     
    
mostrar_mensaje("El programa calcula la suma de dos valores ingresado por teclado")
calculadora()
mostrar_mensaje("Gracias por utilizar este servicio")  