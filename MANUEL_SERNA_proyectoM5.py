# MANUEL SERNA - PROYECTO M5 POKEDEX
# En este proyecto se crea una pokedex que permite al usuario ingresar pokemones por su nombre,
# mostrar su información y guardar los datos en un archivo JSON.        
# Se utiliza la API de PokeAPI para obtener los datos de los pokemones y la librería matplotlib para mostrar las imágenes.
import requests
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from PIL import Image
from urllib.request import urlopen
import json
from deep_translator import GoogleTranslator


# Diccionario para almacenar los pokemones registrados
pokemons_registrados = {}
# Bucle principal del programa
while True:
    print("""
    Selecciona una opción:
    1. ingresar un nuevo pokemon.
    2. guardar y salir del pokedex.
    3. ver los pokemones registrados en tu pokedex.
          """)
    opcion = input("selecciona una de las opciones: ")

# Opción para ingresar un nuevo pokemon
    if opcion == "1":
        
        # Solicitar al usuario el nombre del pokemon
        pokemon = input("ingresa el nombre del pokemon: ").lower()
        # Realizar la solicitud a la API de PokeAPI
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
        # Obtener la respuesta de la API
        respuesta = requests.get(url)
        
        # Verificar si la respuesta es exitosa
        if respuesta.status_code != 200:
            print("pokemon no encontrado, intenta de nuevo")
            continue
        
        # Procesar la respuesta JSON
        else:
            informacion_pokemon = {}
            datos = respuesta.json()
            # Obtener la imagen del pokemon
            try:
                url_imagen= datos['sprites']['other']['official-artwork']['front_default']
                
            except:
                print("no se pudo cargar la imagen")
                break
            
            # Cargar la imagen utilizando PIL
            imagen = Image.open(urlopen(url_imagen))
            id = datos['id']
            nombre = datos['name']
            altura = datos['height']
            altura_m = (int(altura)/32.8)
            altura = round(altura_m, 2)
            peso = datos['weight']
            peso_kg = (int(peso)/2.205)
            peso = round(peso_kg, 2)
            tipo = datos['types'][0]['type']['name']
            habilidad = habilidad = datos['abilities'][0]['ability']['name']
            movimiento = datos['moves'][0]['move']['name']
            # Almacenar la información del pokemon en el diccionario
            informacion_pokemon['nombre'] = nombre
            informacion_pokemon['altura'] = altura
            informacion_pokemon['peso'] = peso
            informacion_pokemon['tipo'] = tipo
            informacion_pokemon['habilidad'] = habilidad
            informacion_pokemon['movimiento'] = movimiento
            pokemons_registrados[id] = informacion_pokemon
            # Mostrar la información del pokemon utilizando matplotlib
        print(f"pokemon {nombre} agregado a tu pokedex")
        plt.imshow(imagen)
        plt.axis('off') 
        # Agregar un cuadro de texto con la información del pokemon
        plt.text(4, -7, f"Nombre: {nombre}\nAltura: {altura} mts.\nPeso: {peso} kg.\nTipo: {GoogleTranslator(source='auto', target='es').translate(tipo)}\nHabilidad: {GoogleTranslator(source='auto', target='es').translate(habilidad)}\nMovimiento: {GoogleTranslator(source='auto', target='es').translate(movimiento)}", fontsize=8, color='black', bbox=dict(facecolor='white', alpha=0.6))
        plt.subplots_adjust(left=0.125, right=0.9, top=0.7, bottom=0.11)
        plt.show()

    # Opción para guardar y salir del pokedex    
    elif opcion == "2":
        
        # Guardar los pokemones registrados en un archivo JSON
         with open("pokedex.json", "a") as archivo:
             for keys, informacion_pokemon in pokemons_registrados.items():
                archivo.write(f'\n{keys}')
                for keys , values in informacion_pokemon.items():
                   archivo.write(f'\n\t{keys} : {values}')
                with open("pokedex.json", "w") as archivo_json:
                
                    json.dump(pokemons_registrados, archivo_json, indent=4)
                    print("pokedex guardada exitosamente, hasta luego!")
                    exit()

    # Opción para ver los pokemones registrados en la pokedex
    elif opcion == "3":
        # Leer y mostrar el contenido del archivo JSON
        with open("pokedex.json", "r", encoding='utf-8') as archivo:
            contenido = archivo.readline()
            #converitr el contenido a formato JSON legible
            f_json = json.dumps(contenido, indent=4)
            #mostrar la cantidad de pokemones registrados
            print(f"{int(len(pokemons_registrados.items() + 1))} pokemones registrados en tu pokedex:")
            print(contenido)
            exit()
    
    # Opción inválida
    else:
        print("opción no válida, intenta de nuevo")
        continue
            
