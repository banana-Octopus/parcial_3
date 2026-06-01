#clase 25/5

"""
un jugador de videojuegos desea comprar armas para su juego,menciona 3 articulos con sus precios espada:5000    arco:7000   baston magico:9000
el usuario puede comprar los articulos que el desee, al oprimir la opcion salir, el usuario debe ver su boleta
"""
from random import randint

arco=7000
baston=9000

#menu
print ("bienvenido a la tiendita merequetenge guajolote, ¿que arma desea comprar?")
print("\n1. espada chida")
print("2. arco del elfo enano")
print("3. baston maxivergas")
print("4. salir despacio sin decir nada")
opcion=int(input("elija una opcion "))

#ruleta

while True:
    if opcion == 1:
        print("\nla espada chida tiene un costo de 5000,")
        print("pero al azar puedes obtener un descuento de 99% o pagar mas del doble" )
        precio_esp = input("¿elijes si o no? ").lower()
        
        if precio_esp == "si":
           random = randint (99,350)
           print("lo que obtuviste fue: ", random, "%")
           precio_final_esp= 5000*(random/100)
           print("el precio quedria en", precio_final_esp)
           break
        
        elif precio_esp=="no":
            print("weno compras al precio normal")
            precio_final_esp=5000
            break
        else:
            print("\npero escribe si o no we")


