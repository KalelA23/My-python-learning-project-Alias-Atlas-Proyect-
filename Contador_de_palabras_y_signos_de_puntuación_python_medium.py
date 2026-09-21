while True:
    opccion = int(input("Marque 1 para salir, marque 0 para continuar: "))

    if opccion == 0:
        print("Seleccione una palabra a su decisión y le indicaré cuántas letras, espacios y signos de puntuación tiene")
        palabra = input("Seleccione: ")

        longitud1 = len(palabra)
        longitud2 = palabra.count(" ")
        longitud3 = palabra.count("!")
        longitud4 = palabra.count("?")

        print("Hay", longitud1, "caracteres")
        print("Hay", longitud2, "espacios")
        print("Hay", longitud3, "signos de exclamación")
        print("Hay", longitud4, "signos de interrogación")

    if opccion == 1:
        break