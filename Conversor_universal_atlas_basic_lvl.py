while True:
    print("=== CONVERSOR ATLAS ===")
    print("1. Temperatura")
    print("2. Longitud")
    print("3. Peso")
    print("4. Tiempo")
    print("5. Salir")

    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        print("1. Celsius a Fahrenheit")
        print("2. Fahrenheit a Celsius")
        print("3. Celsius a Kelvin")
        print("4. Kelvin a Celsius")

        conversion1 = int(input("Elige: "))

        if conversion1 == 1:
            celsius = float(input("Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print(fahrenheit)

        elif conversion1 == 2:
            fahrenheit = float(input("Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5/9
            print(celsius)

        elif conversion1 == 3:
            celsius = float(input("Celsius: "))
            kelvin = celsius + 273.15
            print(kelvin)

        elif conversion1 == 4:
            kelvin = float(input("Kelvin: "))
            celsius = kelvin - 273.15
            print(celsius)

    elif opcion == 2:
        print("1. De kilómetros a metros")
        print("2. De metros a kilómetros")
        print("3. De kilómetros a millas")
        print("4. De millas a kilómetros")

        conversion2 = int(input("Elige: "))

        if conversion2 == 1:
            kilometros = float(input("Kilómetros: "))
            metros = kilometros * 1000
            print(metros)

        elif conversion2 == 2:
            metros = float(input("Metros: "))
            kilometros = metros / 1000
            print(kilometros)

        elif conversion2 == 3:
            kilometros = float(input("Kilómetros: "))
            millas = kilometros / 1.6093
            print(millas)

        elif conversion2 == 4:
            millas = float(input("Millas: "))
            kilometros = millas * 1.6093
            print(kilometros)

    elif opcion == 3:
        print("1. De kilos a gramos")
        print("2. De gramos a kilos")
        print("3. De kilos a toneladas")
        print("4. De toneladas a kilos")

        conversion3 = int(input("Elige: "))

        if conversion3 == 1:
            kilogramos = float(input("Kilogramos: "))
            gramos = kilogramos * 1000
            print(gramos)

        elif conversion3 == 2:
            gramos = float(input("Gramos: "))
            kilogramos = gramos / 1000
            print(kilogramos)

        elif conversion3 == 3:
            kilogramos = float(input("Kilogramos: "))
            toneladas = kilogramos / 1000
            print(toneladas)

        elif conversion3 == 4:
            toneladas = float(input("Toneladas: "))
            kilogramos = toneladas * 1000
            print(kilogramos)

    elif opcion == 4:
        print("1. De horas a minutos")
        print("2. De minutos a horas")
        print("3. De horas a días")
        print("4. De días a horas")

        conversion4 = int(input("Elige: "))

        if conversion4 == 1:
            horas = float(input("Horas: "))
            minutos = horas * 60
            print(minutos)

        elif conversion4 == 2:
            minutos = float(input("Minutos: "))
            horas = minutos / 60
            print(horas)

        elif conversion4 == 3:
            horas = float(input("Horas: "))
            dias = horas / 24
            print(dias)

        elif conversion4 == 4:
            dias = float(input("Días: "))
            horas = dias * 24
            print(horas)

    elif opcion == 5:
        break

    else:
        print("Escoge una opción válida")