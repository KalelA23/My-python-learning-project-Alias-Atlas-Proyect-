while True:
    print("Corrector gramatical ATLAS")
    print("1.- Convertir a minusculas")
    print("2.- Convertir a mayusculas")
    print("3.- Quitar espacios")
    print("4.- Agregar mayuscula a la primer letra de la oracion")
    print("5.- Agregar mayuscula a la primera letra de cada palabra")
    print("6.- Contar las apariciones de una palabra o letra")
    print("7.- Encontrar la posicion de una palabra o letra")
    print("8.- Remplazar algo de una oracion o palabra")
    print("9.- Salir")

    opcion = input("Escoja en numeros su opcion: ")

    if opcion == "1":
        palabra_minuscula = input(
            "Escriba la palabra u oracion que quiera convertir a minuscula: "
        )
        palabra_minuscula = palabra_minuscula.lower()
        print(palabra_minuscula)

    elif opcion == "2":
        palabra_mayuscula = input(
            "Escriba la palabra u oracion que quiera convertir a mayuscula: "
        )
        palabra_mayuscula = palabra_mayuscula.upper()
        print(palabra_mayuscula)

    elif opcion == "3":
        quitar_espacio = input(
            "Escriba la oracion a la que le quiera quitar los espacios: "
        )
        quitar_espacio = quitar_espacio.strip()
        print(quitar_espacio)

    elif opcion == "4":
        agregar_mayus = input(
            "Escriba la palabra u oracion a la que le quiera agregar una mayuscula: "
        )
        agregar_mayus = agregar_mayus.capitalize()
        print(agregar_mayus)

    elif opcion == "5":
        primer_letra = input(
            "Escriba la palabra u oracion a la que quiera identificar sus primeras letras: "
        )
        primer_letra = primer_letra.title()
        print(primer_letra)

    elif opcion == "6":
        contador_palabra = input("Escriba la palabra u oracion: ")
        contar = input("Escriba que quiere contar: ")
        contador = contador_palabra.count(contar)
        print("La palabra o letra", contar, "aparece", contador, "veces")

    elif opcion == "7":
        posicion_palabra = input("Escriba la palabra u oracion: ")
        posicion = input("Escriba que palabra o letra quiere encontrar: ")
        posiciones = posicion_palabra.find(posicion)
        print("La palabra o letra", posicion, "se encuentra en la posicion", posiciones)

    elif opcion == "8":
        remplazar_palabra = input("Escriba la palabra u oracion: ")
        remplazar = input("Escriba que palabra quiere remplazar: ")
        remplazo = input("Escriba con que quiere remplazarlo: ")
        remplazado = remplazar_palabra.replace(remplazar, remplazo)
        print(remplazado)

    elif opcion == "9":
        break

    else:
        print("Escoja una opcion valida")