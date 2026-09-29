import random
import time

while True:

    print("========== CAMPO DE BATALLA ATLAS ==========")

    vida_jugador = 100
    vida_enemigo = 100

    print("Vida del jugador:", vida_jugador)
    print("Vida del contrincante:", vida_enemigo)
    print()
    print("Los combates seran por turnos. Siempre comienza el jugador.")
    print()
    print("ATACAR - Hace entre 10 y 60 de dano")
    print("CURARSE - Recupera entre 1 y 50 de vida")
    print("HUIR - Solo puedes intentarlo con 90 o mas de vida, o con 10 o menos")
    print()

    while vida_jugador > 0 and vida_enemigo > 0:

        print("========== TURNO DEL JUGADOR ==========")
        print("Vida del jugador:", vida_jugador)
        print("Vida del contrincante:", vida_enemigo)
        print()

        opcion = input("Escoge una opcion: ")
        opcion = opcion.lower()

        # ATAQUE
        if opcion == "atacar":

            if vida_jugador > 70:
                dano = random.randint(10, 60)

            elif vida_jugador >= 40:
                dano = random.randint(10, 45)

            else:
                dano = random.randint(10, 30)

            vida_enemigo = vida_enemigo - dano

            print()
            print("Has hecho", dano, "de dano.")
            print("Vida del contrincante:", vida_enemigo)

        # CURACION
        elif opcion == "curarse":

            if vida_jugador > 70:
                curacion = random.randint(1, 20)

            elif vida_jugador >= 40:
                curacion = random.randint(1, 30)

            else:
                curacion = random.randint(1, 50)

            vida_jugador = vida_jugador + curacion

            if vida_jugador > 100:
                vida_jugador = 100

            print()
            print("Te has curado", curacion, "puntos.")
            print("Vida del jugador:", vida_jugador)

        # HUIR
        elif opcion == "huir":

            if vida_jugador >= 90 or vida_jugador <= 10:

                escape_chance = random.randint(1, 6)

                if escape_chance == 6:
                    print()
                    print("Has huido exitosamente.")
                    break

                else:
                    print()
                    print("No pudiste huir.")

            else:
                print()
                print("No puedes huir con tu nivel actual de vida.")
                continue

        # OPCION INCORRECTA
        else:
            print()
            print("Opcion no valida. Escribe atacar, curarse o huir.")
            continue

        # COMPROBAR SI ALGUIEN GANO
        if vida_jugador <= 0:
            print()
            print("Has perdido.")
            break

        elif vida_enemigo <= 0:
            print()
            print("Has ganado.")
            break

        # TURNO DEL ENEMIGO
        print()
        print("========== TURNO DEL CONTRINCANTE ==========")
        time.sleep(1)

        dano_enemigo = random.randint(10, 40)
        vida_jugador = vida_jugador - dano_enemigo

        print("El contrincante te ha hecho", dano_enemigo, "de dano.")
        print()
        print("Vida del jugador:", vida_jugador)
        print("Vida del contrincante:", vida_enemigo)

        # COMPROBAR SI ALGUIEN GANO
        if vida_jugador <= 0:
            print()
            print("Has perdido.")
            break

        elif vida_enemigo <= 0:
            print()
            print("Has ganado.")
            break

        time.sleep(1)
        print()

    jugar_de_nuevo = input("Quieres jugar otra partida? (si/no): ")
    jugar_de_nuevo = jugar_de_nuevo.lower()

    if jugar_de_nuevo != "si":
        print("Gracias por jugar Campo de Batalla ATLAS.")
        break

    print()