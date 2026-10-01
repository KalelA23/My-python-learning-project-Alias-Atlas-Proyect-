while True:
    continuar = input("1.- Salir\n2.- Continuar\nSeleccione una opción: ")

    if continuar == "1":
        break

    elif continuar == "2":
        oracion = input("Introduzca la oración o palabra: ")
        alfabeto = "abcdefghijklmnopqrstuvwxyz"

        for letra in alfabeto:
            cantidad = oracion.lower().count(letra)

            if cantidad > 0:
                print(letra, ":", cantidad, "veces")

    else:
        print("Opción no válida")