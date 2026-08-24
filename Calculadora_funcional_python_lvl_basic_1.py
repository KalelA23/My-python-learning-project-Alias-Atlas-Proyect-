Cal1 = input("Seleccione la operación (+, -, x, división, potencia, raiz o pitagoras): ")

if Cal1 == "+":
    Cal2n1 = float(input("Seleccione un numero para hacer la suma:     "))
    Cal2n2 = float(input("Seleccione otro numero para hacer la suma:     "))
    Cal2o = Cal2n1 + Cal2n2
    print("El resultado de la suma es:", Cal2o)

elif Cal1 == "-":
    Cal3n1 = float(input("Seleccione un numero para hacer la resta:     "))
    Cal3n2 = float(input("Seleccione otro numero para hacer la resta:     "))
    Cal3o = Cal3n1 - Cal3n2
    print("El resultado es:", Cal3o)

elif Cal1 == "x":
    Cal4n1 = float(input("Seleccione un numero para la multiplicación:      "))
    Cal4n2 = float(input("Seleccione otro numero para hacer la multiplicación:      "))
    Cal4o = Cal4n1 * Cal4n2
    print("El resultado es:", Cal4o)

elif Cal1 == "división":
    Cal5n1 = float(input("Seleccione el numero que sera dividido:          "))
    Cal5n2 = float(input("Seleccione el numero que sera el divisor:         "))
    Cal5o = Cal5n1 / Cal5n2
    print("El resultado es:", Cal5o)

elif Cal1 == "potencia":
    Cal6n1 = float(input("Seleccione el numero para potencia:          "))
    Cal6n2 = int(input("Seleccione el numero para el potenciador:        "))
    Cal6no = Cal6n1 ** Cal6n2
    print("El resultado es:", Cal6no)

elif Cal1 == "raiz":
    Cal7n1 = float(input("Seleccione el numero para hacer raiz cuadrada:          "))
    Cal7no = Cal7n1 ** (1/2)
    print("El resultado es:", Cal7no)

elif Cal1 == "pitagoras":
    Cal8n1 = input("Indique que cateto intenta encontrar a, b o c: ")

    if Cal8n1 == "c":
        Cal8n2 = float(input("Indique la cantidad del cateto a:    "))
        Cal8n3 = float(input("Indique la cantidad del cateto b:    "))

        Cal8o1 = Cal8n2 ** 2
        Cal8o2 = Cal8n3 ** 2
        Cal8o3 = (Cal8o1 + Cal8o2) ** (1/2)

        print("La hipotenusa es:", Cal8o3)

    elif Cal8n1 == "a":
        Cal8n4 = float(input("Indique la cantidad del cateto b:    "))
        Cal8n5 = float(input("Indique la cantidad de la hipotenusa c:    "))

        Cal8o4 = Cal8n4 ** 2
        Cal8o5 = Cal8n5 ** 2
        Cal8o6 = (Cal8o5 - Cal8o4) ** (1/2)

        print("El cateto a equivale a:", Cal8o6)

    elif Cal8n1 == "b":
        Cal8n6 = float(input("Indique la cantidad del cateto a:    "))
        Cal8n7 = float(input("Indique la cantidad de la hipotenusa c:    "))

        Cal8o7 = Cal8n6 ** 2
        Cal8o8 = Cal8n7 ** 2
        Cal8o9 = (Cal8o8 - Cal8o7) ** (1/2)

        print("El cateto b equivale a:", Cal8o9)