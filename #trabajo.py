#trabajo
"""
desarrolle un programa en python que permiete ingresar dos numeros enteros, e indique un rango numerico, el primer numero debe tener un rango menor 
al segundo, luego el programa debe generar un numero aleatorio, entre el rango de ambos, una vez generado el numero aleatorio, el programa debera
multiplicar por cualquier numero y mostarlo en otro espacio, este no debe afectar los otros dos numeros
"""

from random import randint

print("bienbenido al programa random que multiplica un numero al azar por 134")
print("\n")
num1=int(input("ingrese el primer numero "))
num2=int(input("ingrese el segundo numero "))

#generar numero aleatorio

while True:
    if num1>num2:
        print("el primer numero debe ser menor al segundo")
        break
    elif num1<num2:
        numero = randint(num1,num2)
        #multiplicacion
        num_multiplicado= numero*134
        print("\n")
        print("el numero multiplicado es: ",num_multiplicado)
        print("el numero que salio al azar es ", numero)
        print("los numeros que dijistes ", num1,"-",  num2)

        break
    else:
        num1==num2
        print("apoco si muy verga, bruh -_-   , intentalo otra vez")
        
print("\n adiooooh")










