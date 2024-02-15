
def juego_tenis():
    try:
        # marcador de sets
        sets1 = 0
        sets2 = 0

        # marcador de juegos
        juegos1 = 0
        juegos2 = 0

        suma_juegos = 0

        # marcador de sets
        puntosArr = [0, 15, 30, 40, "GAME", "ADV","GAME"]
        puntos1 = 0
        puntos2 = 0

        try:
            jugador1 = str(input("Ingrese el nombre del jugador 1: "))
            print("El jugador 1 es " + jugador1)
            jugador2 = str(input("Ingrese el nombre del jugador 2: "))
            print("El jugador 2 es " + jugador2)
        except TypeError as te:
            print("Has ingresado los nombres incorrectamente, intente de nuevo")

        jugador_punto = ""

        jugador_saque = ""

        while sets1 < 2 and sets2 < 2:
            while (juegos1 < 6 and juegos2 < 6) or abs(juegos1 - juegos2) < 2 :
                while (puntos1 < 4 and puntos2 < 4) or (puntos1 >= 3 and puntos2 >= 3 and abs(puntos1 - puntos2) < 3):
                    jugador_punto = input("Ingrese el nombre del jugador que hizo puntos: ")
                    if jugador_punto == jugador1:
                        if(puntos1 == 3 and puntos2 == 3):
                            puntos1 += 2
                        elif (puntos1 == 5 and puntos2 == 5 or ((puntos1 == 5 and puntos2 == 4) or (puntos1 == 4 and puntos2 == 5))):
                            puntos1 = 3
                            puntos2 = 3
                        else:
                            puntos1 += 1
                    elif jugador_punto == jugador2:
                        if(puntos2 == 3 and puntos1 == 3):
                            puntos2 += 2
                        elif (puntos1 == 5 and puntos2 == 5 or ((puntos1 == 5 and puntos2 == 4) or (puntos1 == 4 and puntos2 == 5))):
                            puntos2 = 3
                            puntos1 = 3
                        else:
                            puntos2 += 1
                    else:
                        print("Nombre de jugador invalido")
                    print ("Marcadores: " + str(puntosArr[puntos1]) + "-" + str(puntosArr[puntos2]))
                if puntos1 < puntos2:
                    juegos2 += 1
                    puntos1 = 0
                    puntos2 = 0
                elif puntos1 > puntos2:
                    juegos1 += 1
                    puntos2 = 0
                    puntos1 = 0
                print("Se ha sumado un juego a " + jugador_punto)
                print("Marcadores de juego: " + str(juegos1) + "-" + str(juegos2))
            suma_juegos = juegos1 + juegos2
            if (suma_juegos % 2 == 1):
                print("El numero de juegos ha sido impar " + str(suma_juegos) + ",se ha cambiado de cancha")
            if juegos1 > juegos2:
                sets1 += 1
            else:
                sets2 += 1
            print("Se ha sumado un set a " + jugador_punto)
            print("Marcadores de sets: " + str(sets1) + "-" + str(sets2))
            juegos1 = 0
            juegos2 = 0
            suma_juegos = 0

        if(sets1 < sets2):
            print("Ha ganado el jugador 2 llamado " + jugador2)
        elif(sets2 < sets1):
            print("Ha ganado el jugador 1 llamado " + jugador1)
    except Exception as err:
        print("Ha ocurrido un error en la ejecucion", err)



if __name__ == '__main__':
    juego_tenis()







