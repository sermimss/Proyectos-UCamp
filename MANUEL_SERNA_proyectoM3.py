#importamos las librerias necesarias
#random para la eleccion aleatoria
#matplotlib para la visualizacion de los resultados
import random
import matplotlib.pyplot as plt

    
def calculo(maquina_de_galton):
    '''Esta funcion simula la caida de 3000 pelotas atravesando 12 niveles de obstaculos
    y devuelve una lista con la posicion final de cada pelota en un eje horizontal'''
    # Simulamos la caida de 3000 pelotas 
    for p in range(1,3001):
        caida = 0
        # Simulamos las 12 decisiones de cada pelota
        for eleccion in random.choices(['D','I'], k=12):
            if eleccion == 'D':
                caida += 1
            else:
                caida -= 1
        # Almacenamos el resultado de cada pelota en una lista
        maquina_de_galton.append(caida)
    # Devolvemos la lista con los resultados de las 3000 pelotas
    return maquina_de_galton


def histograma(maquina_de_galton):
    '''Esta funcion grafica un histograma con los resultados de la simulacion'''
    plt.hist(maquina_de_galton, bins=12 , color='skyblue')
    #se agregan los titulos y etiquetas a la grafica
    plt.title('simulacion de la Máquina de Galton')
    plt.xlabel('distribucion de canicas')
    plt.ylabel('cantidad de canicas')
    # Ajuste de las etiquetas del eje x para que vayan de 1 a 12
    ticks=list(range(-6, 7, 2))
    labels=list(range(0,13, 2))
    plt.xticks(ticks=ticks, labels=labels)  
   # Mostramos la grafica
    plt.show()


def main():
    '''funcion que incluye las dos funciones anteriores que se solicitan en la tarea'''
    # usamos la primer funcion para simular los resultados de la maquina de galton
    maquina_de_galton = [x // 2 for x in calculo(maquina_de_galton =[])]
    # usamos la segunda funcion para graficar el histograma
    histograma(maquina_de_galton)

# Ejecutamos la funcion principal
main()