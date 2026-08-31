tareas = []

while True:

    deci = input("Bienvenido al sistema de tareas, para agregar una tarea presione 1, para ver tus tareas presione 2, para eliminar una tarea presione 3, presione 4 para salir: ")

    if deci == "1":
        tareas.append(input("Escriba la tarea que quiere agregar: "))

    elif deci == "2":
        if not tareas:
            print("Usted no tiene tareas agregadas")
        else:
            for tarea in tareas:
                print(tarea)

    elif deci == "3":
        eliminar = input("Seleccione la tarea que quiere eliminar: ")

        if eliminar in tareas:
            tareas.remove(eliminar)
            print("Tarea eliminada")
        else:
            print("Escriba el nombre de la tarea tal cual como la guardó")

    elif deci == "4":
        break