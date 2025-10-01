# 🎲 Proyecto 3 – Simulación de la Máquina de Galton  
Bootcamp Ucamp – Fundamentos de Python 2025  

## 📝 Descripción  
Este archivo contiene el código de la **Máquina de Galton**, un proyecto desarrollado en el bootcamp de programación en Python. El objetivo principal fue aplicar el uso de librerías externas, la generación de números aleatorios y la visualización de datos mediante gráficas, para simular el comportamiento físico de un sistema de distribución de partículas (canicas) a través de obstáculos.  

La simulación permite observar cómo la probabilidad y el azar influyen en la distribución final de las pelotas, mostrando un histograma que refleja la clásica curva de campana.  

## 🛠️ Tecnologías y conceptos aplicados  
En el desarrollo del programa se utilizaron los siguientes elementos:  

- **Librerías externas**:  
  - `random` → Generación de elecciones aleatorias que determinan el camino de cada pelota en la simulación.  
  - `matplotlib` → Creación de un histograma que representa gráficamente los resultados de la distribución.  

- **Funciones en Python**:  
  - Definición de funciones (`calculo`, `histograma`, `main`) para modularizar el programa y separar la lógica de la simulación y la visualización.  

- **Bucles y estructuras de control**:  
  - Uso de ciclos `for` para simular el recorrido de **3000 pelotas** a través de **12 niveles de obstáculos**.  
  - Condicionales simples para determinar si la pelota se mueve hacia la derecha o la izquierda.  

- **Listas y almacenamiento de datos**:  
  - Registro de las posiciones finales de cada pelota en una lista para su posterior análisis y graficación.  

- **Visualización de resultados**:  
  - Histograma que muestra la cantidad de pelotas acumuladas en cada posición final, con etiquetas personalizadas en los ejes.  

## 💡 Observaciones personales  
Este tercer proyecto fue una experiencia muy interesante, ya que permitió comprender cómo conceptos matemáticos y probabilísticos pueden representarse mediante programación.  

Me resultó muy motivador ver cómo, a través de la combinación de **números aleatorios** y **gráficas**, se pueden simular fenómenos físicos complejos en un entorno computacional. Además, el uso de librerías externas como `matplotlib` me ayudó a visualizar resultados de una manera clara y profesional.  

Con cada proyecto siento que avanzo en la construcción de un perfil más completo
