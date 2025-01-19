

# diccionario
carrito = []

# funcion que pregunta si se quiere añadir más artículos al carrito de la compra

def pregunta():
    respuesta = input ("¿Quieres añadir artículos a la lista (Si/No)?---- ")
    respuesta = respuesta.upper()
    if (respuesta == "SI" or respuesta == "S"):
        seguirComprando()
    elif (respuesta == "NO" or respuesta == "N"):
        imprimeTicket()

def seguirComprando():
    articuloNuevo = input("Introduce un artículo: ")
    precioNuevo = float(input(f"Introduce el precio de {articuloNuevo}: "))
    carrito.append({"articulo": articuloNuevo, "precio": precioNuevo})
    pregunta()

def imprimeTicket():
    print("Lista de la compra")
    cadaCosa = list(carrito[0].keys())
    valores = len(cadaCosa)
    for i in range(len(carrito)):
        print(f"{carrito[i][cadaCosa[valores-2]]} con precio {carrito[i][cadaCosa[valores-1]]}")
    total(len(carrito))

def total(rango):
    costeTotal = 0
    for j in range(rango):
        costeTotal += carrito[j]["precio"]
    print(f"Coste total {costeTotal}")


seguirComprando()


