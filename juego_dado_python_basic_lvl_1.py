import random
uno = 0
dos = 0
tres = 0
cuatro = 0
cinco = 0
seis = 0
for i in range(100):
    resultado = random.randint(1,6)
    if resultado == 1:
        uno += 1
    elif resultado == 2:
        dos += 1
    elif resultado == 3:
        tres += 1
    elif resultado == 4:
        cuatro += 1
    elif resultado == 5:
        cinco += 1
    elif resultado == 6:
        seis += 1
print("Las veces que aparecieron cada numero fueron:")
print("1:", uno)
print("2:", dos)
print("3:", tres)
print("4:", cuatro)
print("5:", cinco)
print("6:", seis)
