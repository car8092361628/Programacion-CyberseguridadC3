#Creamos nuestra variable
# Cadena de texto o string
saludo="Hola, bienvenido al curso de Python"
print(saludo)
nombre= input("Por favor, ingresa tu nombre: ")
print("Mi nombre es:",nombre)
#Edad
# Entero o int
#leer se guarda en una variable
edad = int(input("Por favor, ingresa tu edad: "))

print("Mi edad es:",edad)

#Decimal o float    
estatura=float(input("Por favor, ingresa tu estatura en metros (por ejemplo, 1.75): ")) 
print("Mi estatura es:",estatura)

#Booleano o boolean
es_estudiante=True
print("¿Es estudiante?:",es_estudiante)
es_empleado=False
print("¿Es empleado?:",es_empleado)

#condicional if y else
if es_estudiante:
    print(nombre,"es estudiante.")
else:
    print(nombre,"no es estudiante.")
