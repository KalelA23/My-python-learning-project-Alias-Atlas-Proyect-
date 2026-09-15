while True:
    print("SISTEMA DE PRECIOS ATLAS")
    print("1.- CALCULAR DESCUENTO")
    print("2.- CALCULAR AUMENTO")
    print("3.- CALCULAR IVA")
    print("4.- CALCULAR PRECIO FINAL")
    print("5.- CALCULAR Y COMPARAR DOS PRECIOS")
    print("6.- CALCULAR PRECIO FINAL IVA")
    print("7.- CALCULAR PORCENTAJE DE UN PRECIO")
    print("8.- CALCULAR PRECIO ORIGINAL")
    print("9.- SALIR")

    seleccion = int(input("Seleccione la opcion que desea usar: "))

    if seleccion == 1:
        descuento1 = float(input("Seleccione el precio del producto: "))
        descuento2 = int(input("Seleccione la cantidad del porcentaje: "))
        descuento3 = descuento1 * (descuento2 / 100)
        print("El descuento es:", descuento3)

    elif seleccion == 2:
        aumento1 = float(input("Seleccione el precio del producto: "))
        aumento2 = int(input("Seleccione cuanto aumento su valor: "))
        aumento3 = aumento1 * (aumento2 / 100)
        print("El aumento es:", aumento3)

    elif seleccion == 3:
        iva1 = float(input("Seleccione el precio del producto: "))
        iva2 = int(input("Indique de cuanto es el IVA: "))
        iva3 = iva1 * (iva2 / 100)
        print("El IVA es:", iva3)

    elif seleccion == 4:
        preciof1 = float(input("Seleccione el precio del producto: "))
        preciof2 = float(input("Seleccione la cantidad del descuento: "))
        preciof3 = preciof1 * (preciof2 / 100)
        preciof4 = preciof1 - preciof3
        print("El precio final es:", preciof4)

    elif seleccion == 5:
        comparar1 = float(input("Seleccione el precio del primer producto: "))
        comparar2 = float(input("Seleccione el precio del segundo producto que sera comparado: "))

        comparar3 = ((comparar2 - comparar1) / comparar1) * 100

        print("La diferencia porcentual es:", comparar3, "%")

    elif seleccion == 6:
        ivaf1 = float(input("Seleccione el precio del producto: "))
        ivaf2 = int(input("Indique de cuanto es el IVA: "))
        ivaf3 = ivaf1 * (ivaf2 / 100)
        ivaf4 = ivaf1 + ivaf3
        print("El precio final con IVA es:", ivaf4)

    elif seleccion == 7:
        porcentaje1 = float(input("Seleccione el precio del producto: "))
        porcentaje2 = int(input("Seleccione cuanto se le resta o suma al producto: "))
        porcentaje3 = (porcentaje2 / porcentaje1) * 100
        print("El porcentaje es:", porcentaje3, "%")

    elif seleccion == 8:
        original1 = float(input("Seleccione de cuanto es el precio ya con descuento: "))
        original2 = int(input("Seleccione de cuanto es el descuento: "))
        original3 = original1 / (1 - (original2 / 100))
        print("El precio original es:", original3)

    elif seleccion == 9:
        print("Gracias por usar SISTEMA DE PRECIOS ATLAS")
        break

    else:
       print("Seleccione una opccion valida")