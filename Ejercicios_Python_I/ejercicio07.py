numero_input = input("Introduce un número entero positivo: ")
numero_int = int(numero_input)
for i in range (1, numero_int+1 ,2): #hay que sumar uno al límite ya que el contador no incluye el último número
    print(i, end=", ") # este end evita el salto de línea
