while True:
    print("\nEXAMEN DE PYTHON ATLAS")
    print("1.- Respuesta abierta")
    print("2.- Respuesta cerrada")
    print("3.- Salir")

    tipo = input("Escoge: ")

    if tipo == "3":
        break
    if tipo not in ["1", "2"]:
        print("Opción no válida")
        continue

    preguntas = [
        "¿Qué hace print en Python?",
        "¿Qué comando permite ingresar datos?",
        "¿Qué convierte un dato a entero?",
        "¿Qué comando crea una condición?",
        "¿Qué convierte texto a minúsculas?"
    ]

    respuestas = ["imprimir texto", "input", "int", "if", "lower"]
    letras = ["b", "b", "b", "a", "b"]
    puntos = [20, 20, 20, 20, 20]
    total = 0

    for i in range(5):
        print("\n", i + 1, preguntas[i])

        if tipo == "2":
            opciones = [
                ["a) Ingresar datos", "b) Imprimir texto", "c) Convertir números"],
                ["a) if", "b) input", "c) print"],
                ["a) str", "b) int", "c) float"],
                ["a) if", "b) input", "c) print"],
                ["a) upper", "b) lower", "c) int"]
            ]

            for opcion in opciones[i]:
                print(opcion)

            respuesta = input("Escoge: ").lower()
            if respuesta == letras[i]:
                total += puntos[i]

        else:
            respuesta = input("Respuesta: ").lower()
            if respuestas[i] in respuesta:
                total += puntos[i]

    print("\nPuntaje:", total, "/100")

    if total >= 56:
        print("Por encima del promedio")
    elif total >= 49:
        print("Promedio")
    else:
        print("Debajo del promedio")
