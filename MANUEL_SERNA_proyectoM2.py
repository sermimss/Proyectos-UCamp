import os

#definicion de la funcion referente al codigo "localiza el cuadrante"
def cuadrantes(nombre):
    
    #se piden al usuario las dos cordenadas referentes a los ejes (x,y)
    x = int(input('ingresa la primer coordenada: '))
    y = int(input('ingresa la segunda coordenada: '))

    #se evalua el simbolo de cada cuadrante "(+,-) (+,+) (-,-) (-,+)"
    x_positiva = x > 0
    y_positiva = y > 0

    #se verifica que no se encuentre en el punto de origen 
    if x == 0 and y == 0:
        print('estas en el punto de origen debes seleccionar una coordenada valida.')
        cuadrantes(nombre)

    #se evalua que ninguna de las cordenadas sea 0
    if x == 0:
        print(f"no estas en ningun cuadrante {nombre}. estas sobre el eje 'Y'")
        cuadrantes(nombre)
    if y == 0:
        print(f"no estas en ningun cuadrante {nombre}. estas sobre el eje 'x'")
        cuadrantes(nombre)   

    # si nada de lo anterior resulta cierto se ingresa a localizar el cuadrante de ubicacion
    #si las dos cordenadas son positivas (+,+)
    if x_positiva and y_positiva:
        print('estas en el "cuadrante I"')
        main(nombre)
    #si solo x es positiva (+,-)
    else:
        if x_positiva:
            print('estas en el "cuadrante IV"')
            main(nombre)
    #si solo y es positiva (-,+)
        else:
            if y_positiva: 
                print('estas en el "cuadrante II"')
                main(nombre)
    #si ninguna es positiva (-,-)
            else:
                print('estas en el "cuadrante III"')
                main(nombre)

#####################################################################

# definicion de la funcion referente a la "Longitud de una frase"

def palabra_secreta(nombre):
    
    #se pide al usuario que ingrese la palabra
    palabra = list(input("ingresa la palabra:\n "))

    #se verifica el tamaño de la palabra
    #si es menor al rango de 4-8 letras
    if len(palabra) < 4:
        print(f"hacen falta letras {nombre}. solo tienes {len(palabra)} letras")
        #se vuelve a preguntar una palabra
        palabra_secreta(nombre)
   
    #si es mayor al rango de 4-8 letras
    elif len(palabra) > 8:
        print(f"sobran letras {nombre}. tienes {len(palabra)} letras")
        #se vuelve a preguntar la palabra 
        palabra_secreta(nombre)
   
    # cuando la frase es del rango correcto
    else:
        print("FELICIDADES!!! la palabra es correcta\n")
        main(nombre)

#########################################################################################


#se define la funcion que dara opciones de eleccion al usuario
def main(nombre):

    opcion = input("a que parte del codigo te gustaria ingresar\n 1.-Palabra secreta\n 2.-Encuentra tu cuadrante\n 0.-salir del programa.\n")
   
    #mientras el usuario no decida salir del programa este continuara 
    if opcion != '0':
    #se verifica la opcion ingresada por el usuario 
    #1 para la primera parte del proyecto 
        if opcion == '1':
        #presentacion personalizada al usuario
            print("perfecto", nombre, "bienvenido al codigo\n 'Longitud de una palabra'")
            palabra_secreta(nombre)
   
    #2 para la segunda parte del proyecto
        elif opcion == '2':
            print(f"perfecto {nombre} bienvenido al codigo 'cuadrantes' usemos tus cordenadas para saber tu ubicacion")
            cuadrantes(nombre)
   
    #cualquier otro valor diferente a los anteriores excepto cero volvera a preguntar al usuario 
        else:
            print("la opcion es invalida.")
            main(nombre)

    else:
    #se finaliza el programa 
        print("fin del programa adios.")
        os.system('pause')
        exit()

nombre = input("hola, cual es tu nombre?")
print(f"Que tal {nombre}")
main(nombre)
