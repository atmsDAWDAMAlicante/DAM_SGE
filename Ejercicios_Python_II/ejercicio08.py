usuario = {
    "nombre": "4",
    "edad": 0,
    "direccion": "",
    "telefono": ""
}

listaClaves = list(usuario.keys()) # hay que poner el list para que sea como un array
print (listaClaves) #=> ['nombre', 'edad', 'direccion', 'telefono']

for i in range (len(listaClaves)):
    #print (str(listaClaves[i])) no hace falta el str()
    # print (usuario[listaClaves[i]]) ESTA ES LA CLAVE: ESTO IMPRIME LOS VALORES
    usuario[listaClaves[i]] = input(f"Introduce {listaClaves[i]}: ") # Con un literal pide cada clave
# Impresión del resultado con literales
print (f"{usuario["nombre"]} tiene {usuario["edad"]} años, vive en {usuario["direccion"]} y su número de teléfono es {usuario["telefono"]}")