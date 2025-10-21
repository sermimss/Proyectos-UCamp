# 🧩 Proyecto M5 – Pokedex
**Bootcamp Ucamp – Consumo de APIs y manejo de archivos en Python 2025**

---

## 📝 Descripción
Este proyecto consiste en el desarrollo de una **Pokedex interactiva** implementada en **Python**, la cual permite al usuario consultar información de diferentes Pokémon de manera dinámica.  
El programa obtiene los datos directamente desde la **API pública de PokeAPI**, mostrando información como el nombre, tipo, habilidad, movimiento, altura y peso del Pokémon seleccionado. Además, utiliza la librería **matplotlib** para mostrar su imagen oficial y **deep_translator** para traducir la información al español.  

El objetivo principal de este proyecto fue poner en práctica el **consumo de APIs**, el **manejo de estructuras de datos** en Python, y la **persistencia de información** mediante archivos **JSON**, aplicando los conocimientos adquiridos en el módulo 5 del bootcamp.

---

## 🛠️ Tecnologías y conceptos aplicados
Durante el desarrollo de la Pokedex se emplearon diversas herramientas y conceptos de programación en Python, entre ellos:

- **Consumo de APIs REST:** Uso de la librería `requests` para realizar solicitudes HTTP a la API de PokeAPI y obtener datos en formato JSON.  
- **Procesamiento de datos JSON:** Conversión de las respuestas obtenidas en estructuras de diccionario para facilitar su manipulación.  
- **Visualización con Matplotlib:** Implementación de la librería `matplotlib.pyplot` para mostrar la imagen del Pokémon junto con sus datos en pantalla.  
- **Manejo de imágenes:** Uso de la librería `PIL (Pillow)` para abrir imágenes desde URLs.  
- **Traducción automática:** Integración de `deep_translator` para traducir texto del inglés al español en tiempo real.  
- **Almacenamiento local:** Creación y escritura de un archivo `pokedex.json` para registrar los Pokémon consultados.  
- **Estructuras de control y bucles:** Implementación de menús interactivos mediante `while` y `if/elif/else` para ofrecer una experiencia de uso fluida y repetitiva.  
- **Control de errores:** Verificación del estado de las respuestas HTTP para asegurar la correcta obtención de información.

---

## 💡 Observaciones personales
Este proyecto representó un desafío interesante, ya que me permitió integrar varios conceptos aprendidos a lo largo del módulo en un solo programa funcional. El consumo de una API real como **PokeAPI** me ayudó a comprender mejor cómo se comunican las aplicaciones con servicios externos y cómo transformar esa información en algo visual e interactivo.  

Me resultó especialmente gratificante trabajar con imágenes y traducciones automáticas, ya que dotan al programa de una experiencia más completa y profesional. También reforcé mis conocimientos sobre la lectura y escritura de archivos en formato JSON, algo fundamental en el desarrollo de software moderno.  

En general, considero que este proyecto consolidó mis habilidades en Python y me preparó mejor para los siguientes módulos del bootcamp, donde seguiré aplicando estas bases para crear aplicaciones más complejas y dinámicas.
