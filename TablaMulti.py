# Programa pra crear la tbla de mult de un numero ingresado

numero=float(input("ingrese el numero:"))

for i in range(1,11):
    resultado=numero*i
    print(f"{numero}x{i}={resultado}")