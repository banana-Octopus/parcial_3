#evaluacion formativa 3 Sara Quitral


pikachu_roll=4500
otaku_roll=5000
pulpo_venenoso=5200
angila_electrica=4800

#bienvenida
print("bienvenidos al suhitumare")
print("¿que desea pedir?")
#menu
print("\n1. pikachu roll $4500")
print("2. otaku roll $5000")
print("3. pulpo venenoso roll $5200")
print("4. angila electrica roll $4800")
print("5. finalizar pedido")

#pedidos
pedido=(input("igrese el numero del sushi para tomar su orden "))
while True:
    #valores variables
    total_pedidos=0
    cant_pedido1=0
    cant_pedido2=0
    cant_pedido3=0
    cant_pedido4=0

    if pedido==1:
        precio_1=pikachu_roll
        cant_pedido1 =+1

    elif pedido==2:
        precio_2=otaku_roll
        cant_pedido2=+1
        

    elif pedido==3:
        precio_3=pulpo_venenoso
        cant_pedido3=+1
        

    elif pedido ==4:
        precio_4=angila_electrica
        cant_pedido3 =+1

        
    pedido=(int(input("¿algo mas que desea agregar? ")))

    if pedido==5:
        total_pedidos=cant_pedido1+cant_pedido2+cant_pedido3+cant_pedido4
        break

print("ya tenemos su pedido")

sub_total=[[cant_pedido1*pikachu_roll]+[cant_pedido2*otaku_roll]+[cant_pedido3*pulpo_venenoso]+[cant_pedido4*angila_electrica]]

    

#descuento
pregunta=(input("¿desea ingresar un cupon? si/no ")).isalpha
if pregunta=="si".upper():
    while True:
        cupon=input("ingrese el cupon")
        if cupon!="soyotaku":
            cupon=input("ingrese un cupon valido o presione x para volver")

            if cupon!="soyotaku":
                print("ingrese un cupon valido")

            elif cupon=="x":
                break
        else:
            cupon== "soyotaku"
            valor_desc=10
            desc=0.10
else:
    #no hay cupon
    valor_desc=0
    desc=1

print("---------------boleta-------------")
print("\ntotal productos: ", total_pedidos)
print("picachu roll: ", cant_pedido1)
print("otaku roll: ", cant_pedido2)
print("pulpo venenoso roll: ", cant_pedido3)
print("angila electrica roll:", cant_pedido4)
print("subtotal a pagar: ", sub_total)
print("descuento:", valor_desc, "%")
print(f"precio final: {sub_total*desc}")