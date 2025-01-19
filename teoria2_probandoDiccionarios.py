

diccionario1 = {
    "nombre": "Angel",
    "edad": 54
}
lista = list(diccionario1.keys())
print(lista)
valores = diccionario1.values()
print(valores)
print(diccionario1["nombre"])
print(diccionario1[f"{lista[0]}"])