# 🌊 Hundir la Flota en Python 🚢

Un clásico juego de mesa de "Hundir la Flota" desarrollado completamente en Python para jugar desde la terminal. Este proyecto enfrenta al jugador contra una Inteligencia Artificial en un tablero de 10x10. 

El primero en conseguir 16 impactos y hundir la flota enemiga por completo, ¡gana la partida!

## ✨ Características y Mejoras Destacadas

Este proyecto no es solo una versión básica, sino que incluye varias mejoras avanzadas de lógica y experiencia de usuario (UX):

*   **Inteligencia de Posicionamiento Espacial:** Los barcos se generan de forma aleatoria garantizando que **nunca se tocan entre sí**. El algoritmo revisa las 8 casillas vecinas de cada coordenada para asegurar que siempre haya al menos un margen de 1 casilla de agua entre diferentes barcos.
*   **Sistema real de "Tocado y Hundido":** El código rastrea individualmente las "vidas" (coordenadas) de cada barco. Al acertar un disparo, el juego informa si el barco ha sido "Tocado" o si has destruido su última pieza anunciando un "💥 ¡HUNDIDO! 💥".
*   **Interfaz adaptada a humanos:** Aunque internamente las matrices funcionan con índices del 0 al 9, el juego pide al usuario coordenadas del **1 al 10**, haciendo la experiencia mucho más intuitiva.
*   **Bucle de Validación (A prueba de fallos):** ¡No perderás tu turno por un error al teclear! Si introduces una letra, apuntas fuera del mapa o disparas a una coordenada repetida (donde ya hay 'Agua' o 'Tocado'), el juego atrapa el error y te vuelve a pedir las coordenadas inmediatamente.
*   **Niebla de Guerra:** El tablero enemigo se muestra ocultando los barcos ('O') y revelando únicamente tus impactos y fallos.

## 🛠️ Requisitos previos

Para ejecutar este juego, necesitarás tener instalado **Python 3.x** en tu sistema y la librería matemática `numpy` para la gestión de las matrices bidimensionales.

## 🚀 Instalación y Ejecución

Sigue estos pasos para jugar en tu propia terminal:

1. **Clona este repositorio:**
   ```bash
   git clone https://github.com/Patri-y-eso/Proyecto_Hundir_la_Flota_PLH.git
   ```

2. **Navega a la carpeta del proyecto:**
   ```bash
   cd Proyecto_Hundir_la_Flota_PLH
   ```

3. **Instala las dependencias necesarias (Numpy):**
   ```bash
   pip install numpy
   ```
   *(Opcional: Se recomienda hacerlo dentro de un entorno virtual).*

4. **Ejecuta el juego:**
   ```bash
   python main.py
   ```

## 📂 Estructura del Proyecto

El código está dividido en dos archivos principales para mantener una arquitectura limpia y modular:

*   `main.py`: Contiene el bucle principal del juego, la interacción con el usuario mediante terminal y la gestión de los turnos de ambos jugadores.
*   `utils.py`: El "motor" lógico. Aquí se alojan todas las funciones relacionadas con la creación del tablero con Numpy, la generación de coordenadas válidas, la colocación espacial de la flota y la validación de los disparos.

## 🕹️ Cómo jugar

1. Al iniciar, verás tu tablero con tus 6 barcos desplegados de forma aleatoria (representados por la letra `O`).
2. En tu turno, se te pedirá que introduzcas una **Fila (1-10)** y una **Columna (1-10)** para atacar el radar enemigo.
3. Significado de los iconos en el mapa:
   *   ` ` : Agua inexplorada.
   *   `A` : Disparo al agua (fallo).
   *   `X` : Impacto en un barco enemigo (Tocado/Hundido).
   *   `O` : Tus barcos sanos (solo visibles en tu tablero).
4. Tras tu disparo, la máquina responderá automáticamente atacando tus coordenadas.
