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

sentimientos = [
    "estoy bien",
    "me encuentro bien",
    "bien, supongo",
    "no me va nada mal"
]

musica_feliz = [
    "música pop animada",
    "rock energético",
    "música electrónica",
    "funk"
]

musica_triste = [
    "música tranquila",
    "lo-fi",
    "piano instrumental",
    "música acústica"
]

musica_enojado = [
    "rock pesado",
    "metal",
    "rap",
    "música electrónica intensa"
]

musica_neutral = [
    "lo-fi",
    "pop",
    "rock alternativo",
    "música instrumental"
]

contenido_feliz = [
    "Shrek",
    "Los Minions",
    "una comedia",
    "una película de aventuras"
]

contenido_triste = [
    "Intensamente",
    "una película reconfortante",
    "una serie tranquila",
    "una película de animación"
]

contenido_enojado = [
    "una película de acción",
    "una película de superhéroes",
    "una comedia para distraerte",
    "una serie de acción"
]

contenido_neutral = [
    "una película de ciencia ficción",
    "una serie de misterio",
    "una película de aventuras",
    "un documental interesante"
]


nombre_chatbot = "Chat bot"
nombre_usuario = "Usuario"


while True:

    usuario = input(nombre_usuario + ": ")
    usuario = usuario.lower()
    usuario = usuario.replace("¡", "").replace("!", "").replace("¿", "").replace("?", "")

    # SALUDOS
    if usuario == "hola" or usuario == "alo" or usuario == "ola" or usuario == "holaa":

        print(nombre_chatbot + ":", random.choice(saludos))
        print(nombre_chatbot + ": ¿Cómo estás,", nombre_usuario + "?")

        sentimiento_usuario = input(nombre_usuario + ": ")
        sentimiento_usuario = sentimiento_usuario.lower()

        if sentimiento_usuario == "bien" or sentimiento_usuario == "estoy bien" or sentimiento_usuario == "feliz":

            print(nombre_chatbot + ": Me alegra que estés bien,", nombre_usuario + ".")
            print(nombre_chatbot + ": ¿Qué te gustaría hacer?")

        elif sentimiento_usuario == "mal" or sentimiento_usuario == "triste" or sentimiento_usuario == "enojado":

            print(nombre_chatbot + ": Qué mal,", nombre_usuario + ".")
            print(nombre_chatbot + ": Espero que las cosas mejoren.")
            print(nombre_chatbot + ": ¿Quieres hablar de otra cosa?")

        else:

            print(nombre_chatbot + ": Entiendo,", nombre_usuario + ".")
            print(nombre_chatbot + ": ¿Qué te gustaría hacer?")


    # NOMBRE DEL CHATBOT
    elif usuario == "como te llamas" or usuario == "cual es tu nombre" or usuario == "dime tu nombre":

        if nombre_chatbot == "Chat bot":

            print(nombre_chatbot + ": Aún no tengo un nombre personalizado.")

            respuesta = input(nombre_chatbot + ": ¿Quieres ponerme un nombre? ")
            respuesta = respuesta.lower()

            if respuesta == "si" or respuesta == "sí":

                nombre = input(nombre_chatbot + ": ¿Qué nombre quieres ponerme? ")

                if nombre.strip() == "":

                    print(nombre_chatbot + ": No escribiste ningún nombre.")
                    print(nombre_chatbot + ": Seguiré siendo Chat bot.")

                else:

                    nombre_chatbot = nombre.strip()

                    print(nombre_chatbot + ": ¡Perfecto! Ahora me llamaré", nombre_chatbot + ".")
                    print(nombre_chatbot + ": Y ahora que tenemos mi nombre, ¿cuál es el tuyo?")

                    nuevo_nombre = input(nombre_usuario + ": ")

                    if nuevo_nombre.strip() == "":

                        print(nombre_chatbot + ": Está bien, seguiré llamándote Usuario.")

                    else:

                        nombre_usuario = nuevo_nombre.strip()

                        print(nombre_chatbot + ": Mucho gusto,", nombre_usuario + ".")
                        print(nombre_chatbot + ": Ahora ya tenemos nuestros nombres.")

            elif respuesta == "no":

                print(nombre_chatbot + ": Está bien, seguiré siendo Chat bot.")

            else:

                print(nombre_chatbot + ": No entendí tu respuesta.")
                print(nombre_chatbot + ": Seguiré siendo Chat bot.")

        else:

            print(nombre_chatbot + ": Yo me llamo", nombre_chatbot + ".")
            print(nombre_chatbot + ": ¿Te gusta mi nombre?")

            respuesta = input(nombre_usuario + ": ")
            respuesta = respuesta.lower()

            if respuesta == "si" or respuesta == "sí" or respuesta == "me gusta":

                print(nombre_chatbot + ": Me alegra que te guste.")

            elif respuesta == "no" or respuesta == "no me gusta":

                print(nombre_chatbot + ": Bueno, siempre podemos cambiarlo.")

            else:

                print(nombre_chatbot + ": Entiendo.")


    # NOMBRE DEL USUARIO
    elif usuario == "como me llamo" or usuario == "cual es mi nombre":

        print(nombre_chatbot + ": Tu nombre es", nombre_usuario + ".")
        print(nombre_chatbot + ": ¿Quieres cambiarlo?")

        respuesta = input(nombre_usuario + ": ")
        respuesta = respuesta.lower()

        if respuesta == "si" or respuesta == "sí":

            nuevo_nombre = input(nombre_chatbot + ": ¿Cómo quieres que te llame? ")

            if nuevo_nombre.strip() == "":

                print(nombre_chatbot + ": No escribiste ningún nombre.")

            else:

                nombre_usuario = nuevo_nombre.strip()

                print(nombre_chatbot + ": Perfecto. Ahora te llamaré", nombre_usuario + ".")

        elif respuesta == "no":

            print(nombre_chatbot + ": Está bien,", nombre_usuario + ".")

        else:

            print(nombre_chatbot + ": No entendí tu respuesta.")


    # CAMBIAR NOMBRE DEL USUARIO
    elif usuario == "quiero cambiar mi nombre" or usuario == "cambiar mi nombre":

        print(nombre_chatbot + ": Claro,", nombre_usuario + ".")

        nuevo_nombre = input(nombre_chatbot + ": ¿Cómo quieres que te llame? ")

        if nuevo_nombre.strip() == "":

            print(nombre_chatbot + ": No escribiste ningún nombre.")

        else:

            nombre_usuario = nuevo_nombre.strip()

            print(nombre_chatbot + ": Perfecto. Ahora te llamaré", nombre_usuario + ".")


    # DECIRLE EL NOMBRE AL CHATBOT
    elif usuario == "quiero decirte mi nombre" or usuario == "mi nombre":

        nuevo_nombre = input(nombre_chatbot + ": ¿Cómo te llamas? ")

        if nuevo_nombre.strip() == "":

            print(nombre_chatbot + ": Está bien, seguiré llamándote Usuario.")

        else:

            nombre_usuario = nuevo_nombre.strip()

            print(nombre_chatbot + ": Mucho gusto,", nombre_usuario + ".")
            print(nombre_chatbot + ": Ahora recordaré tu nombre mientras el programa esté funcionando.")


    # PYTHON
    elif usuario == "que es python" or usuario == "python":

        print(nombre_chatbot + ": Python es un lenguaje de programación.")
        print(nombre_chatbot + ": Se utiliza para crear programas, juegos, aplicaciones, automatizaciones y mucho más.")
        print(nombre_chatbot + ": ¿Quieres hacer una operación matemática?")

        respuesta = input(nombre_usuario + ": ")
        respuesta = respuesta.lower()

        if respuesta == "si" or respuesta == "sí":

            print(nombre_chatbot + ": Puedes escribir suma, resta, multiplicacion, division, potencia o raiz.")

        elif respuesta == "no":

            print(nombre_chatbot + ": Está bien.")

        else:

            print(nombre_chatbot + ": No entendí tu respuesta.")


    # COMO ESTA
    elif usuario == "como estas" or usuario == "que pasa":

        print(
            nombre_chatbot + ":",
            random.choice(sentimientos),
            "aunque realmente no siento nada, porque soy un chatbot."
        )

        print(nombre_chatbot + ": ¿Y tú cómo estás,", nombre_usuario + "?")

        sentimiento_usuario = input(nombre_usuario + ": ")
        sentimiento_usuario = sentimiento_usuario.lower()

        if sentimiento_usuario == "bien" or sentimiento_usuario == "estoy bien" or sentimiento_usuario == "feliz":

            print(nombre_chatbot + ": Es bueno que estés bien,", nombre_usuario + ".")
            print(nombre_chatbot + ": En base a tu humor te recomendaría ver una película de Minions.")

        elif sentimiento_usuario == "mal" or sentimiento_usuario == "triste" or sentimiento_usuario == "enojado":

            print(nombre_chatbot + ": Qué mal,", nombre_usuario + ".")
            print(nombre_chatbot + ": Te recomendaría una película divertida. ¿Qué tal Shrek?")

        else:

            print(nombre_chatbot + ": Mmmmm, no sé muy bien qué película recomendarte.")
            print(nombre_chatbot + ": ¿Qué tal Intensamente?")


    # QUE PUEDE HACER
    elif usuario == "que puedes hacer" or usuario == "que mas puedes hacer":

        print(nombre_chatbot + ": Puedo hacer varias cosas.")
        print(nombre_chatbot + ": Puedo hacer operaciones matemáticas, guardar tu nombre y jugar contigo.")
        print(nombre_chatbot + ": También puedo responder algunas preguntas.")
        print(nombre_chatbot + ": Puedo recomendarte música y contenido audiovisual según cómo estés.")
        print(nombre_chatbot + ": También puedo preguntarte cómo estás y darte recomendaciones.")
        print(nombre_chatbot + ": ¿Quieres probar alguna función?")

        respuesta = input(nombre_usuario + ": ")
        respuesta = respuesta.lower()

        if respuesta == "si" or respuesta == "sí":

            print(nombre_chatbot + ": Puedes intentar decirme suma, resta, multiplicacion, division, potencia, raiz, juego o recomendacion.")

        elif respuesta == "no":

            print(nombre_chatbot + ": Está bien.")

        else:

            print(nombre_chatbot + ": Puedes decirme directamente qué quieres hacer.")


    # SUMA
    elif usuario == "suma":

        suma1 = int(input(nombre_chatbot + ": Dame un número: "))
        suma2 = int(input(nombre_chatbot + ": Dame otro número: "))

        suma3 = suma1 + suma2

        print(nombre_chatbot + ": El resultado es", suma3)
        print(nombre_chatbot + ": ¿Quieres hacer otra operación?")


    # RESTA
    elif usuario == "resta":

        resta1 = int(input(nombre_chatbot + ": Dame un número: "))
        resta2 = int(input(nombre_chatbot + ": Dame otro número: "))

        resta3 = resta1 - resta2

        print(nombre_chatbot + ": El resultado es", resta3)
        print(nombre_chatbot + ": Bastante sencillo.")


    # MULTIPLICACIÓN
    elif usuario == "multiplicacion" or usuario == "multiplicación":

        multi1 = int(input(nombre_chatbot + ": Dame un número: "))
        multi2 = int(input(nombre_chatbot + ": Dame otro número: "))

        multi3 = multi1 * multi2

        print(nombre_chatbot + ": El resultado es", multi3)


    # DIVISIÓN
    elif usuario == "division" or usuario == "división":

        divi1 = int(input(nombre_chatbot + ": Dame el dividendo: "))
        divi2 = int(input(nombre_chatbot + ": Dame el divisor: "))

        if divi2 == 0:

            print(nombre_chatbot + ": No se puede dividir entre cero.")

        else:

            divi3 = divi1 / divi2

            print(nombre_chatbot + ": El resultado es", divi3)


    # POTENCIA
    elif usuario == "potencia":

        pote1 = int(input(nombre_chatbot + ": Dame la base: "))
        pote2 = int(input(nombre_chatbot + ": Dame el exponente: "))

        pote3 = pote1 ** pote2

        print(nombre_chatbot + ": El resultado es", pote3)


    # RAÍZ
    elif usuario == "raiz" or usuario == "raíz":

        raiz1 = int(input(nombre_chatbot + ": Dame un número: "))

        if raiz1 < 0:

            print(nombre_chatbot + ": No puedo calcular la raíz cuadrada de un número negativo.")

        else:

            raiz2 = math.sqrt(raiz1)

            print(nombre_chatbot + ": El resultado es", raiz2)


    # JUEGO
    elif usuario == "jugar" or usuario == "juego":

        tipo_juego = input(
            nombre_chatbot + ": Ok, jugaremos. Escoge entre piedra papel o tijera o adivina el numero: "
        )

        tipo_juego = tipo_juego.lower()

        if tipo_juego == "piedra papel o tijera":

            print(nombre_chatbot + ": Ok,", nombre_usuario + ", jugaremos piedra, papel o tijera.")

            jugador = input(nombre_usuario + ": ")
            jugador = jugador.lower()

            if jugador not in opciones:

                print(nombre_chatbot + ": Esa opción no es válida.")

            else:

                Chat = random.choice(opciones)

                print(nombre_chatbot + ": Yo elegí", Chat)

                if jugador == Chat:

                    print(nombre_chatbot + ": ¡Es un empate!")

                elif (jugador == "piedra" and Chat == "tijera") or \
                     (jugador == "papel" and Chat == "piedra") or \
                     (jugador == "tijera" and Chat == "papel"):

                    print(nombre_chatbot + ": ¡Ganaste,", nombre_usuario + "!")

                else:

                    print(nombre_chatbot + ": ¡Yo gano!")


        elif tipo_juego == "adivina el numero":

            print(
                nombre_chatbot + ": Ok,", nombre_usuario +
                ", jugaremos adivina el número."
            )

            print(
                nombre_chatbot +
                ": Tienes 3 intentos para adivinar un número entre 1 y 10. ¡Suerte!"
            )

            numero_secreto = random.randint(1, 10)

            for intento in range(1, 4):

                adivinar = int(input(nombre_usuario + ": "))

                if adivinar == numero_secreto:

                    print(
                        nombre_chatbot + ": ¡Ganaste en el intento #",
                        intento
                    )

                    break

                elif adivinar < numero_secreto:

                    print(nombre_chatbot + ": Mi número es mayor.")

                else:

                    print(nombre_chatbot + ": Mi número es menor.")

                if intento == 3:

                    print(
                        nombre_chatbot + ": Se acabaron tus intentos.",
                        "Yo había elegido el número",
                        numero_secreto
                    )


        else:

            print(nombre_chatbot + ": No reconocí ese juego.")


    # RECOMENDACIONES
    elif usuario == "recomendacion" or usuario == "recomendaciones" or usuario == "recomiendame algo":

        print(nombre_chatbot + ": Claro,", nombre_usuario + ".")
        print(nombre_chatbot + ": Primero dime cómo estás.")
        print(nombre_chatbot + ": Puedes decirme bien, feliz, triste, enojado o algo diferente.")

        estado = input(nombre_usuario + ": ")
        estado = estado.lower()

        if estado == "bien" or estado == "feliz":

            musica = random.choice(musica_feliz)
            contenido = random.choice(contenido_feliz)

            print(nombre_chatbot + ": Ya que estás", estado + ",")
            print(nombre_chatbot + ": Te recomiendo escuchar", musica + ".")
            print(nombre_chatbot + ": Y para ver, podrías probar", contenido + ".")


        elif estado == "triste":

            musica = random.choice(musica_triste)
            contenido = random.choice(contenido_triste)

            print(nombre_chatbot + ": Si estás triste, podemos buscar algo más tranquilo.")
            print(nombre_chatbot + ": Te recomiendo escuchar", musica + ".")
            print(nombre_chatbot + ": Para ver, podrías probar", contenido + ".")


        elif estado == "enojado":

            musica = random.choice(musica_enojado)
            contenido = random.choice(contenido_enojado)

            print(nombre_chatbot + ": Si estás enojado, quizá te ayude algo con más energía.")
            print(nombre_chatbot + ": Te recomiendo escuchar", musica + ".")
            print(nombre_chatbot + ": Para ver, podrías probar", contenido + ".")


        else:

            musica = random.choice(musica_neutral)
            contenido = random.choice(contenido_neutral)

            print(nombre_chatbot + ": No estoy seguro de cómo te sientes.")
            print(nombre_chatbot + ": Así que te daré una recomendación neutral.")
            print(nombre_chatbot + ": Te recomiendo escuchar", musica + ".")
            print(nombre_chatbot + ": Para ver, podrías probar", contenido + ".")


    # SALIR
    elif usuario == "off":

        print(nombre_chatbot + ": ¡Hasta luego,", nombre_usuario + "!")
        break


    # NO ENTENDIÓ
    else:

        print(nombre_chatbot + ": No entendí lo que dijiste,", nombre_usuario + ".")
        print(nombre_chatbot + ": Puedes intentar decirme algo como hola, juego, suma, recomendacion o qué puedes hacer.")