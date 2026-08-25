import random

scr = random.randint(1, 100)

print("Hay un número secreto del 1 al 100, ¡buena suerte adivinándolo!")

while True:
    intento = int(input("Seleccione el número que cree que sea el número secreto: "))

    if intento > 100:
        print("Es un número entre el 1 y el 100, no por encima del 100")

    elif intento < 1:
        print("Es un número positivo y es del 1 al 100, no por debajo del 1")

    elif intento == scr:
        print("¡CORRECTO! ¡ADIVINASTE, FELICIDADES!")
        break

    else:
        dif = abs(intento - scr)

        if dif <= 2:
            print("¡Estás muy cerca!")

        elif dif <= 5:
            print("¡Estás cerca!")

        elif dif <= 10:
            print("Estás algo cerca")

        elif dif <= 15:
            print("Estás lejos")

        else:
            print("Estás muy lejos")
