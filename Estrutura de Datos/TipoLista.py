"""Definir una lista que almacene 5 enteros. Sumar todos sus
elementos y mostrar dicha suma"""

Lista=[10,7,3,7,2,7,7]
Lista.append(100)
Lista.remove(3)


suma=0 #acomulador
x=0 # contador
y=len(Lista)
a=Lista.count(7)
b=sorted(Lista)
Lista.sort()
while x <len(Lista):
    suma=suma+Lista[x]
    x=x+1
    
print ("los elementos de la lista son: ")   
print(Lista) 
print("La suma de todos los elementos es: ")
print(suma)
print("La longitud de la la lista es: ",y)
print("La Cantidad de (x) la  lista es: ",a)
print("el orden ascendente de la  lista es: ",b)


