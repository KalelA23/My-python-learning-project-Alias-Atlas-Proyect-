numero = int(input("Seleccione el numero y le indicare si es par, impar o primo: "))

if numero % 2 == 0:
    print("Su numero es par!")
else:
    print("Su numero es impar!")

es_primo = True

if numero < 2:
    es_primo = False
else:
    for divisor in range(2, numero):
        if numero % divisor == 0:
            es_primo = False
            break

if es_primo:
    print("Su numero ES primo")
else:
    print("Su numero NO es primo")