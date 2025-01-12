numero = int(input("Introduce un número entero: "))
for i in range (1, numero+1, 2):
    resultado = ""
    for j in range (i, 0, -2):
        resultado += (str(j) + ", ")
    print(resultado)
