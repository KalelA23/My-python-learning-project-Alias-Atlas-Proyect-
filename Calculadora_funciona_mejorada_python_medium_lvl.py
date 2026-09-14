import math

while True:
    print("\nCALCULADORA ATLAS")

    print("1.- SUMA")
    print("2.- RESTA")
    print("3.- DIVISION")
    print("4.- MULTIPLICACION")
    print("5.- RAIZ CUADRADA")
    print("6.- POTENCIA")
    print("7.- ECUACION PRIMER GRADO")
    print("8.- ECUACION CON POTENCIA")
    print("9.- PORCENTAJES")
    print("10.- TRIGONOMETRIA")
    print("11.- FORMULAS")
    print("12.- SALIR")

    opccion = int(input("Seleccione una: "))

    if opccion == 1:
        suma1 = float(input("Seleccione un numero: "))
        suma2 = float(input("Seleccione otro numero: "))
        suma3 = suma1 + suma2
        print("Resultado:", suma3)

    elif opccion == 2:
        resta1 = float(input("Seleccione un numero: "))
        resta2 = float(input("Seleccione otro numero: "))
        resta3 = resta1 - resta2
        print("Resultado:", resta3)

    elif opccion == 3:
        division1 = float(input("Seleccione el dividendo: "))
        division2 = float(input("Seleccione el divisor: "))

        if division2 != 0:
            division3 = division1 / division2
            print("Resultado:", division3)
        else:
            print("No se puede dividir entre 0.")

    elif opccion == 4:
        multiplicacion1 = float(input("Seleccione un numero: "))
        multiplicacion2 = float(input("Seleccione otro numero: "))
        multiplicacion3 = multiplicacion1 * multiplicacion2
        print("Resultado:", multiplicacion3)

    elif opccion == 5:
        raizcuadrada1 = float(input("Seleccione un numero: "))

        if raizcuadrada1 >= 0:
            raizcuadrada2 = math.sqrt(raizcuadrada1)
            print("Resultado:", raizcuadrada2)
        else:
            print("No se puede sacar la raiz de un numero negativo.")

    elif opccion == 6:
        potencia1 = float(input("Seleccione la base: "))
        potencia2 = float(input("Seleccione el exponente: "))
        potencia3 = potencia1 ** potencia2
        print("Resultado:", potencia3)

    elif opccion == 7:
        print("\nECUACION DE PRIMER GRADO")
        print("Forma: a + bx = c")

        algebra1 = float(input("Seleccione el valor de a: "))
        algebra2 = float(input("Seleccione el coeficiente de x: "))
        algebra3 = float(input("Seleccione el resultado: "))

        algebra5 = (algebra3 - algebra1) / algebra2

        print("x =", algebra5)

    elif opccion == 8:
        print("\nECUACION CON POTENCIA")
        print("Forma: x^2 = resultado")

        ecupo1 = float(input("Seleccione el resultado de la ecuacion: "))

        if ecupo1 >= 0:
            ecupo2 = math.sqrt(ecupo1)
            print("x =", ecupo2)
            print("Tambien existe x =", -ecupo2)
        else:
            print("No existe una solucion real.")

    elif opccion == 9:
        porcentaje1 = float(input("Seleccione un numero: "))
        porcentaje2 = float(input("Seleccione el porcentaje: "))

        porcentaje3 = porcentaje1 * (porcentaje2 / 100)

        print("Resultado:", porcentaje3)

    elif opccion == 10:
        print("\nTRIGONOMETRIA")
        print("1.- SIN")
        print("2.- COS")
        print("3.- TAN")

        trigonometria2 = input("Seleccione SIN, COS o TAN: ").upper()
        trigonometria1 = float(input("Seleccione los grados: "))

        radianes = math.radians(trigonometria1)

        if trigonometria2 == "SIN":
            trigonometria3 = math.sin(radianes)
            print("Resultado:", trigonometria3)

        elif trigonometria2 == "COS":
            trigonometria4 = math.cos(radianes)
            print("Resultado:", trigonometria4)

        elif trigonometria2 == "TAN":
            trigonometria5 = math.tan(radianes)
            print("Resultado:", trigonometria5)

        else:
            print("Opcion no valida.")

    elif opccion == 11:
        print("\nFORMULAS")
        print("1.- Teorema de Pitagoras")
        print("2.- Area triangulo")
        print("3.- Area circulo")
        print("4.- Perimetro rectangulo")
        print("5.- Velocidad")
        print("6.- Tiempo")
        print("7.- Distancia")

        formula1 = int(input("Seleccione una: "))

        if formula1 == 1:
            print("a^2 + b^2 = c^2")
            print("c^2 - b^2 = a^2")
            print("c^2 - a^2 = b^2")

        elif formula1 == 2:
            print("A = (b x h) / 2")

        elif formula1 == 3:
            print("A = pi x r^2")

        elif formula1 == 4:
            print("P = 2(b + h)")

        elif formula1 == 5:
            print("V = distancia / tiempo")

        elif formula1 == 6:
            print("T = distancia / velocidad")

        elif formula1 == 7:
            print("D = velocidad x tiempo")

        else:
            print("Opcion no valida.")

    elif opccion == 12:
        print("Saliendo de CALCULADORA ATLAS...")
        break

    else:
        print("Opcion no valida.")