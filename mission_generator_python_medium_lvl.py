
import random

misiones = [
    "Resolver un acertijo",
    "Derrotar a un enemigo",
    "Encontrar un tesoro"
]

acertijos = [
    "¿Qué fruto se come primero y se planta después?",
    "Cinco hermanos salen a la calle y cuatro se mojan. ¿Cómo es posible?",
    "En una habitación oscura hay una vela, una lámpara y una estufa. ¿Qué enciendes primero?",
    "Un hombre está atrapado en un castillo con un pasillo peligroso y un dragón. ¿Cómo puede escapar?",
    "Tres amigos pagan $30 por una habitación y reciben $3 de vuelta. ¿Dónde está el dólar faltante?",
    "Tres cajas tienen etiquetas incorrectas: blancas, negras y mezcla. ¿De cuál sacas una canica para corregirlas?"
]

def generar_mision():
    return random.choice(misiones)

def generar_acertijo():
    return random.choice(acertijos)

nombre = input("Introduce tu nombre: ")
mision = generar_mision()
puntos = 0

print("\n=== GENERADOR DE MISIONES ATLAS ===")
print("Hola,", nombre)
print("Tu misión es:", mision)

# MISIÓN 1: ACERTIJOS
if mision == "Resolver un acertijo":
    acertijo = generar_acertijo()
    print("\nResuelve el siguiente acertijo:")
    print(acertijo)

    if acertijo == acertijos[0]:
        recompensa = 10
    elif acertijo == acertijos[1]:
        recompensa = 20
    elif acertijo == acertijos[2]:
        recompensa = 10
    elif acertijo == acertijos[3]:
        recompensa = 30
    elif acertijo == acertijos[4]:
        recompensa = 40
    else:
        recompensa = 50

    respuesta = input("Tu respuesta: ").lower()

    print("Recompensa posible:", recompensa, "puntos")
    print("La comprobación de respuestas aún está pendiente.")

# MISIÓN 2: COMBATE
elif mision == "Derrotar a un enemigo":
    vida_enemigo = random.randint(100, 250)
    vida_jugador = 100
    escapaste = False

    print("\n¡Un enemigo apareció!")
    print("Vida del enemigo:", vida_enemigo)

    for i in range(3):
        if vida_enemigo <= 0 or vida_jugador <= 0:
            break

        print("\nTurno", i + 1)
        print("Tu vida:", vida_jugador)
        print("Vida enemiga:", vida_enemigo)

        opcion = input("Atacar, Curar o Escapar: ").lower()

        if opcion == "atacar":
            ataque = random.randint(40, 150)
            vida_enemigo -= ataque
            print("¡Hiciste", ataque, "de daño!")

            if vida_enemigo > 0:
                daño = random.randint(10, 30)
                vida_jugador -= daño
                print("El enemigo te hizo", daño, "de daño.")

        elif opcion == "curar":
            curacion = random.randint(20, 60)
            vida_jugador += curacion
            print("Recuperaste", curacion, "de vida.")

            daño = random.randint(10, 30)
            vida_jugador -= daño
            print("El enemigo te hizo", daño, "de daño.")

        elif opcion == "escapar":
            escapaste = True
            print("¡Escapaste del enemigo!")
            break

        else:
            print("Opción no válida. Pierdes el turno.")

    if vida_enemigo <= 0:
        puntos = 100
        print("\n¡Victoria! Derrotaste al enemigo.")
    elif vida_jugador <= 0:
        print("\nTe quedaste sin vida.")
    elif escapaste:
        print("\nEscapaste sin obtener puntos.")
    else:
        print("\nSe acabaron los turnos.")

    print("Puntos obtenidos:", puntos)

# MISIÓN 3: BUSCAR EL TESORO
elif mision == "Encontrar un tesoro":
    tesoro_x = random.randint(1, 50)
    tesoro_y = random.randint(1, 50)

    print("\n¡Encuentra el tesoro!")
    print("El tesoro está entre las coordenadas 1 y 50.")
    print("Tienes 10 intentos.")

    for i in range(10):
        x = int(input("Coordenada X: "))
        y = int(input("Coordenada Y: "))

        if x == tesoro_x and y == tesoro_y:
            puntos = 200
            print("\n¡ENCONTRASTE EL TESORO!")
            break

        distancia = abs(x - tesoro_x) + abs(y - tesoro_y)

        if distancia <= 3:
            print("¡Muy cerca!")
        elif distancia <= 8:
            print("Cerca")
        elif distancia <= 15:
            print("Lejos")
        else:
            print("¡Muy lejos!")

        print("Intentos restantes:", 9 - i)

    if puntos == 0:
        print("\nNo encontraste el tesoro.")
        print("El tesoro estaba en:", tesoro_x, "X y en", tesoro_y, "Y")

    print("Puntos obtenidos:", puntos)

print("\n=== FIN DE LA MISIÓN ===")
print("Jugador:", nombre)
print("Puntuación final:", puntos)

