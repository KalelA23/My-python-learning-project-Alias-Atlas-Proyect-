# JUEGO DE SUPERVIVENCAI CON INICIO DE SESION V1
from time import sleep
from random import randint, choice

contraseñas = []
inventory = []

comida = [
    "Lata de verduras",
    "Lata de frijoles",
    "Lata de carne molida",
    "Dulces"
]

comida_sospechosa = [
    "Comida para perros",
    "Comida para gatos",
    "Lata de verduras abollada",
    "Lata de atun caducada"
]

bebida = [
    "Agua",
    "Agua de coco",
    "Bebida refrescante",
    "Refresco"
]

bebida_sospechosa = [
    "Botella con liquido amarillo",
    "Leche pasada",
    "Agua de cactus"
]

curacion = [
    "Botiquin",
    "Vendajes",
    "Kit de primeros auxilios",
    "Alcohol desinfectador",
    "Medicina"
]

curacion_sospechosa = [
    "Vendaje mojado",
    "Desfibrilador",
    "Remedio casero",
    "Kit de masajes"
]

numeros_suertudos = [
    1, 2, 4, 5, 6, 32, 23, 3, 6, 8, 3,
    74, 26, 17, 2, 7, 87, 95, 53, 86, 13
]

numeros_desafortunados = [
    15, 25, 35, 45, 65, 75, 85, 95,
    100, 12, 24, 38, 50, 62, 74, 86
]

edificio = [
    "Hospital abandonado",
    "Supermercado",
    "Farmacia",
    "Refugio de supervivientes pacificos",
    "Ciudad abandonada"
]

edificio_sospechoso = [
    "Manicomnio",
    "Refugio de saqueadores",
    "Ciudad infestada",
    "Fabrica nuclear"
]

health = 100
hunger = 100
thirsty = 100

mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
minusculas = "abcdefghijklmnñopqrstuvwxyz"
números = "0123456789"
signos = "!@#&/?¡¿"


# INICIO DEL PROGRAMA
print("SISTEMA DE ALMACENAMIENTO DE DATOS ATLAS")

while True:
    print("\n1. Iniciar sesion")
    print("2. Crear cuenta")
    print("3. Salir")

    acceso = input("Seleccione: ")

    # INICIO DE SESION
    if acceso == "1":
        user_login = input("Usuario: ")
        password_login = input("Contraseña: ")

        cuenta_encontrada = False

        for cuenta in contraseñas:
            if user_login == cuenta[0] and password_login == cuenta[1]:
                cuenta_encontrada = True
                break

        if cuenta_encontrada:
            print("Cargando...")
            sleep(2)
            print("¡Inicio de sesion exitoso!")

            # JUEGO DE SUPERVIVENCIA
            while True:
                print("\n===== JUEGO DE SUPERVIVENCIA ATLAS =====")
                print("Vida:", health, "/100")
                print("Hambre:", hunger, "/100")
                print("Sed:", thirsty, "/100")
                print("Inventario:", inventory)

                print("\n1. Salir a explorar")
                print("2. Comer algo del inventario")
                print("3. Beber algo del inventario")
                print("4. Curarse con algo del inventario")
                print("5. Cerrar sesion")

                select = input("Seleccione: ")

                # EXPLORAR
                if select == "1":
                    estructura = randint(1, 100)

                    if estructura in numeros_suertudos:
                        lugar = choice(edificio)
                        print("¡Has encontrado un:", lugar, "!")

                        if lugar == "Supermercado":
                            objeto = choice(comida + bebida)
                            inventory.append(objeto)
                            print("Has encontrado:", objeto)

                        elif lugar == "Hospital abandonado":
                            objeto = choice(curacion)
                            inventory.append(objeto)
                            print("Has encontrado:", objeto)

                        elif lugar == "Farmacia":
                            objeto = choice(curacion)
                            inventory.append(objeto)
                            print("Has encontrado:", objeto)

                        elif lugar == "Refugio de supervivientes pacificos":
                            objeto = choice(comida + bebida + curacion)
                            inventory.append(objeto)
                            print("Has encontrado:", objeto)

                        elif lugar == "Ciudad abandonada":
                            objeto = choice(comida + bebida + curacion)
                            inventory.append(objeto)
                            print("Has encontrado:", objeto)

                    elif estructura in numeros_desafortunados:
                        lugar = choice(edificio_sospechoso)
                        print("¡Has encontrado un lugar peligroso:", lugar, "!")

                        if lugar == "Refugio de saqueadores":
                            print("Los saqueadores te han atacado.")
                            health -= 20

                        elif lugar == "Ciudad infestada":
                            print("Has sufrido una herida al escapar.")
                            health -= 15

                        elif lugar == "Fabrica nuclear":
                            print("La zona peligrosa te ha debilitado.")
                            health -= 25

                        elif lugar == "Manicomnio":
                            print("Te has perdido en el edificio.")
                            hunger -= 10
                            thirsty -= 10

                    else:
                        print("No has encontrado ninguna estructura.")
                        hunger -= 5
                        thirsty -= 5

                # COMER
                elif select == "2":
                    alimentos = [
                        objeto for objeto in inventory
                        if objeto in comida
                    ]

                    if alimentos:
                        print("Alimentos disponibles:", alimentos)
                        objeto = input("¿Que deseas comer?: ")

                        if objeto in alimentos:
                            inventory.remove(objeto)
                            hunger = min(100, hunger + 25)
                            print("Has comido:", objeto)
                            print("Hambre:", hunger, "/100")
                        else:
                            print("Ese alimento no esta en tu inventario.")
                    else:
                        print("No tienes alimentos en tu inventario.")

                # BEBER
                elif select == "3":
                    bebidas = [
                        objeto for objeto in inventory
                        if objeto in bebida
                    ]

                    if bebidas:
                        print("Bebidas disponibles:", bebidas)
                        objeto = input("¿Que deseas beber?: ")

                        if objeto in bebidas:
                            inventory.remove(objeto)
                            thirsty = min(100, thirsty + 30)
                            print("Has bebido:", objeto)
                            print("Sed:", thirsty, "/100")
                        else:
                            print("Esa bebida no esta en tu inventario.")
                    else:
                        print("No tienes bebidas en tu inventario.")

                # CURARSE
                elif select == "4":
                    medicamentos = [
                        objeto for objeto in inventory
                        if objeto in curacion
                    ]

                    if medicamentos:
                        print("Objetos de curacion:", medicamentos)
                        objeto = input("¿Que deseas utilizar?: ")

                        if objeto in medicamentos:
                            inventory.remove(objeto)
                            health = min(100, health + 30)
                            print("Has utilizado:", objeto)
                            print("Vida:", health, "/100")
                        else:
                            print("Ese objeto no esta en tu inventario.")
                    else:
                        print("No tienes objetos de curacion.")

                # CERRAR SESION
                elif select == "5":
                    print("Cerrando sesion...")
                    break

                else:
                    print("Opcion no valida.")

                # COMPROBAR ESTADO
                hunger = max(0, min(100, hunger))
                thirsty = max(0, min(100, thirsty))
                health = max(0, min(100, health))

                if hunger == 0:
                    health -= 5
                    print("¡El hambre esta afectando tu vida!")

                if thirsty == 0:
                    health -= 10
                    print("¡La falta de agua esta afectando tu vida!")

                health = max(0, health)

                if health == 0:
                    print("\n¡Has perdido toda tu vida!")
                    print("Fin de la partida.")
                    break

        else:
            print("Usuario o contraseña incorrectos.")

    # CREAR CUENTA
    elif acceso == "2":
        user_create = input("Ingrese un nombre de usuario: ")

        usuario_repetido = False

        for cuenta in contraseñas:
            if user_create == cuenta[0]:
                usuario_repetido = True
                break

        if usuario_repetido or user_create == "":
            print("El usuario esta vacio o ya existe.")
            continue

        password_create = input(
            "Contraseña (mayusculas, minusculas, numeros y signos): "
        )

        tiene_mayuscula = False
        tiene_minuscula = False
        tiene_numero = False
        tiene_signo = False

        for caracter in password_create:
            if caracter in mayusculas:
                tiene_mayuscula = True
            if caracter in minusculas:
                tiene_minuscula = True
            if caracter in números:
                tiene_numero = True
            if caracter in signos:
                tiene_signo = True

        if (tiene_mayuscula and tiene_minuscula
                and tiene_numero and tiene_signo):

            contraseñas.append([user_create, password_create])
            print("Creando cuenta...")
            sleep(2)
            print("¡Cuenta creada exitosamente!")

        else:
            print(
                "Contraseña invalida. Debe contener mayusculas, "
                "minusculas, numeros y signos."
            )

    # SALIR
    elif acceso == "3":
        print("Que tenga un buen dia.")
        break

    else:
        print("Opcion no valida.")