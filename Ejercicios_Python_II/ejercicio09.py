
# Usuario vacío - diccionario
usuario = {
    "nombre":"",
    "primer apellido":"",
    "edad":"",
    "sexo":"",
    "telefono":"",
    "correo electronico":""
}

# Convierte la lista de claves en un array
listaClaves = list(usuario.keys())

# El bucle pide cada dato y lo imprime
for i in range (len(listaClaves)):
    usuario[listaClaves[i]] = input(f"Introduce tu {listaClaves[i]}: ")
    print(f"Tu {listaClaves[i]} es {usuario[listaClaves[i]]}")