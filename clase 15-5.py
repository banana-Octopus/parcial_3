#clase 15/5

#ejercicio


"""
el centro de educacion duoc los acaba de contratar para realizar un nuevo sistema de calificacion para sus estudiantes, asignatura para registrar:
matematica 1, fundamentos de programacion, debox, inteligencia artificial y ciencia de datos
el docente debe introducir las calificaciones de cada asignatura, debe s er capas de consultar dichas calificaciones y calcular el promedio
el programa debe tener manejo de errores
"""
#cosas importantes
nota_minima=1.0
nota_maxima=7.0

#datos del alumno
while True:
    alumno=input("ingrese el nombre del alumno ")
    if alumno.isalpha():
     print("alumno aceptado")
     break
    else:
        print("ingrese un nombre valido")


#sistema de notas
print("----------elija materia----------")
print("\n1. matematica 1")
print("2. fundamento de la programacion")
print("3. inteligencia artificial")
print("4. ciencia de datos")

opcion=int(input("seleccione una clase "))

if opcion==1:
    def promedio_mate():
        while True:
            cantidad_de_notas=0

            nota1=input("ingrese la primera nota ")
            if nota1 <nota_minima >nota_maxima:
                cantidad_de_notas=+1
            else:
                print("ingrese una nota valida")

            nota2=input("ingrese la segunda nota ")
            if nota2 <nota_minima >nota_maxima:
                cantidad_de_notas=+1
            else:
             print("ingrese una nota valida")

            nota3=input("ingrese la tercera nota ")
            if nota3 <nota_minima >nota_maxima:
                cantidad_de_notas=+1
            else:
                print("ingrese una nota valida")

            nota4=input("ingrese la cuarta nota ")
            if nota4 <nota_minima >nota_maxima:
                cantidad_de_notas=+1
                break
                
            else:
                print("ingrese una nota valida")
                
            suma_notas=(nota1+nota2+nota3+nota4)
        if cantidad_de_notas==4:
         promedio_mate(suma_notas)/4
    promedio_mate()
    

       
elif opcion==2:
    while True:
        
        nota1=int(input("ingrese una calificacion"))
        if nota1 == nota:
            cantidad_de_notas=+1
        else:
            print("ingrese una nota valida")

        nota2=int(input("ingrese una calificacion"))
        if nota2 == nota:
            cantidad_de_notas=+1
        else:
            print("ingrese una nota valida")

        nota3=int(input("ingrese una calificacion"))
        if nota == nota:
            cantidad_de_notas=+1
        else:
            print("ingrese una nota valida")

        nota4=int(input("ingrese una calificacion"))
        if nota4 == nota:
            cantidad_de_notas=+1
            break
        else:
            print("ingrese una nota valida")
            
    if cantidad_de_notas==4:
         promedio_fundamento=(nota1+nota2+nota3+nota4)/4

elif opcion==3:
    while True:
        
        nota1=int(input("ingrese una calificacion"))
        if nota1 == nota:
          cantidad_de_notasantidad_de_notas=+1
        else:
           print("ingrese una nota valida")

        nota2=int(input("ingrese una calificacion"))
        if nota2 == nota:
           cantidad_de_notas=+1
        else:
         print("ingrese una nota valida")

        nota3=int(input("ingrese una calificacion"))
        if nota == nota:
            cantidad_de_notas=+1
        else:
            print("ingrese una nota valida")

        nota4=int(input("ingrese una calificacion"))
        if nota4 == nota:
            cantidad_de_notas=+1
            break
        else:
            print("ingrese una nota valida")
            
    if cantidad_de_notas==4:
        promedio_artificial=(nota1+nota2+nota3+nota4)/4

elif opcion==4:
    while True:
    
        nota1=int(input("ingrese una calificacion"))
        if nota1 == nota:
            cantidad_de_notas=+1
        else:
            print("ingrese una nota valida")

        nota2=int(input("ingrese una calificacion"))
        if nota2 == nota:
            cantidad_de_notas=+1
        else:
            print("ingrese una nota valida")

        nota3=int(input("ingrese una calificacion"))    
        if nota == nota:
            cantidad_de_notas=+1
        else:
            print("ingrese una nota valida")

        nota4=int(input("ingrese una calificacion"))
        if nota4 == nota:
            cantidad_de_notas=+1
            break
        else:
            print("ingrese una nota valida")
            
    if cantidad_de_notas==4:
        promedio_ciencias=(nota1+nota2+nota3+nota4)/4
            
else: 
 print("opcion invalida")

#promedio de cada clase
print("---------promedios de clase---------")
print("\npromedio matematicas 1: ", )
print("promedio de fundamentos de programacion: ", )
print("promedio de inteligencia artificial: ", )
print("print promedio de ciencias de datos: ", )