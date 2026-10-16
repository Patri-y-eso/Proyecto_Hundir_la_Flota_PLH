import random
from utils import crear_tablero, colocar_barcos, disparar

def mostrar_oculto(tablero): #aquí se oculta el tablero enemigo para no ver sus barcos
    t_oculto = tablero.copy() #Copia el tablero porque si no modificariamos el tablero del rival y lo dejariamos vacío
    t_oculto[t_oculto == 'O'] = ' ' #Cambia "O" por espacios
    print(t_oculto) #Muestra el tablero oculto
 
def jugar(): #Función principal
    print("🌊 ¡BIENVENIDO A HUNDIR LA FLOTA! 🌊")
    
    tablero_jugador = crear_tablero() 
    tablero_maquina = crear_tablero()
                                    #Crea los dos tableros
    barcos_jugador = colocar_barcos(tablero_jugador)
    barcos_maquina = colocar_barcos(tablero_maquina)
                                                    #Coloca los barcos en ambos tableros
    print("\nEste es tu tablero inicial con tus barcos desplegados:")
    print(tablero_jugador) #Muestra mi tablero
    
    impactos_objetivo = 16 #La suma de los 6 barcos (3x2 + 2x3 + 1x4 = 16),e e primero en lograr 16 impactos a barcos, gana
    puntos_jugador = 0
    puntos_maquina = 0
                      #Marcadores comienzan a 0
    while puntos_jugador < impactos_objetivo and puntos_maquina < impactos_objetivo: #Mientras ninguno de los marcadores esté a 16, el bucle sigue
        #Turno del jugador
        print("\n" + "="*43) #Crear una separación entre ambos tableros
        print("📍 TABLERO ENEMIGO:")
        mostrar_oculto(tablero_maquina) #Muestra el tablero enemigo
        
        while True: #comienza la etapa de meter las cordenadas correctas
            try:
                fila_usuario = int(input("\nIntroduce fila (1-10): "))
                col_usuario = int(input("Introduce columna (1-10): ")) 
                
                if not (1 <= fila_usuario <= 10 and 1 <= col_usuario <= 10): #Si las coordenadas no están dentro del tablero error
                    print("❌ Dispara feliz, dispara contento, pero dispara dentro. Coordenadas fuera del mapa, vuelve a intentarlo.")
                    continue #vuelve al inicio del while
                    
                fila_idx = fila_usuario - 1
                col_idx = col_usuario - 1  #al susuario se pide del 1 al 10, pero el programa asigna del 0 al 9
                
                casilla_objetivo = tablero_maquina[fila_idx, col_idx] #Coordenadas de la casilla disparada
                if casilla_objetivo == 'X' or casilla_objetivo == 'A': #Esto pasa si ya ha sido modificada y por eso no se puede repetir
                    print("⚠️ Ya habías disparado en esta coordenada. ¡Elige otra!")
                    continue #vuelve al inicio del while
                
                break #Ya no hay que ,comprobar nada más, continua el código
                
            except ValueError:
                print("❌ Entrada no válida. Se esperaba un número. Vuelve a intentarlo.") #En caso de que se introduzca un string u otro tipo de atributo
                
        print(f"\nTú disparas a la posición: (Fila {fila_usuario}, Columna {col_usuario})")
        if disparar((fila_idx, col_idx), tablero_maquina, barcos_maquina): #disparar devuelve un booleano, por lo que si es true, suma puntos
            puntos_jugador += 1
            
        if puntos_jugador == impactos_objetivo: #Si el jugador llega a 16 puntos gana
            print("\n🏆 ¡ENHORABUENA! Has hundido toda la flota enemiga.")
            break
            
        # TURNO DE LA MÁQUINA
        print("\n" + "-"*43) #separación
        print("🤖 TURNO DE LA MÁQUINA...")
        
        while True:
            fila_maq = random.randint(0, 9)
            col_maq = random.randint(0, 9)  #genera la coordenada random
            
            casilla_objetivo_maq = tablero_jugador[fila_maq, col_maq]
            
            if casilla_objetivo_maq != 'X' and casilla_objetivo_maq != 'A': #si la casilla ya habia sido disparada, vuelve a iniciar, sino, continúa
                break
        
        print(f"La máquina dispara a: (Fila {fila_maq + 1}, Columna {col_maq + 1})")
        if disparar((fila_maq, col_maq), tablero_jugador, barcos_jugador): #Si acierta, suma puntos la maquina
            puntos_maquina += 1
            
        print("\n📍 TU TABLERO:")
        print(tablero_jugador)
        
        if puntos_maquina == impactos_objetivo: #Si la maquina llega a 16 puntos, pierde el jugador
            print("\n💀 DERROTA. La máquina ha destruido tus barcos.")
            break

if __name__ == "__main__":
    jugar()