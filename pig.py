import random
from random import randint


# El jugador tira un dado, mientras no salga el 1, su puntaje se va sumando. Si sale 1, el puntaje se vuelve 0 y pierde
# si el jugador hace más de 50 puntos, gana.
# el jugador decide cuándo termina su turno y va el siguiente jugador, asi sucesivamente

# Tirar dados
def tirar_dados():

    # esta funcion arroja un numero aleatorio del 1 al 6
    num = random.randint(1,6)
    return num

# Numero de jugadores
def jugadores():
    while True:
        players = input("Ingresa el numero de jugadores (min 2, max 4): ")
        if players.isdigit():
            players = int(players)
            if 2 <= players <= 4:
                break
            else:
                print("Debes ingresar un numero entre 2 y 4")
        else:
            print("Invalido. Ingresa un numero entre 2 y 4")
    return players

puntaje_max = 50
puntaje_players = []
numero_jugadores = jugadores()
for player in range(numero_jugadores):
    puntaje_players.append(0)

while max(puntaje_players) < puntaje_max:

    for jugador_indice in range(numero_jugadores):

        print(f"\nJugador {jugador_indice + 1} es tu turno!\n")
        print(f"Tu puntaje total es: {puntaje_players[jugador_indice]}\n")
        puntaje_al_momento = 0

        while True:
            pregunta = input("Quieres lanzar el dado? (Y): ")
            if pregunta.lower() != "y":
                break

            valor = tirar_dados()
            if valor == 1:
                print(f"Tiraste un {valor}! Termino tu turno!")
                puntaje_al_momento = 0
                break
            else:
                puntaje_al_momento += valor
                print(f"Tiraste un {valor}!")

            print(f"Tu puntaje es: {puntaje_al_momento}")

        puntaje_players[jugador_indice] += puntaje_al_momento
        print(f"Tu puntaje total es: {puntaje_players[jugador_indice]}")
puntaje_max = max(puntaje_players)
indice_ganador = puntaje_players.index(puntaje_max)
print(f"El jugador {indice_ganador + 1} es el ganador con un puntaje de {puntaje_max}!")