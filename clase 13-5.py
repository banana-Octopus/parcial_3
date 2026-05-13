#clASE 13/05
#calculadora 100tifika

def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multiplication(a,b):
    return a * b

def dividit(a,b):
    if b == 0:
        return"error, no se puede dividir por cero"
    
    return a / b

print("============calculdora============")
num1 =float(input("ingrese su primer numero"))
num2 =float(input("ingrese su segundo numero"))

print("\n1 sumar")
print("2. restar")
print("3. multiplicar")
print("4. dividir")

opcion=input("selecciona una opcion")

if opcion=="1":
    print("resultado", suma(num1,num2))

elif opcion=="2":
    print("resultado", resta(num1,num2))

elif opcion=="3":
    print("resultado", multiplication(num1,num2))

elif opcion =="4":
    print("resultado",dividit(num1,num2))

else:
    print("opcion invalida")