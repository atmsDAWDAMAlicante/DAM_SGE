
intento = 0

while (intento < 5):
    password = input("Introduce la contraseña: (que es 1234): ")
    if (password != "1234"):
        intento+=1
        print("Llevas " + str(intento) + " intentos")
    else: 
        print("Bienvenido")
        break
if (intento == 5):
    print("Has superado el número de intentos")
