import math

num2 = math.sqrt(34)
print(num2)
import math
num3 = math.ceil(7.8)
num4 = math.floor(7.8)
print(num3)
print(num4)

#ejemplo para calcular area del triangulo

#variables de entrada
base = int(input("ingrese la base: "))
altura = int(input("ingrese la altura: "))
#proceso
def calcularAreaTriangulo(b,a):
    area = (b*a)/2
    return area

#invocamos la funcion
resultado = calcularAreaTriangulo(base,altura)

#salida
print(f"el area del triangulo cuya base es {base} y la altura {altura} es: ",resultado)

#funcion con argumentos predeterminados
def my_function(country = "Colombia"):
    print("I am from "+country)
#invocar fumcion
my_function()
my_function("sweden")
my_function("germany")
my_function("brazil")

#argumento arbitrario +args
def MostrarEstudiantes(*args):
    print("el estudiante: "+args[2])
MostrarEstudiantes("Emil", "Tobias", "linus", "Bill","luis")

#argumentos de palabras clave
def MostrarCarros(carro1, carro2, carro3):
    print("el carro es: "+carro2)

MostrarCarros(carro1= "bmw", carro3= "ferrari", carro2= "ford")

#argumento arbitrario **kwargs
def MostrarCliente(**kwargs):
    print("su nombre es: "+kwargs["nombre"])

MostrarCliente(nombre = "tobias", apellido= "refsnes")

#declaracion de paso
def mifuncion():
    pass

#Funciones integradas
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

#funcion pow
num1 = pow(7, 4)
print(num1)







