#evaluacion parcial 3 Sara Quitral Secc007D ejercicio 2

cupos_disponibles=75

#bienvenida
print("¡Bienvenido al sistema de gestión de cupos del Gimnasio marcianeke!")
#reserva o liberacion de cupos
while True:
    print("======MENU PINCIPAL======")
    print("\n1. Cupos disponibles")
    print("2. Realizar reserva")
    print("3. Cancelar reserva")
    print("4. Historial de reservas")
    print("5. Salir")

    try:

        opc=int(input("\nSeleccione una opcion "))

        if opc==1:
            print("\nla cantidad de cupos disponibles son: ", cupos_disponibles)

        elif opc==2:
            reservar=int(input("\n¿Cuantos cupos desea reservar? (ingrese numeros enteros) "))
            if reservar <=0:
                print("el valor no puede ser menor o igual a cero")
            elif reservar >75:
                print("el valor no puede ser mayor a los cupos disponibles")
            else:
                cupos_reservados_disp = cupos_disponibles - reservar

        elif opc==3:
            liberar_cupos=int(input("\n¿Cuantos cupos desea liberar? "))
            if liberar_cupos <=0:
                print("no debe ser menor a 0")
            elif liberar_cupos >75 or reservar:
                print("no se puede liberar cupos mayores a los ocupados o los totales del gimnasio")
            else:
                cupos_disp_liberados = liberar_cupos + cupos_reservados_disp

        elif opc==4:
            print("\nHistorial de reservas:")
            print("cupos reservados: ", reservar)
            if liberar_cupos>0:
                print("cupos liberados: ", liberar_cupos)
                print(f"Cupos en total reservados: {reservar-liberar_cupos}")
                print("Cupos disponibles: ", cupos_disp_liberados)
            else:
                print("Cupos reservados en total: ", reservar)
                print("cupos disponibles: ", cupos_reservados_disp)

        elif opc==5:
            print("\nGracias por utilizar nuestro software, hasta la próxima")
            break

    except ValueError:
        print("invalido")