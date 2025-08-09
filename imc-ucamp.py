#practica 1 ucamp fundamentos de python
#este es el codigo del IMC solicitado en la primer tarea 

#primero se da la bienvenida al programa.
print("Bienvenido a: \" LA CALCULADORA DE INDICE DE MASA CORPORAL. \" ")

#se pregunta al usuario si desea continuar con la ejecucion del programa o salir de el.
print("sigue las instrucciones o preciona enter para salir.\n")

#si el usuario continua:
#se comienza con la captura de datos
cliente = input("CUAL ES TU NOMBRE?\n")

#sentencia if para validar la decicion del usuario.
if cliente != "":   
    
    completo = 1

    #sentencia while para asegurar que el usuario introduzca los datos de forma correcta 
    while (completo == 1):

        #sentencia try para manejo de errores 
        #dato nulo o string donde se espera un valor numerico
        try:
            print("cual es tu edad")
            #se agrega un ejemplo del dato esperado
            #para facilitar la fluides del programa
            print("(ej: 25)")
            E = int(input()) 


        except:
            #si el dato ingresado es invalido 
            #se activa el ciclo while 
            print("\nel valor es incorrecto")
            print("intentemoslo nuevamente\n")


        else:
            try:
                #se pregunta su altura
                print("cual seria tu altura en mts.")
                #los ejemplos se mantienen
                #en cada interaccion con el usuario
                print("(ej: 1.78)")
                A = float(input())


            except:
                #siempre que un dato sea erroneo
                #el programa le permitira intentarlo de nuevo
                print("\nel valor ingresado es invalido")
                print("introduzcamos los datos nuevamente\n")


            else:
                try:
                    #se pregunta el peso del usuario
                    print("cual seria tu peso en kg")
                    print("(ej:88.2)")
                    P = float(input())


                except:
                    #solo al ingresar todos los datos 
                    #de forma correcta se abandonara del bucle
                    print("\nel valor introducido no es correcto")
                    print("ingresemos los datos nuevamente\n")


                else:
                    #se informa del exito en la captura de datos 
                    #se utiliza la variable modificada para terminar la sentencia while
                    print("los datos fueron capturados correctamente!!!\n")
                    completo = completo + 1



#este condicional else solo se activa 
#si el usuario no continua con el programa desde un inicio    
else:

    #se agradece el tiempo del usuario 
    #se finaliza el programa 
    print("programa finalizado, gracias por su tiempo \nADIOS!")
    exit()

 
#una vez ingresados todos los datos de forma correcta
#se le presentan al usuario de forma ordenada 
#siguiendo el siguiente formato:
#NOMBRE, EDAD, ALTURA, PESO
print("tu nombre es:", cliente , 
      "\ntu edad:", E, "años", 
      "\ntu altura:", A, "mts", 
      "\ntu peso:", P, "kg\n")



#se utilisa la condicional if 
#para verificar la edad del usuario
if E >= 18:


#se calcula y muestra el IMC
    indice = P/(A**2)

    #se incluye el IMC con un feedback
#de su condicion (severa, leve, moderada)
    indice1 = round(indice, 2)

    #se imprime el IMC con la anotacion del feedback calculado
    print("IMC de:" + str(indice1) + " kg/m2", "\ntu estado de nutricion es:")



#la sentencia if elif else utilizada para
#calcular el feedback y la condicional del usuario
    IMC = indice1
    if IMC >= 0 and IMC <= 15.99:
        print ("Delgadez severa")
    elif IMC >= 16.00 and IMC <= 16.99: 
        print ("Delgadez moderada")
    elif IMC >= 17.00 and IMC <= 18.49:
        print ("Delgadez leve")
    elif IMC >= 18.50 and IMC <= 24.99:
        print ("Normal")
    elif IMC >= 25.00 and IMC <= 29.99:
        print ("Sobrepeso")
    elif IMC >= 30.00 and IMC <= 34.99:
        print ("obesidad leve")
    elif IMC >= 35.00 and IMC <= 39.00:
        print ("obesidad media")
    elif IMC >= 40.00:
        print ("obesidad morbida")
    
    ##solo se muestra el IMC si el usuario es mayor de edad
else:
    print("\nLO SIENTO: se deve ser mayor de edad para usar la calculadora de imc.")
    print("hasta luego.")
