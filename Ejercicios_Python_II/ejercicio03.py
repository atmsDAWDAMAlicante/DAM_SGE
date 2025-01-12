listaNumeros = []
for i in range(10):
    listaNumeros.append(i+1)
for j in range ((len(listaNumeros)-1),-1,-1):# hay que recordar que el último número del bucle no lo pone Python
    print (str(listaNumeros[j]))