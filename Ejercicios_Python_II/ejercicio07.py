lista = []

def numero(num):
    lista.append(num)

def losNumeros(numeros):
    mayor = lista[0]
    menor = lista[0]
    for j in numeros:
        if (mayor < j):
            mayor = j
        if (menor > j):
            menor = j

    print (f'El mayor es {mayor} y el menor es {menor}')

for i in range (5):
   numero(int(input(f"Introduce el número {i+1}º: ")))
   
losNumeros(lista)