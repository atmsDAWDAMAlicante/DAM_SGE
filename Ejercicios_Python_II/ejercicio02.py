modulos = ["SGE", "Acceso a Datos", "EIE", "Inglés", "Cliente"]
notas = []
for nota in range(len(modulos)):
    #pass
    notas.append(int(input("Introduce la nota de la asignatura " + modulos[nota] + ": ")))
print("Notas introducidas")
for resultados in range(len(modulos)):
    print("Asignatura: " + modulos[resultados] + " / calificación: " + str(notas[resultados]))