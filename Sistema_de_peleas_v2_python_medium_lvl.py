from random import randint, choice
import time

enemigo = {
    "oso": 400,
    "humano": 100,
    "lobo": 85,
    "serpiente": 75,
    "leopardo": 200,
    "rebelde (humano armado)": 150
}

premio = {
    "carne de caza mayor": "oso",
    "ropa": "humano",
    "pelaje": "lobo",
    "colmillos": "serpiente",
    "garras": "leopardo",
    "arma de fuego": "rebelde (humano armado)"
}

objeto_inicial = {
    "cuchillo": 50,
    "platano": 3,
    "zapato": 10,
    "pan": 1,
    "boligrafo": 15
}

mala_suerte = [
    1, 6, 17, 12, 16, 8, 36, 86, 69,
    35, 51, 16, 7, 8, 9, 34, 100
]

inventario = []
vida = 100
daño_base = 10

print("SIMULADOR DE PELEAS ATLAS (BETA)")
print("-" * 35)

objeto_aleatorio = randint(1, 100)

if objeto_aleatorio not in mala_suerte:
    objeto = choice(list(objeto_inicial.items()))

    print("¡Vaya! ¡Qué suerte!")
    print("Recibirás un objeto aleatorio...")
    time.sleep(3)

    print("Has obtenido:", objeto[0])
    print("Daño adicional:", objeto[1])

    inventario.append({
        "nombre": objeto[0],
        "daño": objeto[1],
        "usos": 3
    })
else:
    print("Mala suerte, empiezas sin objeto.")

opcion = input(
    "\n1.- BUSCAR UN ENEMIGO PARA PELEAR"
    "\n2.- VER INVENTARIO"
    "\n3.- SALIR"
    "\nElige una opción: "
)

while opcion != "3":

    if opcion == "1":
        print("\nBuscando contrincante, por favor espere...")
        time.sleep(5)

        contrincante, vida_enemigo = choice(list(enemigo.items()))

        print("Tu contrincante será:", contrincante)
        print("El juego será por turnos. Empiezas tú.")
        print("Tu vida:", vida)
        print("Vida del enemigo:", vida_enemigo)

        while vida > 0 and vida_enemigo > 0:

            turno_jugador = input(
                "\n1.- Curarse"
                "\n2.- Atacar"
                "\n3.- Usar objeto del inventario"
                "\n4.- Escapar"
                "\nElige tu acción: "
            )

            if turno_jugador == "1":
                curacion = randint(1, 25)
                vida = min(vida + curacion, 100)

                print("Te curaste. Ahora tu vida es:", vida)

            elif turno_jugador == "2":
                daño = randint(1, 50) + daño_base

                if inventario:
                    print("\nElige un objeto para atacar:")

                    for i, objeto in enumerate(inventario):
                        print(
                            i + 1, "-", objeto["nombre"],
                            "| Daño extra:", objeto["daño"],
                            "| Usos:", objeto["usos"]
                        )

                    print("0 - Atacar sin objeto")
                    eleccion = input("Elige: ")

                    if eleccion.isdigit():
                        eleccion = int(eleccion)

                        if 1 <= eleccion <= len(inventario):
                            objeto_usado = inventario[eleccion - 1]

                            daño += objeto_usado["daño"]
                            objeto_usado["usos"] -= 1

                            print("Usaste:", objeto_usado["nombre"])
                            print("Daño adicional:", objeto_usado["daño"])
                            print("Usos restantes:", objeto_usado["usos"])

                            if objeto_usado["usos"] == 0:
                                print("¡El objeto se ha roto!")
                                inventario.remove(objeto_usado)

                        elif eleccion != 0:
                            print("Opción no válida.")
                            continue
                    else:
                        print("Debes introducir un número.")
                        continue

                vida_enemigo = max(vida_enemigo - daño, 0)

                print("Hiciste", daño, "de daño.")
                print("Vida del enemigo:", vida_enemigo)

                if vida_enemigo > 0:
                    daño_enemigo = randint(5, 20)
                    vida = max(vida - daño_enemigo, 0)

                    print("El enemigo te hizo", daño_enemigo, "de daño.")
                    print("Tu vida:", vida)

            elif turno_jugador == "3":
                if not inventario:
                    print("No hay nada en el inventario.")
                else:
                    print("\n--- INVENTARIO ATLAS ---")

                    for objeto in inventario:
                        print(
                            objeto["nombre"],
                            "- Daño:", objeto["daño"],
                            "- Usos:", objeto["usos"]
                        )

            elif turno_jugador == "4":
                escape = randint (1,10)
                if escape != 1 and escape != 5 and escape != 9:
                     print("Has escapado del combate.")
                     break

            else:
                print("Opción no válida.")

        if vida == 0:
            print("Has perdido el combate.")
            break

        elif vida_enemigo == 0:
            print("¡Has derrotado al", contrincante + "!")

            for nombre_premio, dueño in premio.items():
                if dueño == contrincante:
                    print("El enemigo ha soltado:", nombre_premio)

                    inventario.append({
                        "nombre": nombre_premio,
                        "daño": 0,
                        "usos": 3
                    })

    elif opcion == "2":
        print("\n--- INVENTARIO ATLAS ---")

        if not inventario:
            print("No hay nada en el inventario.")
        else:
            for objeto in inventario:
                print(
                    objeto["nombre"],
                    "- Daño:", objeto["daño"],
                    "- Usos:", objeto["usos"]
                )

    else:
        print("Opción no válida.")

    opcion = input(
        "\n1.- BUSCAR UN ENEMIGO PARA PELEAR"
        "\n2.- VER INVENTARIO"
        "\n3.- SALIR"
        "\nElige una opción: "
    )

print("Has salido del SIMULADOR DE PELEAS ATLAS.")