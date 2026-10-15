
from random import randint

enemigos = ["lobo", "zorro", "oso", "humano", "serpiente"]

objetos = [
    "espada", "zapato roto", "pistola", "municion",
    "arco", "linterna", "comida", "agua",
    "bebida energetica", "vendaje", "medikit"
]

edificios = [
    "biblioteca", "hospital", "comisaria",
    "escuela", "base militar", "casa abandonada"
]

mala_suerte = (1, 24, 50, 32, 45, 12, 49, 3, 6, 19, 4, 8, 5)

inventario = []

vida = 100
energia = 100
comida = 100
sed = 100

dias = 1
acciones_dia = 0


def registrar_accion():
    global energia, acciones_dia, dias
    global comida, sed, vida

    energia -= 5

    if energia < 0:
        energia = 0

    acciones_dia += 1

    if acciones_dia >= 5:
        dias += 1
        acciones_dia = 0

        comida -= 10
        sed -= 10

        if comida < 0:
            comida = 0

        if sed < 0:
            sed = 0

        print("\nHa comenzado el dia", dias)

        if comida == 0 or sed == 0:
            vida -= 10

            if vida < 0:
                vida = 0

            print("Perdiste vida por falta de comida o agua.")
            print("Vida actual:", vida)


def exploracion():
    lugar = randint(0, len(edificios) - 1)

    print("\nLlegaste a:", edificios[lugar])

    continuar = input("Deseas explorar el lugar? ").lower()

    if continuar == "si" or continuar == "sí":
        peligro = randint(1, 50)

        if peligro in mala_suerte:
            enemigo = enemigos[randint(0, len(enemigos) - 1)]

            print("Encontraste un enemigo:", enemigo)
            batalla(enemigo)

        else:
            numero_objeto = randint(1, 10)

            if numero_objeto <= 2:
                print("No encontraste nada.")

            else:
                objeto = objetos[randint(0, len(objetos) - 1)]

                print("Encontraste:", objeto)

                guardar = input("Deseas guardarlo? ").lower()

                if guardar == "si" or guardar == "sí":
                    inventario.append(objeto)
                    print("Objeto guardado.")

                else:
                    print("Dejaste el objeto.")

    else:
        print("Decidiste no continuar.")


def comer():
    global comida

    print("Alimentacion:", comida)

    respuesta = input("Deseas comer? ").lower()

    if respuesta == "si" or respuesta == "sí":
        if "comida" in inventario:
            comida += 20

            if comida > 100:
                comida = 100

            inventario.remove("comida")

            print("Has comido.")
            print("Nivel de alimentacion:", comida)

        else:
            print("No tienes comida en el inventario.")

    else:
        print("Decidiste no comer.")


def beber():
    global sed

    print("Hidratacion:", sed)

    respuesta = input("Deseas beber agua? ").lower()

    if respuesta == "si" or respuesta == "sí":
        if "agua" in inventario:
            sed += 20

            if sed > 100:
                sed = 100

            inventario.remove("agua")

            print("Has bebido agua.")
            print("Nivel de hidratacion:", sed)

        else:
            print("No tienes agua en el inventario.")

    else:
        print("Decidiste no beber.")


def descanso():
    global energia

    print("Energia:", energia)

    respuesta = input("Deseas descansar? ").lower()

    if respuesta == "si" or respuesta == "sí":
        energia += 25

        if energia > 100:
            energia = 100

        print("Descansaste y recuperaste energia.")

        peligro = randint(1, 50)

        if peligro in mala_suerte:
            enemigo = enemigos[randint(0, len(enemigos) - 1)]

            print("Un enemigo te encontro mientras dormias:", enemigo)
            batalla(enemigo)

    else:
        respuesta = input(
            "Deseas usar una bebida energetica? "
        ).lower()

        if respuesta == "si" or respuesta == "sí":
            if "bebida energetica" in inventario:
                energia += 20

                if energia > 100:
                    energia = 100

                inventario.remove("bebida energetica")

                print("Usaste una bebida energetica.")
                print("Energia actual:", energia)

            else:
                print("No tienes bebidas energeticas.")

        else:
            print("Decidiste no recuperar energia.")


def curarse():
    global vida

    print("Vida:", vida)

    if vida >= 100:
        print("Tu vida ya esta al maximo.")
        return

    respuesta = input("Deseas curarte? ").lower()

    if respuesta == "si" or respuesta == "sí":
        if "vendaje" in inventario or "medikit" in inventario:
            vida += 20

            if vida > 100:
                vida = 100

            if "vendaje" in inventario:
                inventario.remove("vendaje")
            else:
                inventario.remove("medikit")

            print("Te has curado.")
            print("Vida actual:", vida)

        else:
            print("No tienes vendajes ni medikits.")

    else:
        print("Decidiste no curarte.")


def ver_inventario():
    print("\nInventario:", inventario)

    respuesta = input("Deseas tirar un objeto? ").lower()

    if respuesta == "si" or respuesta == "sí":
        objeto = input("Que objeto deseas tirar? ").lower()

        if objeto in inventario:
            inventario.remove(objeto)
            print("Objeto descartado.")
            print("Inventario actual:", inventario)

        else:
            print("Ese objeto no esta en tu inventario.")

    else:
        print("No tiraste ningun objeto.")


def batalla(nombre_enemigo):
    global vida, energia

    vida_enemigo = randint(40, 80)

    print("\nCOMBATE POR TURNOS")
    print("Enemigo:", nombre_enemigo)
    print("Vida del enemigo:", vida_enemigo)

    while vida > 0 and vida_enemigo > 0:

        print("\nTu vida:", vida)
        print("Tu energia:", energia)
        print("Vida del enemigo:", vida_enemigo)

        print("1. Atacar")
        print("2. Curarse")
        print("3. Huir")

        accion = input("Elige tu accion: ")

        if accion == "1":
            if energia == 0:
                print("Estas demasiado cansado para atacar.")
                continue

            dano = randint(15, 30)

            if "espada" in inventario:
                dano += 10
                print("Usaste tu espada.")

            elif "pistola" in inventario and "municion" in inventario:
                dano = randint(30, 45)
                inventario.remove("municion")
                print("Usaste tu pistola y una municion.")

            vida_enemigo -= dano

            if vida_enemigo < 0:
                vida_enemigo = 0

            print("Causaste", dano, "puntos de dano.")

            registrar_accion()

        elif accion == "2":
            if vida >= 100:
                print("Tu vida ya esta al maximo.")
                continue

            if "vendaje" in inventario or "medikit" in inventario:
                vida += 20

                if vida > 100:
                    vida = 100

                if "vendaje" in inventario:
                    inventario.remove("vendaje")
                else:
                    inventario.remove("medikit")

                print("Recuperaste vida:", vida)

                registrar_accion()

            else:
                print("No tienes objetos para curarte.")
                continue

        elif accion == "3":
            registrar_accion()

            if randint(1, 3) == 1:
                print("Lograste escapar.")
                return

            else:
                print("No pudiste escapar.")

        else:
            print("Accion no valida.")
            continue

        if vida <= 0:
            break

        if vida_enemigo <= 0:
            print("Derrotaste al enemigo:", nombre_enemigo)
            break

        dano_enemigo = randint(8, 20)
        vida -= dano_enemigo

        if vida < 0:
            vida = 0

        print(nombre_enemigo, "te causo", dano_enemigo, "puntos de dano.")

    if vida_enemigo <= 0:
        print("Victoria. Sobreviviste al combate.")

    if vida <= 0:
        print("Has sido derrotado.")


while vida > 0:

    print("\n==============================")
    print("JUEGO DE SUPERVIVENCIA ATLAS")
    print("==============================")

    print("Dia:", dias)
    print("Vida:", vida)
    print("Alimentacion:", comida)
    print("Hidratacion:", sed)
    print("Energia:", energia)

    print("\n1. Explorar")
    print("2. Comer")
    print("3. Beber agua")
    print("4. Descansar")
    print("5. Curarse")
    print("6. Ver inventario")
    print("7. Salir del juego")

    opcion = input("Escoge una opcion: ")

    if opcion == "1":
        exploracion()

    elif opcion == "2":
        comer()

    elif opcion == "3":
        beber()

    elif opcion == "4":
        descanso()

    elif opcion == "5":
        curarse()

    elif opcion == "6":
        ver_inventario()

    elif opcion == "7":
        print("Saliste del juego.")
        break

    else:
        print("Opcion no valida.")
        continue

    if vida > 0:
        registrar_accion()

if vida <= 0:
    print("\nFIN DEL JUEGO")
    print("Sobreviviste", dias, "dias.")
