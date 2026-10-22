empleados = {}


def comparar_eficacia(empleados):
    if len(empleados) == 0:
        print("No hay empleados registrados")

    else:
        lista_empleados = list(empleados.items())

        for i in range(len(lista_empleados)):
            for j in range(i + 1, len(lista_empleados)):
                if lista_empleados[i][1]["Eficacia"] < lista_empleados[j][1]["Eficacia"]:
                    temporal = lista_empleados[i]
                    lista_empleados[i] = lista_empleados[j]
                    lista_empleados[j] = temporal

        mayor = lista_empleados[0][1]["Eficacia"]
        menor = lista_empleados[-1][1]["Eficacia"]

        print("\n--- EMPLEADOS ORDENADOS POR EFICACIA ---")

        for apellido, datos in lista_empleados:
            print("Apellido:", datos["Apellido"])
            print("Puesto:", datos["Puesto"])
            print("Coeficiente de eficacia:", datos["Eficacia"])
            print("--------------------")

        print("\n--- EMPLEADOS MÁS EFICACES ---")

        for apellido, datos in lista_empleados:
            if datos["Eficacia"] == mayor:
                print(datos["Apellido"], "-", datos["Eficacia"])

        print("\n--- EMPLEADOS MENOS EFICACES ---")

        for apellido, datos in lista_empleados:
            if datos["Eficacia"] == menor:
                print(datos["Apellido"], "-", datos["Eficacia"])


while True:
    decision = input(
        "\n1.- Ver empleados\n"
        "2.- Agregar a un empleado\n"
        "3.- Eliminar a un empleado\n"
        "4.- Comparar eficacia de empleados\n"
        "5.- Ver proyectos anteriores\n"
        "6.- Salir\n"
        "Elija una opción: "
    )

    if decision == "1":
        see_employes = input(
            "1.- Ver todos los empleados\n"
            "2.- Ver un empleado en específico\n"
            "Elija una opción: "
        )

        if see_employes == "1":
            if len(empleados) == 0:
                print("No hay empleados registrados")
            else:
                for apellido, datos in empleados.items():
                    print("Apellido:", datos["Apellido"])
                    print("Puesto:", datos["Puesto"])
                    print("Coeficiente de eficacia:", datos["Eficacia"])
                    print("--------------------")

        elif see_employes == "2":
            see_especific = input(
                "Inserte el apellido del empleado: "
            ).lower()

            if see_especific in empleados:
                print("Apellido:", empleados[see_especific]["Apellido"])
                print("Puesto:", empleados[see_especific]["Puesto"])
                print("Coeficiente de eficacia:",
                      empleados[see_especific]["Eficacia"])
            else:
                print("Empleado no encontrado")

        else:
            print("Opción no válida")

    elif decision == "2":
        last_name = input("Inserte el apellido: ").lower()

        if last_name in empleados:
            print("Ya existe un empleado con ese apellido")

        else:
            job = input("Inserte su puesto: ").lower()
            efficiency = int(input("Inserte su coeficiente de eficacia: "))

            empleados[last_name] = {
                "Apellido": last_name,
                "Puesto": job,
                "Eficacia": efficiency
            }

            print("¡Empleado agregado con éxito!")

    elif decision == "3":
        delete_employee = input(
            "Escriba el apellido del empleado que desea eliminar: "
        ).lower()

        if delete_employee in empleados:
            del empleados[delete_employee]
            print("¡Empleado eliminado con éxito!")
        else:
            print("Empleado no encontrado")

    elif decision == "4":
        comparar_eficacia(empleados)

    elif decision == "5":
        print("\n--- ÚLTIMOS TRES PROYECTOS ---")
        print("Primer proyecto: ChatBot")
        print("Segundo proyecto: Quiz de Python")
        print("Tercer proyecto: Analizador de datos")

    elif decision == "6":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida")