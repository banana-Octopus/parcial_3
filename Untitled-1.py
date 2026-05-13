#clase 11/5
suma=0

for i in range (3):

    while True:

        try:
         numero=float(input(f"ingrese el numero {i+1}:"))
         suma=suma+numero
         break
        except:
         print("error, debe ingresar un numeo valido")


print("la suma total es: ", suma)


"""
una pequeña tienda que desea modernizar su sistema de tienda, actualmente el vendedor lleva un modesto registro
manual y al fianl del dia llega a calcular todo lo vendido;
para facilitar el trabajo, debemos crear un programa en python, donde ingresemos los productos, los precios, 
y cuando hagamos la venta, se le solicita su rut, nombre, direccion (validar el carnet de usuario)
una vez que tenga todos los adatos del usuario, 
"""