from datetime import datetime

while True:
    mensaje = input("Tu:  ")

    if mensaje == "hola":
        print("Bot: ¡Hola! ¿Cómo estás?")

    elif mensaje == "bien":
        print("Bot: ¡Me alegra!")

    elif mensaje == "mal":
        print("Bot: Lo siento por ti, espero estés mejor pronto")

    elif mensaje == "que puedes hacer":
        print("Bot: Puedo responder algunas preguntas por ahora sigo en desarrollo.")

    elif mensaje == "que tipo de preguntas":
        print("Bot: Por ahora puedo responder una cantidad limitada de preguntas, pero puedo hacer suma, resta y dar la hora actual")

    elif mensaje == "suma":
        su1 = int(input("Bot: Dame un numero: "))
        su2 = int(input("Bot: Dame otro numero: "))
        sum = su1 + su2
        print("Bot: El resultado de esta operacion es:", sum)

    elif mensaje == "resta":
        re1 = int(input("Bot: Dame un numero: "))
        re2 = int(input("Bot: Dame otro numero: "))
        res = re1 - re2
        print("Bot: El resultado de esta operacion es:", res)

    elif mensaje == "cual es tu comida favorita":
        print("Bot: No te sabria decir, nunca he probado la comida, pero me gustaria probar la pizza")

    elif mensaje == "cual es tu color favorito":
        print("Bot: Posiblemente el azul o morado")

    elif mensaje == "hora":
        hora = datetime.now()
        print(f"Bot: Son las {hora.hour}:{hora.minute:02d}")

    elif mensaje == "salir":
        print("Bot: ¡Hasta luego!")
        break

    else:
        print("Bot: No entiendo esa pregunta, lo siento.")