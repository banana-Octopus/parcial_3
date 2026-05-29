#evaluacion parcial 3 Sara Quitral Secc007D ejercicio 1

#datos contabilizables
comandante_galactico=0
cadete_estelares=0

#cantidad de pilotos
while True:
    cant_pilotos=int(input("¿Cuantos pilotos desea ingresar? "))
    if cant_pilotos==0:
        print("Debes registrar almenos un piloto")
    elif cant_pilotos<0:
        print("¡Número inválido! Ingresa un entero positivo para continuar el entrenamiento")
    else:
        break
 
#nombre de los pilotos
for i in range (cant_pilotos):
    #nombre piloto

    nombre=input("Ingrese el nombre de uno de los pilotos, sin espacios ")
    try:
        if nombre (1-5):
            print("El nombre debe tener mas de 6 digitos")

        else:
        #cantidad de comandantes y cadetes

            nivel_piloto=int(input("Ingrese el nivel del piloto "))
            if nivel_piloto>40:
                comandante_galactico=+1

            elif nivel_piloto<=40:
                cadete_estelares=+1

            else:
                nivel_piloto<=0
                print("¡Error de calibración! Ingresa un número entero positivo para el nivel de vuelo.")
    except SyntaxError:
        print("")           

#salida final

print(f"\nLa flota estelar cuenta con {comandante_galactico} comandantes galacticos y {cadete_estelares} cadetes estelares")
print("¡PREPARENCE PARA DESPEGAR!")

