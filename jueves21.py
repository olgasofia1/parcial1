#ejercicio 2 
def area_triangulo (b,h):
  a= b*h/2
  return a
print("Cual es la base:")
b=int(input())
print("Cuál es la altura:")
h=int(input())
print("El area del triángulo es",area_triangulo(b,h))



  # ejercicio 1 
def conversión(km):
  m = km*1000
  return m 
  
print("Cuantos kilometros recorrió:")
km=int(input())
print("Tus km en metros son",conversión(km))
  
  #ronda guiada: multiplicacion y división
def multiplicación (a,b):
  x = a * b
  return x

def división (a,b):
  x = a / b 
  return x
print("Dame el primer número:")
a= int(input())
print("Dame el segundo número:")
b= int(input())
 # b es igual al numero ingresado por el usario y conviertelo en muero entero 
print("La multiplicación da",multiplicación(a,b),"Y la división",división(a,b))
