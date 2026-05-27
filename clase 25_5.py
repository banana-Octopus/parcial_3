#clase 25/5

"""
un jugador de videojuegos desea comprar armas para su juego,menciona 3 articulos con sus precios espada:5000    arco:7000   baston magico:9000
el usuario puede comprar los articulos que el desee, al oprimir la opcion salir, el usuario debe ver su boleta
"""
from random import choice
#precios
esp_chida=5000
arco=7000
baston=9000
desc_1=0.15
desc_2=0.25
desc_3=0.50
mala_suerte=2.5

#menu
print ("bienvenido a la tiendita merequetenge guajolote, ¿que arma desea comprar?")
print("\n 1. espada chida")
print("2. arco del elfo enano")
print("3. baston maxivergas")
print("4. salir despacio sin decir nada")
opcion=int(input("elija una opcion"))

#ruleta
def azar():
    ruleta = choice[desc_1,desc_2,desc_3,mala_suerte]
    return ruleta

while True:
    if opcion == 1:
        print("la espada chida tiene un costo de 5000," \
        "pero al azar puedes obtener un descuento o pagar mas del doble" )
        precio_final=input("¿elijes si o no?").isalpha
        
        if precio_final == "si".upper():
           azar()
           print(f"lo que obtuviste fue: {ruleta}")
        
        elif precio_final=="no".upper():
            print("weno compras al precio normal")
            precio_final=esp_chida
           
        else:
            print("pero es si o no we")
            


