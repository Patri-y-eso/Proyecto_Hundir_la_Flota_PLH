import numpy as np
import random

def crear_tablero(tamano=10):
    return np.full((tamano, tamano), ' ') #Tablero de 10x10 con espacios como casillas, ya que con "_" se veia muy saturado

def colocar_barco(barco, tablero): #Barco es una lista de coordenadas y tablero es la matriz donde las va a dibujar
    for fila, col in barco:
        tablero[fila, col] = 'O'  #Va cambiando en el tablero, la matriz, los espacios en blanco por "O" donde se encuentra el barco
    return tablero

def crear_barco(eslora, tablero): #Eslora es el tamaño del barco
    tamano = tablero.shape[0] #Shape del tablero es (10,10), por lo tanto, tamano erá 10
    while True:
        orientacion = random.choice(['H', 'V']) #Elige de manera aleatoria si el barco va a estar colocado en horizonal o vertical
        if orientacion == 'H':
            fila = random.randint(0, tamano - 1) #Elige una fila al azar entre la 0 y la 9
            col = random.randint(0, tamano - eslora) #Elige una columna al azar pero le resta el tamaño del barco, así no se podrá salir del tablero
                                                     #Si el barco es de tamaño 4, el tope de la columna inicial será la 6
            barco = [(fila, col + i) for i in range(eslora)] #Dibuja el resto del barco
        else: #Lo mismo pero en vertical, cambiando filas por columnas
            fila = random.randint(0, tamano - eslora)
            col = random.randint(0, tamano - 1)
            barco = [(fila + i, col) for i in range(eslora)]

        invalido = False #Supone que el barco es válido
        for f, c in barco: #f = fila, c = columna
            for df in [-1, 0, 1]: #df = diferencia de fila
                for dc in [-1, 0, 1]: #dc = diferencia de columna, esta linea y la anterior crean una cuadricula 3x3 al rededor de la casilla que comprobamos
                    vecina_f = f + df 
                    vecina_c = c + dc # esta linea y la anterior crean las verdaderas coordenadas de la casilla vecina que debe estar vacia
                    if 0 <= vecina_f < tamano and 0 <= vecina_c < tamano: #comprueba que la vecina no está fuera del tablero
                        if tablero[vecina_f, vecina_c] == 'O': #Si en esta casilla hay una "O", significa que el barco se solaparia o que esta pegado, no sirve
                            invalido = True #Posicioón invalida
                            break #Rompe el bucle y deja de buscar
                if invalido:
                    break
            if invalido:
                break #Los tres break es para que rompa cada bucle interno y vuelva al while principal
                
        if not invalido:
            return barco #Si no es invalido, todas las vecinas están vacías y devuelve las coordenadas del barco válido

def colocar_barcos(tablero):
    flota = [2, 2, 2, 3, 3, 4] # 6 barcos en total, 3 de tamaño 2, 2 de tamaño 3 y 1 de tamaño 4
    lista_barcos = [] #En esta lista iremos guardando info de los barcos para posteriormente saber si se ha hundido
    
    for eslora in flota: 
        barco_nuevo = crear_barco(eslora, tablero) #crea un barco válido
        colocar_barco(barco_nuevo, tablero) #coloca el barco válido
        lista_barcos.append(list(barco_nuevo)) #guarda las coordenadas del barco en iuna lista, dentro de la lista vacia anteior
        
    return lista_barcos

def disparar(casilla, tablero, lista_barcos): #recibe la coordenada que introduciremos, el tablero y la lista de coordenadas de los barcos
    fila, col = casilla
    estado_actual = tablero[fila, col] #mira si en esa casilla del tablero hay una "O" o está vacía
    
    if estado_actual == 'O':
        tablero[fila, col] = 'X' #Si hay una "O", lo cambia por una "X"
        
        for barco in lista_barcos: #revisa las coordenadas de cada uno de los barcos
            if casilla in barco:
                barco.remove(casilla) # Quita esa coordenada del barco al que pertenece
                if len(barco) == 0:
                    print("💥 ¡HUNDIDO! 💥") #si despues de quitarla, el barco se ha quedado a 0, significa que está hundido
                else:
                    print("🔥 ¡Tocado!") #Si el barco sigue teniendo coordenadas, está solo tocado
                break #Deja de buscar porque ya está encontrado y modificado el barco tocado o hundido
                
        return True #El marcador suma 1
    elif estado_actual == ' ': #Si en la casilla no habia nada, cambia su estado por "A" de agua
        tablero[fila, col] = 'A'
        print("💧 ¡Agua!")
        return False #El marcador no suma puntos