import random
import string

Longitud = int(input("Seleccione la cantidad de caracteres que quiere para su contraseña (8, 16, 32 o 50): "))

Mayuscula = input("Elija si o no si quiere que su contraseña contenga mayúsculas: ")
Simbolos = input("Elija si o no si quiere que su contraseña contenga símbolos: ")
Numeros = input("Elija si o no si quiere que su contraseña contenga números: ")
Minuscula = input("Elija si o no si quiere que su contraseña contenga minúsculas: ")

caracteres = ""

if Mayuscula == "si":
    caracteres += string.ascii_uppercase

if Simbolos == "si":
    caracteres += "!@#$%&*"

if Minuscula == "si":
    caracteres += string.ascii_lowercase

if Numeros == "si":
    caracteres += string.digits

if Mayuscula == "si" or Simbolos == "si" or Numeros == "si" or Minuscula == "si":
    contraseña = ""

    for i in range(Longitud):
        contraseña += random.choice(caracteres)

    print("Su contraseña es:", contraseña)
else:
    print("Debes elegir al menos 1 opción")