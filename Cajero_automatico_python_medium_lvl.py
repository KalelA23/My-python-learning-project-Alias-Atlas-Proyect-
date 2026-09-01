deudas = []
saldo = 0
deudaspor = []

while True:
    opcc = input("Bienvenido al sistema de cajero automatico, para ver su saldo marque 1, para retirar dinero marque 2, para depositar dinero marque 3, para consultar deudas marque 4, para agregar deudas marque 5, para eliminar deudas marque 6, para salir marque 7: ")

    if opcc == "1":
        print("Su saldo es de", saldo, "$")

    elif opcc == "2":
        retiro = float(input("Seleccione cuanto dinero quiere retirar: "))

        if retiro <= saldo:
            saldo = saldo - retiro
            print("Ahora su saldo es de:", saldo, "$")
        else:
            print("No tiene suficiente saldo.")

    elif opcc == "3":
        deposito = float(input("Seleccione cuanto dinero quiere depositar: "))
        saldo = saldo + deposito
        print("Ahora su saldo es de:", saldo, "$")

    elif opcc == "4":
        if not deudas:
            print("No tiene deudas.")
        else:
            for i in range(len(deudas)):
                print(deudaspor[i], "-", deudas[i], "$")

    elif opcc == "5":
        cantidad = float(input("Escriba de cuanto dinero es la deuda: "))
        nombre = input("Escriba de que es la deuda: ")

        deudas.append(cantidad)
        deudaspor.append(nombre)

        print("Deuda agregada.")

    elif opcc == "6":
        eliminar = input("Escriba el nombre de la deuda que quiere eliminar: ")

        if eliminar in deudaspor:
            posicion = deudaspor.index(eliminar)
            deudaspor.remove(eliminar)
            deudas.pop(posicion)
            print("Deuda eliminada.")
        else:
            print("No existe una deuda con ese nombre.")

    elif opcc == "7":
        print("Gracias por usar el cajero.")
        break

    else:
        print("Opcion no valida.")