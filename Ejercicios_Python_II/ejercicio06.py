lista = []

def numero(num):
    lista.append(num)

def media(numeros):
    resultado = 0
    for j in numeros:
        resultado += j
    print (f'La media es: {str(resultado/len(lista))}')

for i in range (5):
   numero(int(input(f"Introduce el número {i+1}º: ")))
   
print(media(lista))