while True:
    print("EXAMEN DE PYTHON ATLAS")
    print("1.- Respuesta abierta")
    print("2.- Respuesta cerrada")
    print("3.- Salir")

    tipo_respuesta = int(input("Escoga: "))

    if tipo_respuesta == 1:
        pregunta1 = input("¿Qué función tiene el comando print en python?")
        pregunta1 = pregunta1.lower()
        if pregunta1 == "para imprimir texto":
            pregunta1 = 10
        else:
            pregunta1 = 0

        pregunta2 = input("¿Qué comando permite agregar datos en python?")
        pregunta2 = pregunta2.lower()
        if pregunta2 == "input":
            pregunta2 = 10
        else:
            pregunta2 = 0

        pregunta3 = input("¿Qué extensión le permite al usuario agregar números a su respuesta?")
        pregunta3 = pregunta3.lower()
        if pregunta3 == "int":
            pregunta3 = 10
        else:
            pregunta3 = 0

        pregunta4 = input("¿Qué comando se usa para crear una condición en python?")
        pregunta4 = pregunta4.lower()
        if pregunta4 == "if" or pregunta4 == "elif":
            pregunta4 = 20
        else:
            pregunta4 = 0

        pregunta5 = input("¿Qué comando es usado para convertir los textos a minusculas?")
        pregunta5 = pregunta5.lower()
        if pregunta5 == "lower" or pregunta5 == "el comando lower" or pregunta5 == "el lower":
            pregunta5 = 20
        else:
            pregunta5 = 0

    if tipo_respuesta == 2:
        print("1.- ¿Qué función tiene el comando print en python?")
        print("a) Agregar datos")
        print("b) Imprimir texto")
        print("c) Convertir números")
        pregunta1 = input("Escoga: ")
        if pregunta1 == "b":
            pregunta1 = 10
        else:
            pregunta1 = 0

        print("2.- ¿Qué comando permite agregar datos en python?")
        print("a) El comando if")
        print("b) El comando input")
        print("c) El comando print")
        pregunta2 = input("Escoga: ")
        if pregunta2 == "b":
            pregunta2 = 10
        else:
            pregunta2 = 0

        print("3.- ¿Qué extensión le permite al usuario agregar números a su respuesta?")
        print("a) str")
        print("b) int")
        print("c) float")
        pregunta3 = input("Escoga: ")
        if pregunta3 == "b":
            pregunta3 = 10
        else:
            pregunta3 = 0

        print("4.- ¿Qué comando se usa para crear una condición en python?")
        print("a) if")
        print("b) input")
        print("c) print")
        pregunta4 = input("Escoga: ")
        if pregunta4 == "a":
            pregunta4 = 20
        else:
            pregunta4 = 0

        print("5.- ¿Qué comando es usado para convertir los textos a minusculas?")
        print("a) upper")
        print("b) lower")
        print("c) int")
        pregunta5 = input("Escoga: ")
        if pregunta5 == "b":
            pregunta5 = 20
        else:
            pregunta5 = 0

    if tipo_respuesta == 3:
        break

    if tipo_respuesta == 1 or tipo_respuesta == 2:
        total = pregunta1 + pregunta2 + pregunta3 + pregunta4 + pregunta5
        print("Su puntuaje es de", total, "/100")

        if total >= 80:
            print("Por encima del promedio")
        elif total >= 70:
            print("Promedio")
        else:
            print("Debajo del promedio")