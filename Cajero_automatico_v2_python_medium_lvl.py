deudas = []
saldo = 0
cuentas = {}

while True:
    print("\n=== CAJERO ATLAS ===")
    print("1. Iniciar sesión")
    print("2. Crear cuenta")
    print("3. Salir")

    inicio = input("Seleccione una opción: ")

    if inicio == "1":
        tarjeta = input("Ingrese su número de tarjeta: ")

        if tarjeta in cuentas:
            contraseña = input("Ingrese su NIP de seguridad: ")

            if contraseña == cuentas[tarjeta]["contraseña"]:
                print("\nInicio de sesión exitoso.")

                while True:
                    print("\n=== MENÚ PRINCIPAL ===")
                    print("1. Consultar saldo")
                    print("2. Retirar dinero")
                    print("3. Depositar dinero")
                    print("4. Consultar deudas")
                    print("5. Agregar deuda")
                    print("6. Eliminar deuda")
                    print("7. Cerrar sesión")

                    opcc = input("Seleccione una opción: ")

                    if opcc == "1":
                        print("Su saldo es de",
                              cuentas[tarjeta]["saldo"], "$")

                    elif opcc == "2":
                        retiro = float(input(
                            "¿Cuánto dinero desea retirar?: "
                        ))

                        if retiro <= 0:
                            print("La cantidad debe ser mayor que cero.")
                        elif retiro <= cuentas[tarjeta]["saldo"]:
                            cuentas[tarjeta]["saldo"] -= retiro
                            print("Retiro exitoso.")
                            print("Saldo actual:",
                                  cuentas[tarjeta]["saldo"], "$")
                        else:
                            print("No tiene suficiente saldo.")

                    elif opcc == "3":
                        deposito = float(input(
                            "¿Cuánto dinero desea depositar?: "
                        ))

                        if deposito > 0:
                            cuentas[tarjeta]["saldo"] += deposito
                            print("Depósito exitoso.")
                            print("Saldo actual:",
                                  cuentas[tarjeta]["saldo"], "$")
                        else:
                            print("La cantidad debe ser mayor que cero.")

                    elif opcc == "4":
                        if not cuentas[tarjeta]["deudas"]:
                            print("No tiene deudas.")
                        else:
                            for i, deuda in enumerate(
                                cuentas[tarjeta]["deudas"], start=1
                            ):
                                print(i, "-", deuda["nombre"],
                                      "-", deuda["cantidad"], "$")

                    elif opcc == "5":
                        nombre = input("¿De qué es la deuda?: ")
                        cantidad = float(input(
                            "¿Cuánto dinero debe?: "
                        ))

                        if cantidad > 0:
                            cuentas[tarjeta]["deudas"].append({
                                "nombre": nombre,
                                "cantidad": cantidad
                            })
                            print("Deuda agregada.")
                        else:
                            print("La cantidad debe ser mayor que cero.")

                    elif opcc == "6":
                        if not cuentas[tarjeta]["deudas"]:
                            print("No tiene deudas para eliminar.")
                        else:
                            for i, deuda in enumerate(
                                cuentas[tarjeta]["deudas"], start=1
                            ):
                                print(i, "-", deuda["nombre"],
                                      "-", deuda["cantidad"], "$")

                            eliminar = input(
                                "Escriba el número de la deuda que desea "
                                "eliminar: "
                            )

                            if eliminar.isdigit():
                                posicion = int(eliminar) - 1

                                if 0 <= posicion < len(
                                    cuentas[tarjeta]["deudas"]
                                ):
                                    cuentas[tarjeta]["deudas"].pop(posicion)
                                    print("Deuda eliminada.")
                                else:
                                    print("Número de deuda incorrecto.")
                            else:
                                print("Introduzca un número válido.")

                    elif opcc == "7":
                        print("Sesión cerrada.")
                        break

                    else:
                        print("Opción no válida.")

            else:
                print("NIP incorrecto.")

        else:
            print("La tarjeta no está registrada.")

    elif inicio == "2":
        tarjeta = input("Cree un número de tarjeta ficticio: ")

        if tarjeta in cuentas:
            print("Esa tarjeta ya está registrada.")
        elif not tarjeta:
            print("El número de tarjeta no puede estar vacío.")
        else:
            contraseña = input("Cree un NIP de seguridad: ")

            if not contraseña:
                print("El NIP no puede estar vacío.")
            else:
                cuentas[tarjeta] = {
                    "contraseña": contraseña,
                    "saldo": 0,
                    "deudas": []
                }
                print("Cuenta creada correctamente.")

    elif inicio == "3":
        print("Gracias por usar el Cajero Atlas.")
        break

    else:
        print("Opción no válida.")