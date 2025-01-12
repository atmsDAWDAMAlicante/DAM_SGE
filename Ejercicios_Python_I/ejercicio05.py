numero_input = input("Introduce un número entero: ")
numero_int = int(numero_input)
if (numero_int % 2 == 0):
    print("El número " + str(numero_int) + " es par")
else:
    print("El número " + str(numero_int) + " es impar")