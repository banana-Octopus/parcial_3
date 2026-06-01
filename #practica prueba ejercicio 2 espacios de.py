#practica prueba ejercicio 2 espacios de almacenamiento

espacios_disponibles=60

print("¡bienvenido al sistema de gestion de esoacios del almacen industrial!")

while True:
  
    try:
        print("\n====== MENU PRINCIPAL=======")
        print("\n1. espacios disponibles")
        print("2. ocupar espcaio")
        print("3. liberar espacio")
        print("4. espacios actualmente ocupados")
        print("5. salir")
        opc=int(input("seleccione una opcion "))

        if opc==1:

            print("\nlos espacios disponibles son: ",espacios_disponibles)

        elif opc==2:
            ocupar_espacio=int(input("¿cuantos espacios desea ocupar? "))
            if ocupar_espacio  <=0:
                print("ingresa un numero entero mayor a 0")
            elif ocupar_espacio >60:
                print("espacio solicitado mayor al disponible")
            else:
                espacios_ocupados=espacios_disponibles-ocupar_espacio

        elif opc ==3:
            liberar_espacio=int(input("¿cuantos espacios desea liberar? "))
            if liberar_espacio<=0:
                print("ingresa numeros enteros mayores a 0")
            elif liberar_espacio>ocupar_espacio:
                print("no se puede liberar espacio mayor al total de almacenamiento ocupado")
            else:
                ocupar_espacio=espacios_ocupados+liberar_espacio
        elif opc==4:
            print("los espacios actualmente ocupados son: ", ocupar_espacio)

        elif opc==5:
            print("salir")
            break
    except ValueError:
        print("debes ingresar valores enteros")


