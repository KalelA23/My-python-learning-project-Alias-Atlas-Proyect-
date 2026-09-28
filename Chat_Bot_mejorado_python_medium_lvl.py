from datetime import datetime
import math
import random

saludos = [
    "¡Hola!",
    "¡Qué onda!",
    "¡Hola! ¿Cómo estás?",
    "¡Bienvenido!"
]

opciones = [
    "piedra",
    "papel",
    "tijera"
]

while True:
    usuario = input("Usuario: ")
    usuario = usuario.lower()
    usuario = usuario.replace("¡", "").replace("!", "").replace("¿", "").replace("?", "")

    if usuario == "hola":
        print("Chat bot:", random.choice(saludos), "Soy un chatbot en desarrollo, espero ayudar en todo lo posible.")

    elif usuario == "que es python" or usuario == "python":
        print("Chat bot: Python es un lenguaje de programación que es usado en todo el mundo.")

    elif usuario == "como te llamas" or usuario == "cual es tu nombre":
        print("Chat bot: Mi nombre aún no está muy definido. Si quieres, puedes darme una sugerencia de cómo llamarme.")
        nombre = input("Nombre sugerido: ")

        if nombre.strip() == "":
            print("Chat bot: Está bien, buscaré yo mismo un nombre para mí.")
        else:
            print("Chat bot: ¡Wow, qué gran nombre! Me llamo", nombre, "¡Mucho gusto!")

    elif usuario == "que puedes hacer" or usuario == "que mas puedes hacer":
        print("Chat bot: Puedo hacer operaciones matemáticas, darte la hora actual, guardar tus datos y jugar contigo.")

    elif usuario == "suma":
        suma1 = int(input("Dame un número: "))
        suma2 = int(input("Dame otro número: "))
        suma3 = suma1 + suma2
        print("Chat bot: El resultado es", suma3)

    elif usuario == "resta":
        resta1 = int(input("Dame un número: "))
        resta2 = int(input("Dame otro número: "))
        resta3 = resta1 - resta2
        print("Chat bot: El resultado es", resta3)

    elif usuario == "multiplicacion" or usuario == "multiplicación":
        multi1 = int(input("Dame un número: "))
        multi2 = int(input("Dame otro número: "))
        multi3 = multi1 * multi2
        print("Chat bot: El resultado es", multi3)

    elif usuario == "division" or usuario == "división":
        divi1 = int(input("Dame el dividendo: "))
        divi2 = int(input("Dame el divisor: "))

        if divi2 == 0:
            print("Chat bot: No se puede dividir entre cero.")
        else:
            divi3 = divi1 / divi2
            print("Chat bot: El resultado es", divi3)

    elif usuario == "potencia":
        pote1 = int(input("Dame la base: "))
        pote2 = int(input("Dame el exponente: "))
        pote3 = pote1 ** pote2
        print("Chat bot: El resultado es", pote3)

    elif usuario == "raiz" or usuario == "raíz":
        raiz1 = int(input("Dame un número: "))

        if raiz1 < 0:
            print("Chat bot: No puedo calcular la raíz cuadrada de un número negativo.")
        else:
            raiz2 = math.sqrt(raiz1)
            print("Chat bot: El resultado es", raiz2)

    elif usuario == "hora" or usuario == "hora actual":
        hora = datetime.now().strftime("%H:%M")
        print("Chat bot: La hora actual es", hora)

    elif usuario == "jugar" or usuario == "juego":
        Chat = random.choice(opciones)

        print("Chat bot: Ok, jugaremos piedra, papel o tijera.")
        jugador = input("Jugador: ")
        jugador = jugador.lower()

        if jugador not in opciones:
            print("Chat bot: Esa opción no es válida.")
        elif jugador == Chat:
            print("Chat bot: Yo elegí", Chat)
            print("Chat bot: ¡Es un empate!")
        elif (jugador == "piedra" and Chat == "tijera") or \
             (jugador == "papel" and Chat == "piedra") or \
             (jugador == "tijera" and Chat == "papel"):
            print("Chat bot: Yo elegí", Chat)
            print("Chat bot: ¡Ganaste!")
        else:
            print("Chat bot: Yo elegí", Chat)
            print("Chat bot: ¡Yo gano!")

    elif usuario == "salir":
        print("Chat bot: ¡Hasta luego!")
        break

    else:
        print("Chat bot: No entendí lo que dijiste.")