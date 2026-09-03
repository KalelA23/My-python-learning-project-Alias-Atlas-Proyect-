numeros = []

for i in range(10):
    numero = int(input("Escribe un número: "))
    numeros.append(numero)

mayor = numeros[0]

for numero in numeros:
    if numero > mayor:
        mayor = numero

menor = numeros[0]

for numero in numeros:
    if numero < menor:
        menor = numero

par = 0

for numero in numeros:
    if numero % 2 == 0:
        par += 1

impar = 0

for numero in numeros:
    if numero % 2 != 0:
        impar += 1

suma = 0

for numero in numeros:
    suma += numero

promedio = suma / 10

print("Mayor:", mayor)
print("Menor:", menor)
print("Pares:", par)
print("Impares:", impar)
print("Promedio:", promedio)
print("Suma de todos:", suma)