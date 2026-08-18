Pr1 = input("Seleccione la unidad que quiere convertir: ")
Pr2 = input("Seleccione a qué unidad quiere convertirla: ")
Grados = float(input("¿Cuántos grados?: "))

if Pr1 == "celsius":
    if Pr2 == "kelvin":
        R1 = Grados + 273.15
        print("Tus grados en kelvin son:", R1)
if Pr1 == "celsius":
    if Pr2 == "fahrenheit":
        R2 = (Grados * 9 / 5) + 32
        print("Tus grados en fahrenheit serian:",R2)
if Pr1 == "kelvin":
    if Pr2 == "celsius":
        R3 = Grados - 273.15
        print("Tus grados en celsius son:", R3)
if Pr1 == "kelvin":
    if Pr2 == "fahrenheit":
        R4 = (Grados - 273.15) * 9 / 5 + 32
        print("Tus grados en fahrenheit son:", R4)
if Pr1 == "fahrenheit":
    if Pr2 == "celsius":
        R5 = (Grados - 32) * 5 / 9
        print("Tus grados en celsius son:", R5)
if Pr1 == "fahrenheit":
    if Pr2 == "kelvin":
        R6 = (Grados - 32) * 5 / 9 + 273.15
        print("Tus grados en kelvin son:", R6)
if Pr1 not in ["celsius", "fahrenheit", "kelvin"]:
    print("No uses mayusculas y escribe el nombre bien")
if Pr2 not in ["celsius", "fahrenheit", "kelvin"]:
    print("No uses mayusculas y escribe bien el nombre, tambien escoge entre celsius, fahrenheit o kelvin")
