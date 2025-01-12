numero_int = int(input("Introduce un numero entero y positivo: "))
for i in range(numero_int, 0, -1): # -1 para decrementar el contador; 0 para que salga 1
    print(i, end=', ') # recordatorio: end para evitar el salto de línea